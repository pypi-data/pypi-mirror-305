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
# suppress all warnings.
import textwrap
import rich
import shlex
from .task import task_backend, task_git, task_git_commit, task_replay
from . import defaults
from . import debian
from . import frontend
import sys
import os
import re
import argparse
import concurrent.futures
from prompt_toolkit.completion import Completer, Completion
from prompt_toolkit import PromptSession
from rich.panel import Panel
from rich.markup import escape
from rich.progress import track
from prompt_toolkit.styles import Style
from typing import List, Optional
import warnings

warnings.filterwarnings("ignore")

console = rich.get_console()


def version() -> None:
    from debgpt import __version__, __copyright__, __license__
    console.print(
        f'DebGPT {__version__}; Copyright {__copyright__}; Released under {__license__} license.'
    )


def generate_config_file(ag) -> None:
    '''
    special task: generate config template, print and quit
    '''
    console.print(ag.config_template)
    exit(0)


def fresh_install_guide(ag) -> None:
    '''
    special task: print fresh install guide, then quit
    '''
    __doc__ = '''\
DebGPT Fresh Install Guide
==========================

To use DebGPT, you need to configure a frontend to connect to the LLM backend.
There are several frontends available, including:

   (DEFAULT, commercial, proprietary, need-api-key, OpenAI-API)
 * `openai`: a frontend that connects to the OpenAI API. You need to obtain an
   API key from https://platform.openai.com/api-keys and set it in the
   `--openai_api_key` argument or the `OPENAI_API_KEY` environment variable.
   Note, this is a commercial proprietary service that needs to be paied for.

   (commercial, proprietary, need-api-key, Anthropic-API)
 * `anthropic`: Connects with Anthropic service. You need to specify
   `--anthropic_api_key` or environt variable `ANTHROPIC_API_KEY` to use this.

   (commercial, proprietary, need-api-key, Google-API)
 * `gemini`: Connects with Google's Gemini service. You need to specify
   `--gemini_api_key` to use this.

   (self-hosted, open-source, OpenAI-API)
 * `llamafile`: a frontend that connects to the llamafile JSON API service.
   Please read the instructions at https://github.com/Mozilla-Ocho/llamafile
   to setup the self-hosted llamafile service.

   (self-hosted, open-source, OpenAI-API)
 * `ollama`: a frontend that connects to the Ollama JSON API service.
   Please read the instructions at https://ollama.com/ to setup the
   self-hosted Ollama service.

   (self-hosted, open-source, need-api-key, OpenAI-API)
 * `vllm`: a frontend that connects to a vLLM service instance.
   See https://docs.vllm.ai/en/latest/ for more information.
   This is a OpenAI-API compatible self-hosted service. You need an API key
   that matches to the one used in the vLLM service.

   (self-hosted, open-source, transformers, debugging)
 * `zmq`: a frontend that connects to a self-hosted LLM inference server.
   This pairs with the self-contained primitive backend implementation
   of debgpt, which is directly based on `transformers`.

   (debugging)
 * `dryrun`: a fake frontend that will do nothing other than printing the
   generated prompt. This is only useful for debugging.

The frontend is specified by the `-F|--frontend` argument. For convenience,
you can also specify the frontend in the `~/.debgpt/config.toml` file.

You may use the following command to generate a template `config.toml` file:

 $ debgpt genconfig > ~/.debgpt/config.toml

The important flags for each of the frontends are provided in the template.

Enjoy DebGPT!'''
    console.print(__doc__)
    exit(0)


def parse_args(argv):
    '''
    argparse with subparsers. Generate a config.toml template as byproduct.
    '''

    # helper functions
    def __add_arg_to_config(template,
                            parser,
                            argname,
                            formatter: callable = repr):
        '''
        We will create a template for the config.toml file, based on the
        help messages of the argument parser. In that sense I do not have
        to write everything twice, and this avoids many human errors.
        '''
        template += '\n'.join('# ' + x for x in textwrap.wrap(
            parser._option_string_actions['--' + argname].help))
        template += f'''\n{argname} = {formatter(getattr(conf, argname))}\n'''
        return template

    # if ~/.debgpt/config.toml exists, parse it to override the built-in defaults.
    _verbose = any(x in argv for x in ('-v', '--verbose'))
    conf = defaults.Config(verbose=_verbose)
    # override the loaded configurations again with command line arguments
    ag = argparse.ArgumentParser()

    # CLI Behavior / Frontend Arguments
    config_template = '''\
##############################
# Command Line Interface Behavior
##############################
\n'''
    _g = ag.add_argument_group('Command Line Interface Behavior')
    _g.add_argument('--quit',
                    '-Q',
                    action='store_true',
                    help='directly quit after receiving the first response \
from LLM, instead of staying in interation.')
    _g.add_argument('--multiline',
                    '-M',
                    action='store_true',
                    help='enable multi-line input for prompt_toolkit. \
use Meta+Enter to accept the input instead.')
    _g.add_argument(
        '--hide_first',
        '-H',
        action='store_true',
        help='hide the first (generated) prompt; do not print argparse results'
    )
    _g.add_argument('--verbose',
                    '-v',
                    action='store_true',
                    help='verbose mode. helpful for debugging')
    _g.add_argument('--output',
                    '-o',
                    type=str,
                    default=None,
                    help='write the last LLM message to specified file')
    _g.add_argument('--version',
                    action='store_true',
                    help='show DebGPT software version and quit.')
    _g.add_argument('--debgpt_home',
                    type=str,
                    default=conf['debgpt_home'],
                    help='directory to store cache and sessions.')
    _g.add_argument(
        '--frontend',
        '-F',
        type=str,
        default=conf['frontend'],
        choices=(
            'dryrun',
            # commercial services
            'openai',
            'anthropic',
            'gemini',
            # self-hosted services
            'llamafile',
            'ollama',
            'vllm',
            'zmq'),
        help=f"default frontend is {conf['frontend']}. Available \
choices are: (dryrun, zmq, openai, anthropic, gemini, zmq, llamafile, ollama, vllm).\
The 'dryrun' is a fake frontend that will \
do nothing other than printing the generated prompt. So that you can copy \
it to web-based LLMs in that case.")
    config_template = __add_arg_to_config(config_template, ag, 'frontend')

    _g.add_argument('--monochrome',
                    type=bool,
                    default=conf['monochrome'],
                    help='disable colorized output for prompt_toolkit.')
    config_template = __add_arg_to_config(config_template,
                                          _g,
                                          'monochrome',
                                          formatter=lambda x: str(x).lower())
    _g.add_argument('--render_markdown',
                    '--render',
                    action='store_true',
                    default=conf['render_markdown'],
                    help='render the LLM output as markdown with rich.')
    config_template = __add_arg_to_config(config_template,
                                          _g,
                                          'render_markdown',
                                          formatter=lambda x: str(x).lower())

    # LLM Inference Arguments
    config_template += '''\n
###########################
# Common Frontend Arguments
###########################
\n'''
    _g = ag.add_argument_group('Common Frontend Arguments')
    _g.add_argument(
        '--temperature',
        '-T',
        type=float,
        default=conf['temperature'],
        help='''Sampling temperature. Typically ranges within [0,1]. \
Low values like 0.2 gives more focused (coherent) answer. \
High values like 0.8 gives a more random (creative) answer. \
Not suggested to combine this with with --top_p. See \
https://platform.openai.com/docs/api-reference/ \
    ''')
    config_template = __add_arg_to_config(config_template, _g, 'temperature')

    _g.add_argument('--top_p',
                    '-P',
                    type=float,
                    default=conf['top_p'],
                    help='Top-p (nucleus) sampling.')
    config_template = __add_arg_to_config(config_template, _g, 'top_p')

    # Specific to OpenAI Frontend
    config_template += '''\n
#############################
# Specific to OpenAI Frontend
#############################
\n'''
    _g = ag.add_argument_group('OpenAI Frontend Options')
    _g.add_argument('--openai_base_url',
                    type=str,
                    default=conf['openai_base_url'],
                    help='OpenAI API is a widely adopted standard. You can \
switch to other compatible service providers, or a self-hosted compatible \
server.')
    config_template = __add_arg_to_config(config_template, _g,
                                          'openai_base_url')

    _g.add_argument('--openai_api_key',
                    type=str,
                    default=conf['openai_api_key'],
                    help='API key is necessary to access services including \
OpenAI API server. https://platform.openai.com/api-keys')
    config_template = __add_arg_to_config(config_template, _g,
                                          'openai_api_key')

    _g.add_argument('--openai_model',
                    type=str,
                    default=conf['openai_model'],
                    help='For instance, gpt-3.5-turbo (4k context), \
gpt-3.5-turbo-16k (16k context), gpt-4, gpt-4-32k (32k context). \
Their prices vary. See https://platform.openai.com/docs/models .')
    config_template = __add_arg_to_config(config_template, _g, 'openai_model')

    # Specific to Anthropic Frontend
    config_template += '''\n
##################################
# Anthropic Frontend Options
##################################
\n'''
    _g = ag.add_argument_group('Anthropic Frontend Options')
    _g.add_argument('--anthropic_base_url',
                    type=str,
                    default=conf['anthropic_base_url'],
                    help='the URL to the Anthropic JSON API service.')
    config_template = __add_arg_to_config(config_template, _g,
                                          'anthropic_base_url')

    _g.add_argument('--anthropic_api_key',
                    type=str,
                    default=conf['anthropic_api_key'],
                    help='Anthropic API key')
    config_template = __add_arg_to_config(config_template, _g,
                                          'anthropic_api_key')

    _g.add_argument(
        '--anthropic_model',
        type=str,
        default=conf['anthropic_model'],
        help='the anthropic model, e.g., claude-3-5-sonnet-20241022')
    config_template = __add_arg_to_config(config_template, _g,
                                          'anthropic_model')

    # Specific to Gemini Frontend
    config_template += '''\n
#########################
# Gemini Frontend Options
#########################
\n'''
    _g = ag.add_argument_group('Gemini Frontend Options')
    _g.add_argument('--gemini_api_key',
                    type=str,
                    default=conf['gemini_api_key'],
                    help='Gemini API key')
    config_template = __add_arg_to_config(config_template, _g,
                                          'gemini_api_key')

    _g.add_argument('--gemini_model',
                    type=str,
                    default=conf['gemini_model'],
                    help='the gemini model, e.g., gemini-1.5-flash')
    config_template = __add_arg_to_config(config_template, _g, 'gemini_model')

    # Specific to Llamafile Frontend
    config_template += '''\n
############################
# Llamafile Frontend Options
############################
\n'''
    _g = ag.add_argument_group('Llamafile Frontend Options')
    _g.add_argument('--llamafile_base_url',
                    type=str,
                    default=conf['llamafile_base_url'],
                    help='the URL to the llamafile JSON API service.')
    config_template = __add_arg_to_config(config_template, _g,
                                          'llamafile_base_url')

    # Specific to Ollama Frontend
    config_template += '''\n
#########################################################
# Ollama Frontend Options (OpenAI compatibility mode)
#########################################################
\n'''
    _g = ag.add_argument_group('Ollama Frontend Options')
    _g.add_argument('--ollama_base_url',
                    type=str,
                    default=conf['ollama_base_url'],
                    help='the URL to the Ollama JSON API service.')
    config_template = __add_arg_to_config(config_template, _g,
                                          'ollama_base_url')

    _g.add_argument('--ollama_model',
                    type=str,
                    default=conf['ollama_model'],
                    help='the model to use in Ollama. For instance, llama3.2')
    config_template = __add_arg_to_config(config_template, _g, 'ollama_model')

    # Specific to vLLM Frontend
    config_template += '''\n
###########################
# vLLM Frontend Options
###########################
\n'''
    _g = ag.add_argument_group('vLLM Frontend Options')
    _g.add_argument('--vllm_base_url',
                    type=str,
                    default=conf['vllm_base_url'],
                    help='the URL to the vllm JSON API service.')
    config_template = __add_arg_to_config(config_template, _g, 'vllm_base_url')

    _g.add_argument('--vllm_api_key',
                    type=str,
                    default=conf['vllm_api_key'],
                    help='vLLM API key is necessary to access services')
    config_template = __add_arg_to_config(config_template, _g, 'vllm_api_key')

    _g.add_argument('--vllm_model',
                    type=str,
                    default=conf['vllm_model'],
                    help='the model to use in vllm. For instance, llama3.2')
    config_template = __add_arg_to_config(config_template, _g, 'vllm_model')

    # Specific to ZMQ Frontend
    config_template += '''\n
##############################
# ZMQ Frontend Options
##############################
\n'''
    _g = ag.add_argument_group('ZMQ Frontend Options')
    _g.add_argument(
        '--zmq_backend',
        type=str,
        default=conf['zmq_backend'],
        help='the ZMQ backend URL that the frontend will connect to')
    config_template = __add_arg_to_config(config_template, _g, 'zmq_backend')

    # Prompt Loaders (numbered list). You can specify them multiple times.
    # for instance, `debgpt -H -f foo.py -f bar.py`.
    config_template += '''\n
##############################
# Prompt Composer
##############################
\n'''
    # -- 1. Debian BTS
    _g = ag.add_argument_group('Prompt Composer')
    _g.add_argument(
        '--bts',
        type=str,
        default=[],
        action='append',
        help='Retrieve BTS webpage to prompt. example: "src:pytorch", "1056388"'
    )
    _g.add_argument('--bts_raw',
                    action='store_true',
                    help='load raw HTML instead of plain text.')
    # -- 2. Custom Command Line(s)
    _g.add_argument('--cmd',
                    type=str,
                    default=[],
                    action='append',
                    help='add the command line output to the prompt')
    # -- 3. Debian Buildd
    _g.add_argument('--buildd',
                    type=str,
                    default=[],
                    action='append',
                    help='Retrieve buildd page for package to prompt.')
    # -- 4. Arbitrary Plain Text File(s)
    _g.add_argument('--file',
                    '-f',
                    type=str,
                    default=[],
                    action='append',
                    help='load specified file(s) in prompt. A special syntax \
                    is supported: "--file filename:start_line:end_line"')
    # -- 5. Debian Policy
    _g.add_argument(
        '--policy',
        type=str,
        default=[],
        action='append',
        help='load specified policy section(s). (e.g., "1", "4.6")')
    # -- 6. Debian Developers References
    _g.add_argument('--devref',
                    type=str,
                    default=[],
                    action='append',
                    help='load specified devref section(s).')
    # -- 7. TLDR Manual Page
    _g.add_argument('--tldr',
                    type=str,
                    default=[],
                    action='append',
                    help='add tldr page to the prompt.')
    # -- 8. Man Page
    _g.add_argument(
        '--man',
        type=str,
        default=[],
        action='append',
        help='add man page to the prompt. Note the context length!')
    # -- 9. Arbitrary HTML document
    _g.add_argument('--html',
                    type=str,
                    default=[],
                    action='append',
                    help='load HTML document from given URL(s)')
    # -- 10. CPython What's New
    _g.add_argument(
        '--pynew',
        type=str,
        default=[],
        action='append',
        help=
        "load CPython What's New website, e.g. '3.12:summary-release-highlights'"
    )
    # -- 11. Arch Wiki
    _g.add_argument('--archw',
                    type=str,
                    default=[],
                    action='append',
                    help='load Arch Wiki. e.g., "Archiving_and_compression"')
    # -- 12. PDF File
    _g.add_argument('--pdf',
                    type=str,
                    default=[],
                    action='append',
                    help='load texts from PDF file(s)')
    # -- 998. The special query buider for mapreduce chunks
    _g.add_argument('--mapreduce',
                    '--map',
                    '-x',
                    action='append',
                    type=str,
                    help='load any file or directory for an answer')
    _g.add_argument('--mapreduce_chunksize',
                    '--map_chunksize',
                    type=int,
                    default=conf['mapreduce_chunksize'],
                    help='context chunk size for mapreduce')
    config_template = __add_arg_to_config(config_template, _g,
                                          'mapreduce_chunksize')
    _g.add_argument('--mapreduce_parallelism',
                    '--mapreduce_jobs',
                    '--map_parallelism',
                    '--map_jobs',
                    type=int,
                    default=conf['mapreduce_parallelism'],
                    help='number of parallel processes in mapreduce')
    config_template = __add_arg_to_config(config_template, _g,
                                          'mapreduce_parallelism')
    # -- 999. The Question Template at the End of Prompt
    _g.add_argument('--ask',
                    '-A',
                    '-a',
                    type=str,
                    default='',
                    help="User question to append at the end of the prompt. ")

    # Task Specific Subparsers
    subps = ag.add_subparsers(dest='subparser_name',
                              help='specific task handling')
    ag.set_defaults(func=lambda ag: None)  # if no subparser is specified

    # Specific to ZMQ Backend (self-hosted LLM Inference)
    ps_backend = subps.add_parser(
        'backend', help='start backend server (self-hosted LLM inference)')
    ps_backend.add_argument('--port',
                            '-p',
                            type=int,
                            default=11177,
                            help='port number "11177" looks like "LLM"')
    ps_backend.add_argument('--host', type=str, default='tcp://*')
    ps_backend.add_argument('--backend_impl',
                            type=str,
                            default='zmq',
                            choices=('zmq', ))
    ps_backend.add_argument('--max_new_tokens', type=int, default=512)
    ps_backend.add_argument('--llm', type=str, default='Mistral7B')
    ps_backend.add_argument('--device', type=str, default='cuda')
    ps_backend.add_argument('--precision', type=str, default='fp16')
    ps_backend.set_defaults(func=task_backend)

    # Task: git
    ps_git = subps.add_parser('git', help='git command wrapper')
    ps_git.set_defaults(func=task_git)
    git_subps = ps_git.add_subparsers(help='git commands')
    # Task: git commit
    ps_git_commit = git_subps.add_parser(
        'commit',
        aliases=['co'],
        help='directly commit staged changes with auto-generated message')
    ps_git_commit.set_defaults(func=task_git_commit)
    ps_git_commit.add_argument('--amend',
                               action='store_true',
                               help='amend the last commit')

    # Task: replay
    ps_replay = subps.add_parser('replay',
                                 help='replay a conversation from a JSON file')
    ps_replay.add_argument('json_file_path',
                           type=str,
                           nargs='?',
                           help='path to the JSON file')
    ps_replay.set_defaults(func=task_replay)

    # Task: stdin
    ps_stdin = subps.add_parser(
        'stdin',
        help='read stdin as the first prompt. Should combine with -Q.')
    ps_stdin.set_defaults(func=lambda ag: debian.stdin())

    # Task: genconfig
    ps_genconfig = subps.add_parser('genconfig',
                                    aliases=['genconf', 'config.toml'],
                                    help='generate config.toml file template')
    ps_genconfig.set_defaults(func=generate_config_file)

    # -- parse and sanitize
    ag = ag.parse_args(argv)
    ag.config_template = config_template
    return ag


def parse_args_order(argv) -> List[str]:
    '''
    parse the order of selected arguments

    We want `debgpt -f file1.txt -f file2.txt` generate different results
    than    `debgpt -f file2.txt -f file1.txt`. But the standard argparse
    will not reserve the order.

    For example, we need to match
    -f, --file, -Hf (-[^-]*f), into --file
    '''
    order: List[str] = []

    def _match_ls(probe: str, long: str, short: str, dest: List[str]):
        if any(probe == x for x in (long, short)) \
                or any(probe.startswith(x+'=') for x in (long, short)) \
                or re.match(r'-[^-]*'+short[-1], probe):
            dest.append(long.lstrip('--'))

    def _match_l(probe: str, long: str, dest: List[str]):
        if probe == long or probe.startswith(long + '='):
            dest.append(long.lstrip('--'))

    for item in argv:
        _match_l(item, '--bts', order)
        _match_l(item, '--cmd', order)
        _match_l(item, '--buildd', order)
        _match_ls(item, '--file', '-f', order)
        _match_l(item, '--policy', order)
        _match_l(item, '--devref', order)
        _match_l(item, '--tldr', order)
        _match_l(item, '--man', order)
        _match_l(item, '--html', order)
        _match_l(item, '--pynew', order)
        _match_l(item, '--archw', order)
        _match_l(item, '--pdf', order)
        _match_ls(item, '--mapreduce', '-x', order)
    return order


def mapreduce_super_long_context(ag) -> str:
    '''
    We can add a mechanism to chunk super long context , let LLM read chunk
    by chunk, providing chunk-wise analysis. Then we aggregate the chunk-wise
    analysis together using LLM again.

    Procedure:
      1. chunk a long input into pieces
      2. map each piece to LLM and get the result
      3. reduce (aggregate) the results using LLM
      4. return the aggregated LLM output
    '''
    # TODO: parse special questions like does in gather_information_ordered()
    if ag.ask:
        user_question = ag.ask
    else:
        user_question = 'summarize the above contents.'

    chunks = debian.mapreduce_load_any_astext(ag.mapreduce,
                                              ag.mapreduce_chunksize,
                                              user_question=user_question,
                                              args=ag)
    console.print(
        f'[bold]MapReduce[/bold]: Got {len(chunks)} chunks from {ag.mapreduce}'
    )
    if ag.verbose:
        for i, chunk in enumerate(chunks):
            firstline = chunk.split('\n')[:1]
            console.print(f'  [bold]Chunk {i}[/bold]: {firstline}...')

    def _shorten(s: str, maxlen: int = 100) -> str:
        return textwrap.shorten(s[::-1], width=maxlen,
                                placeholder='......')[::-1]

    def _pad_chunk(chunk: str, question: str) -> str:
        '''
        process a chunk of text with a question
        '''
        template = 'Extract any information that is relevant to question '
        template += f'{repr(question)} from the following file part. '
        template += 'Note, if there is no relevant information, just briefly say nothing.'
        template += '\n\n\n'
        template += chunk
        return template

    # skip mapreduce if there is only one chunk
    if len(chunks) == 1:
        filepath = debian.mapreduce_parse_path(ag.mapreduce,
                                               debgpt_home=ag.debgpt_home)
        if any(
                filepath.startswith(x)
                for x in ('file://', 'http://', 'https://')):
            return debian.url(filepath)
        else:
            if filepath.endswith('.pdf'):
                return debian.pdf(filepath)
            else:
                return debian.file(filepath)

    def _process_chunk(chunk: str, question: str) -> str:
        '''
        process a chunk of text with a question
        '''
        template = _pad_chunk(chunk, question)
        if ag.verbose:
            console.log('mapreduce:send:', _shorten(template, 100))
        answer = ag.frontend_instance.oneshot(template)
        if ag.verbose:
            console.log('mapreduce:recv:', _shorten(answer, 100))
        return answer

    def _pad_two_results(a: str, b: str, question: str) -> str:
        template = 'Extract any information that is relevant to question '
        template += f'{repr(question)} from the following contents and aggregate them. '
        template += 'Note, if there is no relevant information, just briefly say nothing.'
        template += '\n\n\n'
        template += '```\n' + a + '\n```\n\n'
        template += '```\n' + b + '\n```\n\n'
        return template

    def _process_two_results(a: str, b: str, question: str) -> str:
        template = _pad_two_results(a, b, question)
        if ag.verbose:
            console.log('mapreduce:send:', _shorten(template, 100))
        answer = ag.frontend_instance.oneshot(template)
        if ag.verbose:
            console.log('mapreduce:recv:', _shorten(answer, 100))
        return answer

    # start the reduce of chunks from super long context
    if ag.mapreduce_parallelism > 1:
        '''
        Parallel processing. Note, we may easily exceed the TPM limit set
        by the service provider. We will automatically retry until success.
        '''
        with concurrent.futures.ThreadPoolExecutor(
                max_workers=ag.mapreduce_parallelism) as executor:
            results = list(
                track(executor.map(lambda x: _process_chunk(x, user_question),
                                   chunks),
                      total=len(chunks),
                      description=f'MapReduce[{ag.mapreduce_parallelism}]:',
                      transient=True))
        while len(results) > 1:
            console.print(
                f'[bold]MapReduce[/bold]: reduced to {len(results)} intermediate results'
            )
            pairs = list(zip(results[::2], results[1::2]))
            with concurrent.futures.ThreadPoolExecutor(
                    max_workers=ag.mapreduce_parallelism) as executor:
                new_results = list(
                    track(
                        executor.map(
                            lambda x: _process_two_results(*x, user_question),
                            pairs),
                        total=len(pairs),
                        description=f'Mapreduce[{ag.mapreduce_parallelism}]:',
                        transient=True))
            if len(results) % 2 == 1:
                new_results.append(results[-1])
            results = new_results
        aggregated_result = results[0]
    else:
        '''
        serial processing
        '''
        # mapreduce::first pass
        results = []
        for chunk in track(chunks,
                           total=len(chunks),
                           description='MapReduce: initial pass'):
            results.append(_process_chunk(chunk, user_question))
        # mapreduce::recursive processing
        while len(results) > 1:
            console.print(
                f'[bold]MapReduce[/bold]: reduced to {len(results)} intermediate results'
            )
            new_results = []
            for (a, b) in track(zip(results[::2], results[1::2]),
                                total=len(results) // 2,
                                description='Mapreduce: intermediate pass'):
                new_results.append(_process_two_results(a, b, user_question))
            if len(results) % 2 == 1:
                new_results.append(results[-1])
            results = new_results
        aggregated_result = results[0]
    return aggregated_result + '\n\n'


def gather_information_ordered(msg: Optional[str], ag,
                               ag_order) -> Optional[str]:
    '''
    based on the argparse results, as well as the argument order, collect
    the specified information into the first prompt. If none specified,
    return None.
    '''
    __has_done_mapreduce = False

    def _append_info(msg: str, info: str) -> str:
        msg = '' if msg is None else msg
        return msg + '\n' + info

    # following the argument order, dispatch to debian.* functions with
    # different function signatures
    for key in ag_order:
        if key in ('file', 'tldr', 'man', 'buildd', 'pynew', 'archw', 'pdf'):
            spec = getattr(ag, key).pop(0)
            func = getattr(debian, key)
            msg = _append_info(msg, func(spec))
        elif key == 'cmd':
            cmd_line = ag.cmd.pop(0)
            msg = _append_info(msg, debian.command_line(cmd_line))
        elif key == 'bts':
            bts_id = ag.bts.pop(0)
            msg = _append_info(msg, debian.bts(bts_id, raw=ag.bts_raw))
        elif key == 'html':
            url = ag.html.pop(0)
            msg = _append_info(msg, debian.html(url, raw=False))
        elif key in ('policy', 'devref'):
            spec = getattr(ag, key).pop(0)
            func = getattr(debian, key)
            msg = _append_info(msg, func(spec, debgpt_home=ag.debgpt_home))
        elif key == 'mapreduce':
            # but we only do once for mapreduce
            if __has_done_mapreduce:
                continue
            msg = _append_info(msg, mapreduce_super_long_context(ag))
            __has_done_mapreduce = True
        else:
            raise NotImplementedError(key)

    # --ask should be processed as the last one
    if ag.ask:
        msg = '' if msg is None else msg
        msg += ('' if not msg else '\n') + ag.ask

    return msg


def interactive_mode(f: frontend.AbstractFrontend, ag):
    # create prompt_toolkit style
    if ag.monochrome:
        prompt_style = Style([])
    else:
        prompt_style = Style([('prompt', 'bold fg:ansibrightcyan'),
                              ('', 'bold ansiwhite')])

    # Completer with several keywords keywords to be completed
    class CustomCompleter(Completer):

        def get_completions(self, document, complete_event):
            # Get the current text before the cursor
            text_before_cursor = document.text_before_cursor

            # Check if the text starts with '/'
            if text_before_cursor.startswith('/'):
                # Define the available keywords
                keywords = ['/save', '/reset']

                # Generate completions for each keyword
                for keyword in keywords:
                    if keyword.startswith(text_before_cursor):
                        yield Completion(keyword, -len(text_before_cursor))

    # start prompt session
    prompt_session = PromptSession(style=prompt_style,
                                   multiline=ag.multiline,
                                   completer=CustomCompleter())

    # loop
    try:
        while text := prompt_session.prompt(
                f'{os.getlogin()}[{max(1, len(f.session))}]> '):
            # parse escaped interaction commands
            if text.startswith('/'):
                cmd = shlex.split(text)
                if cmd[0] == '/save':
                    # save the last LLM reply to a file
                    if len(cmd) != 2:
                        console.print('syntax error: /save <path>')
                        continue
                    path = cmd[-1]
                    with open(path, 'wt') as fp:
                        fp.write(f.session[-1]['content'])
                    console.log(f'The last LLM response is saved at {path}')
                elif cmd[0] == '/reset':
                    if len(cmd) != 1:
                        console.print('syntax error: /reset')
                        continue
                    f.reset()
                else:
                    console.print(f'unknown command: {cmd[0]}')
            else:
                frontend.query_once(f, text)
    except EOFError:
        pass
    except KeyboardInterrupt:
        pass


def main(argv=sys.argv[1:]):
    # parse args and prepare debgpt_home
    ag = parse_args(argv)
    if ag.version:
        version()
        exit(0)
    # detect first-time launch (fresh install)
    whether_show_fresh_install_guide = all([
        ag.frontend == 'openai',
        ag.openai_api_key == 'your-openai-api-key',
        ag.openai_base_url == 'https://api.openai.com/v1',
        ag.subparser_name not in ('genconfig', 'genconf', 'config.toml'),
    ])
    if whether_show_fresh_install_guide:
        fresh_install_guide(ag)
        exit(0)

    # parse argument order
    ag_order = parse_args_order(argv)
    if ag.verbose:
        console.log('Argument Order:', ag_order)

    # initialize the frontend
    f = frontend.create_frontend(ag)
    ag.frontend_instance = f

    # create task-specific prompts. note, some special tasks will exit()
    # in their subparser default function when then finished, such as backend,
    # version, etc. They will exit.
    msg = ag.func(ag)

    # gather all specified information in the initial prompt,
    # such as --file, --man, --policy, --ask
    msg = gather_information_ordered(msg, ag, ag_order)

    # in dryrun mode, we simply print the generated initial prompts
    # then the user can copy the prompt, and paste them into web-based
    # LLMs like the free web-based ChatGPT (OpenAI), claude.ai (Anthropic),
    # Bard (google), Gemini (google), huggingchat (huggingface), etc.
    if ag.frontend == 'dryrun':
        console.print(msg, markup=False)
        exit(0)

    # print the prompt and do the first query, if specified
    if msg is not None:
        if not ag.hide_first:
            console.print(Panel(escape(msg), title='Initial Prompt'))

        # query the backend
        frontend.query_once(f, msg)

    # drop the user into interactive mode if specified (-i)
    if not ag.quit:
        interactive_mode(f, ag)

    # dump session to json
    f.dump()
    if ag.output is not None:
        if os.path.exists(ag.output):
            console.print(
                f'[red]! destination {ag.output} exists. Will not overwrite this file.[/red]'
            )
        else:
            with open(ag.output, 'wt') as fp:
                fp.write(f.session[-1]['content'])


if __name__ == '__main__':
    main()
