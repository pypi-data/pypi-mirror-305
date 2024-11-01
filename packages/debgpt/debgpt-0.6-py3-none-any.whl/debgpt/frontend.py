'''
MIT License

Copyright (c) 2024 Mo Zhou <lumin@debian.org>

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
'''
from typing import List, Dict, Union
from rich.status import Status
from rich.panel import Panel
from rich.markup import escape
from rich.markdown import Markdown
from rich.live import Live
import argparse
import os
import json
import rich
import uuid
import sys
import time
import functools as ft
from . import defaults

console = rich.get_console()


def _check(messages: List[Dict]):
    '''
    communitation protocol.
    both huggingface transformers and openapi api use this
    '''
    assert isinstance(messages, list)
    assert all(isinstance(x, dict) for x in messages)
    assert all('role' in x.keys() for x in messages)
    assert all('content' in x.keys() for x in messages)
    assert all(isinstance(x['role'], str) for x in messages)
    assert all(isinstance(x['content'], str) for x in messages)
    assert all(x['role'] in ('system', 'user', 'assistant') for x in messages)


def retry_ratelimit(func: callable,
                    exception: Exception,
                    retry_interval: int = 15):
    '''
    a decorator to retry the function call when exception occurs.

    OpenAI API doc provides some other methods to retry:
    https://platform.openai.com/docs/guides/rate-limits/error-mitigation
    '''

    @ft.wraps(func)
    def wrapper(*args, **kwargs):
        while True:
            try:
                result = func(*args, **kwargs)
                break
            except exception as e:
                console.log(
                    f'Rate limit reached. Will retry after {retry_interval} seconds.'
                )
                time.sleep(15)
        return result

    return wrapper


class AbstractFrontend():
    '''
    The frontend instance holds the whole chat session. The context is the whole
    session for the next LLM query. Historical chats is also a part of the
    context for following up questions. You may feel LLMs smart when they
    get information from the historical chat in the same session.
    '''

    NAME = 'AbstractFrontend'

    def __init__(self, args):
        self.uuid = uuid.uuid4()
        self.session = []
        self.debgpt_home = args.debgpt_home
        self.monochrome = args.monochrome
        self.render_markdown = args.render_markdown
        if args.subparser_name not in ('genconfig', 'genconf', 'config.toml'):
            # in order to avoid including the frontend and UUID into the
            # configuration file.
            console.log(f'{self.NAME}> Starting conversation {self.uuid}')

    def reset(self):
        '''
        clear the context. No need to change UUID I think.
        '''
        self.session = []

    def oneshot(self, message: str) -> str:
        '''
        Generate response text from the given question, without history.
        And do not print anything. Just return the response text silently.

        Args:
            message: a string, the question.
        Returns:
            a string, the response text.
        '''
        raise NotImplementedError('please override AbstractFrontend.oneshot()')

    def query(self, messages: List[Dict]) -> str:
        '''
        Generate response text from the given chat history. This function
        will also handle printing and rendering.

        Args:
            messages: a list of dict, each dict contains a message.
        Returns:
            a string, the response text.
        the messages format can be found in _check(...) function above.
        '''
        raise NotImplementedError('please override AbstractFrontend.query()')

    def update_session(self, messages: Union[List, Dict, str]) -> None:
        if isinstance(messages, list):
            # reset the chat with provided message list
            self.session = messages
        elif isinstance(messages, dict):
            # just append a new dict
            self.session.append(messages)
        elif isinstance(messages, str):
            # just append a new user dict
            self.session.append({'role': 'user', 'content': messages})
        else:
            raise TypeError(type(messages))
        _check(self.session)

    def __call__(self, *args, **kwargs):
        return self.query(*args, **kwargs)

    def dump(self):
        fpath = os.path.join(self.debgpt_home, str(self.uuid) + '.json')
        with open(fpath, 'wt') as f:
            json.dump(self.session, f, indent=2)
        console.log(f'{self.NAME}> Conversation saved at {fpath}')


class OpenAIFrontend(AbstractFrontend):
    '''
    https://platform.openai.com/docs/quickstart?context=python
    '''
    NAME: str = 'OpenAIFrontend'
    debug: bool = False
    stream: bool = True
    system_message: str = defaults.OPENAI_SYSTEM_MESSAGE

    def __init__(self, args):
        super().__init__(args)
        try:
            from openai import OpenAI
        except ImportError:
            console.log('please install OpenAI package: "pip install openai"')
            exit(1)
        self.client = OpenAI(api_key=args.openai_api_key,
                             base_url=args.openai_base_url)
        self.session.append({"role": "system", "content": self.system_message})
        self.model = args.openai_model
        self.kwargs = {'temperature': args.temperature, 'top_p': args.top_p}
        if args.verbose:
            console.log(f'{self.NAME}> model={repr(self.model)}, ' +
                        f'temperature={args.temperature}, top_p={args.top_p}.')

    def oneshot(self, message: str) -> str:

        def _func() -> str:
            _callable = self.client.chat.completions.create
            completions = _callable(model=self.model,
                                    messages=[{
                                        "role": "user",
                                        "content": message
                                    }],
                                    **self.kwargs)
            return completions.choices[0].message.content

        from openai import RateLimitError
        return retry_ratelimit(_func, RateLimitError)()

    def query(self, messages: Union[List, Dict, str]) -> list:
        # add the message into the session
        self.update_session(messages)
        if self.debug:
            console.log('send:', self.session[-1])
        completion = self.client.chat.completions.create(model=self.model,
                                                         messages=self.session,
                                                         stream=self.stream,
                                                         **self.kwargs)
        if self.stream:
            chunks = []
            if self.render_markdown:
                with Live(Markdown('')) as live:
                    for chunk in completion:
                        if chunk.choices[0].delta.content is None:
                            continue
                        piece = chunk.choices[0].delta.content
                        chunks.append(piece)
                        live.update(Markdown(''.join(chunks)), refresh=True)
            else:
                for chunk in completion:
                    if chunk.choices[0].delta.content is None:
                        continue
                    piece = chunk.choices[0].delta.content
                    chunks.append(piece)
                    print(piece, end="", flush=True)
            generated_text = ''.join(chunks)
            if not generated_text.endswith('\n'):
                print()
                sys.stdout.flush()
        else:
            generated_text = completion.choices[0].message.content
            if self.render_markdown:
                console.print(Markdown(generated_text))
            else:
                console.print(escape(generated_text))
        new_message = {'role': 'assistant', 'content': generated_text}
        self.update_session(new_message)
        if self.debug:
            console.log('recv:', self.session[-1])
        return self.session[-1]['content']


class AnthropicFrontend(AbstractFrontend):
    '''
    https://docs.anthropic.com/en/api/getting-started
    But we are currently using OpenAI API.

    The max_token limit for each model can be found here:
    https://docs.anthropic.com/en/docs/about-claude/models
    '''
    NAME = 'AnthropicFrontend'
    debug: bool = False
    stream: bool = True
    max_tokens: int = 4096

    def __init__(self, args):
        super().__init__(args)
        try:
            from anthropic import Anthropic
        except ImportError:
            console.log(
                'please install Anthropic package: "pip install anthropic"')
            exit(1)
        self.client = Anthropic(api_key=args.anthropic_api_key,
                                base_url=args.anthropic_base_url)
        self.model = args.anthropic_model
        self.kwargs = {'temperature': args.temperature, 'top_p': args.top_p}
        if args.verbose:
            console.log(f'{self.NAME}> model={repr(self.model)}, ' +
                        f'temperature={args.temperature}, top_p={args.top_p}.')

    def oneshot(self, message: str) -> str:

        def _func():
            _callable = self.client.messages.create
            completion = _callable(model=self.model,
                                   messages=[{
                                       "role": "user",
                                       "content": message
                                   }],
                                   max_tokens=self.max_tokens,
                                   **self.kwargs)
            return completion.content[0].text

        from anthropic import RateLimitError
        return retry_ratelimit(_func, RateLimitError)()

    def query(self, messages: Union[List, Dict, str]) -> list:
        # add the message into the session
        self.update_session(messages)
        if self.debug:
            console.log('send:', self.session[-1])
        if self.stream:
            chunks = []
            with self.client.messages.stream(model=self.model,
                                             messages=self.session,
                                             max_tokens=self.max_tokens,
                                             **self.kwargs) as stream:
                if self.render_markdown:
                    with Live(Markdown('')) as live:
                        for chunk in stream.text_stream:
                            chunks.append(chunk)
                            live.update(Markdown(''.join(chunks)),
                                        refresh=True)
                else:
                    for chunk in stream.text_stream:
                        chunks.append(chunk)
                        print(chunk, end="", flush=True)
            generated_text = ''.join(chunks)
            if not generated_text.endswith('\n'):
                print()
                sys.stdout.flush()
        else:
            completion = self.client.messages.create(
                model=self.model,
                messages=self.session,
                max_tokens=self.max_tokens,
                stream=self.stream,
                **self.kwargs)
            generated_text = completion.content[0].text
            if self.render_markdown:
                console.print(Markdown(generated_text))
            else:
                console.print(escape(generated_text))
        new_message = {'role': 'assistant', 'content': generated_text}
        self.update_session(new_message)
        if self.debug:
            console.log('recv:', self.session[-1])
        return self.session[-1]['content']


class GeminiFrontend(AbstractFrontend):
    '''
    https://ai.google.dev/gemini-api/docs
    '''
    NAME = 'GeminiFrontend'
    debug: bool = False
    stream: bool = True

    def __init__(self, args):
        super().__init__(args)
        try:
            import google.generativeai as genai
        except ImportError:
            console.log(
                'please install gemini package: "pip install google-generativeai"'
            )
            exit(1)
        genai.configure(api_key=args.gemini_api_key)
        self.client = genai.GenerativeModel(args.gemini_model)
        self.chat = self.client.start_chat()
        self.kwargs = genai.types.GenerationConfig(
            temperature=args.temperature, top_p=args.top_p)
        if args.verbose:
            console.log(f'{self.NAME}> model={repr(args.gemini_model)}, ' +
                        f'temperature={args.temperature}, top_p={args.top_p}.')

    def oneshot(self, message: str, *, retry: bool = True) -> str:

        def _func():
            _callable = self.client.generate_content
            result = _callable(message, generation_config=self.kwargs)
            return result.text

        from google.api_core.exceptions import ResourceExhausted
        return retry_ratelimit(_func, ResourceExhausted)()

    def query(self, messages: Union[List, Dict, str]) -> list:
        # add the message into the session
        self.update_session(messages)
        if self.debug:
            console.log('send:', self.session[-1])
        if self.stream:
            chunks = []
            response = self.chat.send_message(self.session[-1]['content'],
                                              stream=True,
                                              generation_config=self.kwargs)
            if self.render_markdown:
                with Live(Markdown('')) as live:
                    for chunk in response:
                        chunks.append(chunk.text)
                        live.update(Markdown(''.join(chunks)), refresh=True)
            else:
                for chunk in response:
                    chunks.append(chunk.text)
                    print(chunk.text, end="", flush=True)
            generated_text = ''.join(chunks)
        else:
            response = self.chat.send_message(self.session[-1]['content'],
                                              generation_config=self.kwargs)
            generated_text = response.text
            if self.render_markdown:
                console.print(Markdown(generated_text))
            else:
                console.print(escape(generated_text))
        new_message = {'role': 'assistant', 'content': generated_text}
        self.update_session(new_message)
        if self.debug:
            console.log('recv:', self.session[-1])
        return self.session[-1]['content']


class LlamafileFrontend(OpenAIFrontend):
    '''
    https://github.com/Mozilla-Ocho/llamafile
    '''
    NAME = 'LlamafileFrontend'

    def __init__(self, args):
        AbstractFrontend.__init__(self, args)
        from openai import OpenAI
        self.client = OpenAI(api_key='no-key-required',
                             base_url=args.llamafile_base_url)
        self.session.append({"role": "system", "content": self.system_message})
        self.model = 'llamafile from https://github.com/Mozilla-Ocho/llamafile'
        self.kwargs = {'temperature': args.temperature, 'top_p': args.top_p}
        if args.verbose:
            console.log(f'{self.NAME}> model={repr(self.model)}, ' +
                        f'temperature={args.temperature}, top_p={args.top_p}.')


class OllamaFrontend(OpenAIFrontend):
    '''
    https://github.com/ollama/ollama
    '''
    NAME = 'OllamaFrontend'

    def __init__(self, args):
        AbstractFrontend.__init__(self, args)
        from openai import OpenAI
        self.client = OpenAI(api_key='no-key-required',
                             base_url=args.ollama_base_url)
        self.session.append({"role": "system", "content": self.system_message})
        self.model = args.ollama_model
        self.kwargs = {'temperature': args.temperature, 'top_p': args.top_p}
        if args.verbose:
            console.log(f'{self.NAME}> model={repr(self.model)}, ' +
                        f'temperature={args.temperature}, top_p={args.top_p}.')


class vLLMFrontend(OpenAIFrontend):
    '''
    https://docs.vllm.ai/en/stable/serving/openai_compatible_server.html
    '''
    NAME = 'vLLMFrontend'

    def __init__(self, args):
        AbstractFrontend.__init__(self, args)
        from openai import OpenAI
        self.client = OpenAI(api_key='your-vllm-api-key',
                             base_url=args.vllm_base_url)
        self.session.append({"role": "system", "content": self.system_message})
        self.model = args.vllm_model
        self.kwargs = {'temperature': args.temperature, 'top_p': args.top_p}
        if args.verbose:
            console.log(f'{self.NAME}> model={repr(self.model)}, ' +
                        f'temperature={args.temperature}, top_p={args.top_p}.')


class ZMQFrontend(AbstractFrontend):
    '''
    ZMQ frontend communicates with a self-hosted ZMQ backend.
    '''
    NAME = 'ZMQFrontend'
    debug: bool = False
    stream: bool = False

    def __init__(self, args):
        import zmq
        super().__init__(args)
        self.zmq_backend = args.zmq_backend
        self.socket = zmq.Context().socket(zmq.REQ)
        self.socket.connect(self.zmq_backend)
        console.log(
            f'{self.NAME}> Connected to ZMQ backend {self.zmq_backend}.')
        #
        if hasattr(args, 'temperature'):
            console.log(
                'warning! --temperature not yet supported for this frontend')
        if hasattr(args, 'top_p'):
            console.log('warning! --top_p not yet supported for this frontend')

    def query(self, content: Union[List, Dict, str]) -> list:
        if isinstance(content, list):
            self.session = content
        elif isinstance(content, dict):
            self.session.append(content)
        elif isinstance(content, str):
            self.session.append({'role': 'user', 'content': content})
        _check(self.session)
        msg_json = json.dumps(self.session)
        if self.debug:
            console.log('send:', msg_json)
        self.socket.send_string(msg_json)
        msg = self.socket.recv()
        self.session = json.loads(msg)
        _check(self.session)
        if self.debug:
            console.log('recv:', self.session[-1])
        return self.session[-1]['content']


def create_frontend(args):
    if args.frontend == 'zmq':
        frontend = ZMQFrontend(args)
    elif args.frontend == 'openai':
        frontend = OpenAIFrontend(args)
    elif args.frontend == 'anthropic':
        frontend = AnthropicFrontend(args)
    elif args.frontend == 'gemini':
        frontend = GeminiFrontend(args)
    elif args.frontend == 'llamafile':
        frontend = LlamafileFrontend(args)
    elif args.frontend == 'ollama':
        frontend = OllamaFrontend(args)
    elif args.frontend == 'vllm':
        frontend = vLLMFrontend(args)
    elif args.frontend == 'dryrun':
        frontend = None
    else:
        raise NotImplementedError
    return frontend


def query_once(f: AbstractFrontend, text: str) -> None:
    '''
    we have prepared text -- let frontend send it to LLM, and this function
    will print the LLM reply.

    f: any frontend instance from the current source file.
    text: the text to be sent to LLM.
    '''
    if f.stream:
        end = '' if not f.render_markdown else '\n'
        if f.monochrome:
            lprompt = escape(f'LLM[{1+len(f.session)}]> ')
            console.print(lprompt, end=end, highlight=False, markup=False)
        else:
            lprompt = f'[bold green]LLM[{1+len(f.session)}]>[/bold green] '
            console.print(lprompt, end=end)
        _ = f(text)
    else:
        with Status('LLM', spinner='line'):
            _ = f(text)


if __name__ == '__main__':
    ag = argparse.ArgumentParser()
    ag.add_argument('--zmq_backend', '-B', default='tcp://localhost:11177')
    ag.add_argument('--frontend',
                    '-F',
                    default='zmq',
                    choices=('dryrun', 'zmq', 'openai', 'anthropic', 'gemini',
                             'llamafile', 'ollama', 'vllm'))
    ag.add_argument('--debgpt_home', default=os.path.expanduser('~/.debgpt'))
    ag = ag.parse_args()
    console.print(ag)

    frontend = create_frontend(ag)
    f = frontend
    import IPython
    IPython.embed(colors='neutral')
