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
from typing import List, Union, Dict, Tuple, Optional
import re
import requests
from . import policy as debgpt_policy
from bs4 import BeautifulSoup
import os
import subprocess
import functools as ft
import sys
import glob
import rich
import mimetypes
import tenacity
import concurrent.futures
from urllib.request import urlopen, Request
from urllib.parse import quote

console = rich.get_console()

__doc__ = '''
This file is in charge of organizaing (debian specific) functions for loading
texts from various sources, which are subsequently combined into the first
prompt, and sent through frontend to the backend for LLM to process.
'''


def is_text_file(filepath: str) -> bool:
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            f.read()
            return True
    except UnicodeDecodeError:
        return False


########################
# Utility I/O functions
########################


def _load_html(url: str) -> List[str]:
    '''
    read HTML from url, convert it into plain text, then list of lines
    '''
    r = requests.get(url)
    soup = BeautifulSoup(r.text, features="html.parser")
    text = soup.get_text().strip()
    text = re.sub('\n\n+\n', '\n\n', text)
    text = [x.rstrip() for x in text.split('\n')]
    return text


def _load_bts(identifier: str) -> List[str]:
    url = f'https://bugs.debian.org/{identifier}'
    r = requests.get(url)
    soup = BeautifulSoup(r.text, features="html.parser")

    if not identifier.startswith('src:'):
        # delete useless system messages
        _ = [
            x.clear()
            for x in soup.find_all('p', attrs={'class': 'msgreceived'})
        ]
        _ = [
            x.clear()
            for x in soup.find_all('div', attrs={'class': 'infmessage'})
        ]

    text = soup.get_text().strip()
    text = re.sub('\n\n+\n', '\n\n', text)
    text = [x.strip() for x in text.split('\n')]

    # filter out useless information from the webpage
    if identifier.startswith('src:'):
        # the lines from 'Options' to the end are useless
        text = text[:text.index('Options')]

    return text


def _load_html_raw(url: str) -> List[str]:
    '''
    read the raw HTML.
    XXX: if we do not preprocess the raw HTML, the input sequence to LLM
    will be very long. It may trigger CUDA out-of-memory in the backend
    when the length exceeds a certain value, depending on the CUDA memory
    available in the backend machine.
    '''
    r = requests.get(url)
    text = r.text.strip()
    text = re.sub('\n\n+\n', '\n\n', text)
    text = [x.strip() for x in text.split('\n')]
    return text


def _load_file(path: str) -> List[str]:
    with open(path, 'rt') as f:
        lines = [x.rstrip() for x in f.readlines()]
    return lines


def _load_cmdline(cmd: Union[str, List]) -> List[str]:
    if isinstance(cmd, str):
        cmd = cmd.split(' ')
    stdout = subprocess.check_output(cmd).decode()
    lines = [x.rstrip() for x in stdout.split('\n')]
    return lines


def _load_stdin() -> List[str]:
    lines = [x.rstrip() for x in sys.stdin.readlines()]
    return lines


def _latest_file(files: List[str]) -> str:
    '''
    return the latest file among the list of files
    '''
    latest = max(files, key=os.path.getmtime)
    return latest


def _latest_glob(pattern: str) -> str:
    '''
    return the latest file that matches the glob pattern
    '''
    return _latest_file(glob.glob(pattern))


@tenacity.retry(stop=tenacity.stop_after_attempt(3),
                wait=tenacity.wait_fixed(5))
def _load_url(url: str) -> List[str]:
    headers = {
        'User-Agent': 'Mozilla/5.0',
        'Accept':
        'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8'
    }
    req = Request(url, headers=headers)
    with urlopen(req) as response:
        try:
            content = response.read().decode('utf-8')
        except UnicodeDecodeError:
            console.log(f'Failed to read {repr(url)} as utf-8. Giving up.')
            return ['']
        lines = content.splitlines()
    lines = [x.rstrip() for x in lines]
    return lines


def _load_url_parsed(url: str) -> str:
    content = '\n'.join(_load_url(url))
    soup = BeautifulSoup(content, features="html.parser")
    text = soup.get_text().strip()
    return text.split('\n')


def _load_pdf(file_path: str) -> list[str]:
    try:
        import PyPDF2
    except ImportError:
        print("Please install PyPDF2 using 'pip install PyPDF2'")
        exit(1)
    # Open the PDF file
    with open(file_path, 'rb') as file:
        # Create a PDF reader object
        pdf_reader = PyPDF2.PdfReader(file)

        # Get the number of pages
        num_pages = len(pdf_reader.pages)

        # Initialize a string to store the text
        text = ""

        # Extract text from each page
        for page_num in range(num_pages):
            # Get the page object
            page = pdf_reader.pages[page_num]
            # Extract text from the page
            text += page.extract_text()

    return text.split('\n')


@tenacity.retry(stop=tenacity.stop_after_attempt(3),
                wait=tenacity.wait_fixed(5))
def google_search(query: str) -> List[str]:
    # Format the query for URL
    query = quote(query)

    # Send request to Google
    url = f"https://www.google.com/search?q={query}"
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) " \
                + "AppleWebKit/537.36 (KHTML, like Gecko) " \
                + "Chrome/91.0.4472.124 Safari/537.36"
    }
    response = requests.get(url, headers=headers)

    # Parse the response
    soup = BeautifulSoup(response.text, 'html.parser')

    # Find search results
    search_results = soup.find_all('div', class_='g')

    results = []
    for result in search_results:
        title = result.find('h3')
        link = result.find('a')
        if title and link:
            results.append(link.get('href'))

    return results


#####################################
# Text Loaders from Various Sources
#####################################


def url(url: str):
    '''
    directly load text contents from URL without any processing
    '''
    text = _load_url(url)
    lines = [f'Here is the contents of {url}:']
    lines.extend(['```'] + text + ['```', ''])
    return '\n'.join(lines)


def pdf(path: str) -> str:
    text = _load_pdf(path)
    lines = [f'Here is the contents of PDF file {path}:']
    lines.extend(['```'] + text + ['```', ''])
    return '\n'.join(lines)


def archw(identifier: str) -> str:
    '''
    Archwiki. e.g.,
    https://wiki.archlinux.org/title/Archiving_and_compression
    '''
    url = f'https://wiki.archlinux.org/title/{identifier}'
    r = requests.get(url)
    soup = BeautifulSoup(r.text, features='html.parser')
    text = soup.get_text().split('\n')
    lines = [f'Here is the Arch Wiki about {identifier}:']
    lines.extend(['```', *text, '```', ''])
    return '\n'.join(lines)


def html(url: str, *, raw: bool = False):
    '''
    Load a website in plain/raw text format
    '''
    text = _load_html_raw(url) if raw else _load_html(url)
    lines = [f'Here is the contents of {url}:']
    lines.extend(['```'] + text + ['```', ''])
    return '\n'.join(lines)


def buildd(p: str, *, suite: str = 'sid', raw: bool = False):
    url = f'https://buildd.debian.org/status/package.php?p={p}&suite={suite}'
    text = _load_html_raw(url) if raw else _load_html(url)
    lines = [f'The following is the build status of package {p}:']
    lines.extend(['```'] + text + ['```', ''])
    return '\n'.join(lines)


def bts(identifier: str, *, raw: bool = False):
    text = _load_bts(identifier)
    lines = ["The following is a webpage from Debian's bug tracking system:"]
    lines.extend(['```'] + text + ['```', ''])
    return '\n'.join(lines)


def policy(section: str, *, debgpt_home: str):
    '''
    the policy cache in plain text format will be stored in debgpt_home
    '''
    doc = debgpt_policy.DebianPolicy(os.path.join(debgpt_home, 'policy.txt'))
    text = doc[section].split('\n')
    lines = [f'''The following is the section {section} of Debian Policy:''']
    lines.extend(['```'] + text + ['```', ''])
    return '\n'.join(lines)


def devref(section: str, *, debgpt_home: str):
    '''
    similar to policy, the devref cache will be stored in debgpt_home
    '''
    doc = debgpt_policy.DebianDevref(os.path.join(debgpt_home, 'devref.txt'))
    text = doc[section].split('\n')
    lines = [
        f'''The following is the section {section} of Debian Developer's Reference:'''
    ]
    lines.extend(['```'] + text + ['```', ''])
    return '\n'.join(lines)


def man(name: str):
    text = _load_cmdline(f'man {name}')
    lines = [f'''The following is the manual page of {name}:''']
    lines.extend(['```'] + text + ['```', ''])
    return '\n'.join(lines)


def tldr(name: str):
    text = _load_cmdline(f'tldr {name}')
    lines = [f'''The following is the tldr of the program {name}:''']
    lines.extend(['```'] + text + ['```', ''])
    return '\n'.join(lines)


def command_line(cmd: str):
    text = _load_cmdline(cmd)
    lines = [f'''The following is the output of command line `{cmd}`:''']
    lines.extend(['```'] + text + ['```', ''])
    return '\n'.join(lines)


def stdin():
    text = _load_stdin()
    return '\n'.join(text)


def file(path: str):
    if ':' in path:
        # it is a special syntax to specify line range e.g. setup.py:1-10
        path, lrange = path.split(':')
        text = _load_file(path)
        start, end = re.match(r'^(\d*)-(\d*)', lrange).groups()
        start = int(start) if start else None
        end = int(end) if end else None
        text = text[start:end]
    else:
        text = _load_file(path)
    lines = [f'''The following is a file named {path}:''']
    lines.extend(['```'] + text + ['```', ''])
    return '\n'.join(lines)


def pynew(version_section: str):
    '''
    What's New websites of cpython
    https://docs.python.org/3/whatsnew/3.12.html#summary-release-highlights

    version: e.g. 3.12
    section: e.g. summary
    '''
    # parse inputs
    if ':' in version_section:
        # normally return the specified section
        version, section = version_section.split(':')
    else:
        # print all available sections and exit()
        version, section = version_section, None
    # retrieve webpage
    url = f'https://docs.python.org/3/whatsnew/{version}.html'
    doc = requests.get(url).text
    soup = BeautifulSoup(doc, features='html.parser')
    sections = [x.attrs['id'] for x in soup.find_all('section')]
    # extract information from webpage
    if section is None or not section:
        # if not specified section: print available ones and exit()
        console.print("Available Sections in Python What's New:", sections)
        sys.exit(0)
    else:
        # if specified section: find that section
        part = soup.find_all('section', attrs={'id': section})[0]
        text = part.get_text().strip()
    # enclose in markdown block
    lines = [
        f'''The following is the {section} section of Python {version}'s What's New document:'''
    ]
    lines.extend(['```', text, '```', ''])
    return '\n'.join(lines)


##########################################
# Special Text Loaders
##########################################
def _mapreduce_chunk_lines(path: str, start: int, end: int, lines: List[str],
                           *, chunk_size: int):
    chunk_size_in_bytes = sum(len(x.encode('utf8')) for x in lines[start:end])
    if chunk_size_in_bytes < chunk_size:
        return {(path, start, end): lines[start:end]}
    elif end - start == 1:
        return {(path, start, end): lines[start:end]}
    else:
        # split the lines into chunks
        middle = (start + end) // 2
        left = _mapreduce_chunk_lines(path,
                                      start,
                                      middle,
                                      lines,
                                      chunk_size=chunk_size)
        right = _mapreduce_chunk_lines(path,
                                       middle,
                                       end,
                                       lines,
                                       chunk_size=chunk_size)
        return {**left, **right}


def _mapreduce_chunk_lines_norecussion(path: str, start: int, end: int,
                                       lines: List[str], *, chunk_size: int):
    '''
    the non-recursion version of the above function
    the above version seems to be problematic when dealing with large files

    this function is modified from re-written of the above function with chatgpt.
    '''
    result = {}
    stack = [(start, end)]
    lens = [len(line.encode('utf8')) for line in lines]

    while stack:
        current_start, current_end = stack.pop()
        chunk_size_in_bytes = sum(lens[current_start:current_end])

        if chunk_size_in_bytes < chunk_size:
            # If the chunk is within the size limit, add to result
            result[(path, current_start,
                    current_end)] = lines[current_start:current_end]
        elif current_end - current_start == 1:
            # If the chunk is too large, but only one line, add to result
            result[(path, current_start,
                    current_end)] = lines[current_start:current_end]
        else:
            # If the chunk is too large, split it and add to stack
            middle = (current_start + current_end) // 2
            stack.append((current_start, middle))
            stack.append((middle, current_end))
        print('number of lines:', len(lines), 'stack size:', len(stack))

    return result


def mapreduce_load_url(
    url: str,
    chunk_size: int = 8192,
) -> Dict[Tuple[str, int, int], List[str]]:
    '''
    load text contents from a URL and return the chunked contents
    '''
    with urlopen(url) as response:
        content = response.read().decode('utf-8')
        lines = content.splitlines()
    lines = [x.rstrip() for x in lines]
    chunkdict = _mapreduce_chunk_lines(url,
                                       0,
                                       len(lines),
                                       lines,
                                       chunk_size=chunk_size)
    return chunkdict


def mapreduce_load_file(
    path: str,
    chunk_size: int = 8192,
) -> Dict[Tuple[str, int, int], List[str]]:
    '''
    load the file and return the content as a list of lines
    '''
    # tell the file type and load the file as lines
    mime_type, _ = mimetypes.guess_type(path)
    if mime_type == 'application/pdf':
        lines = _load_pdf(path)
    else:
        with open(path, 'rt') as f:
            lines = [x.rstrip() for x in f.readlines()]

    # chunk the lines
    try:
        chunkdict = _mapreduce_chunk_lines(path,
                                           0,
                                           len(lines),
                                           lines,
                                           chunk_size=chunk_size)
    except RecursionError:
        console.log(
            'Oops! falling back to non-recursion chunking due to RecursionError'
        )
        chunkdict = _mapreduce_chunk_lines_norecussion(path,
                                                       0,
                                                       len(lines),
                                                       lines,
                                                       chunk_size=chunk_size)
    return chunkdict


def mapreduce_load_directory(
    path: str,
    chunk_size: int = 8192,
) -> Dict[Tuple[str, int, int], List[str]]:
    '''
    load a whole directory and return the chunked contents
    '''
    all_chunks = dict()
    for root, _, files in os.walk(path):
        for file in files:
            path = os.path.join(root, file)
            if not is_text_file(path):
                continue
            chunkdict = mapreduce_load_file(path, chunk_size=chunk_size)
            all_chunks.update(chunkdict)
    return all_chunks


def mapreduce_parse_path(path: str, debgpt_home: str) -> str:
    '''
    parse the path string and return the actual path or URL.

    e.g. policy: -> <debgpt_home>/policy.txt
    '''
    if path.startswith(':'):
        if path == 'policy:':
            return os.path.join(debgpt_home, 'policy.txt')
        elif path == 'devref:':
            return os.path.join(debgpt_home, 'devref.txt')
        else:
            raise ValueError(f'Undefined special path {path}')
    elif path == 'sbuild:':
        if not os.path.exists('./debian'):
            raise FileNotFoundError(
                './debian directory not found. Are you in the right directory?'
            )
        return _latest_glob('../*.build')
    else:
        return path


def mapreduce_load_any(
    path: str,
    chunk_size: int = 8192,
    *,
    user_question: str = '',
    args: Optional[object] = None,
) -> Dict[Tuple[str, int, int], List[str]]:
    '''
    load file or directory and return the chunked contents
    '''
    if path == 'policy:':
        lines = debgpt_policy.DebianPolicy(
            os.path.join(args.debgpt_home, 'policy.txt')).lines
        return _mapreduce_chunk_lines('Debian Policy',
                                      0,
                                      len(lines),
                                      lines,
                                      chunk_size=chunk_size)

    elif path == 'devref:':
        lines = debgpt_policy.DebianDevref(
            os.path.join(args.debgpt_home, 'devref.txt')).lines
        return _mapreduce_chunk_lines('Debian Developer Reference',
                                      0,
                                      len(lines),
                                      lines,
                                      chunk_size=chunk_size)

    elif path == 'sbuild:':
        '''
        load the latest sbuild buildlog. we will automatically figure out the
        latest buildlog file in the parent directory.
        '''
        if not os.path.exists('./debian'):
            raise FileNotFoundError(
                './debian directory not found. Are you in the right directory?'
            )
        latest_build_log = _latest_glob('../*.build')
        return mapreduce_load_file(latest_build_log, chunk_size)

    elif path.startswith('google:'):
        query = path[7:] if len(path) > 7 else user_question
        urls = google_search(query)
        if args.verbose:
            console.log(f'Google Search Results for {repr(query)}:', urls)
        else:
            console.log(
                f'Got {len(urls)} Google Search Results for {repr(query)}.')
        with concurrent.futures.ThreadPoolExecutor() as executor:
            futures = {
                executor.submit(_load_url_parsed, url): url
                for url in urls
            }
            chunkdict = {}
            for future in concurrent.futures.as_completed(futures):
                url = futures[future]
                lines = future.result()
                chunkdict.update(
                    _mapreduce_chunk_lines(url,
                                           0,
                                           len(lines),
                                           lines,
                                           chunk_size=chunk_size))
        return chunkdict

    elif any(path.startswith(x) for x in ('file://', 'http://', 'https://')):
        return mapreduce_load_url(path, chunk_size=chunk_size)
    elif os.path.isdir(path):
        return mapreduce_load_directory(path, chunk_size=chunk_size)
    elif os.path.isfile(path):
        return mapreduce_load_file(path, chunk_size=chunk_size)
    else:
        raise FileNotFoundError(f'{path} not found')


def mapreduce_load_any_astext(
    path: Union[str | List[str]],
    chunk_size: int = 8192,
    *,
    user_question: str = '',
    args: Optional[object] = None,
) -> List[str]:
    '''
    load file or directory and return the contents as a list of lines
    '''
    # if list, reduce and concur recursively
    if isinstance(path, list):
        texts = [
            mapreduce_load_any_astext(p,
                                      chunk_size=chunk_size,
                                      user_question=user_question,
                                      args=args) for p in path
        ]
        texts = ft.reduce(list.__add__, texts)
        return texts
    # if str, deal with the concrete loading
    chunkdict = mapreduce_load_any(path,
                                   chunk_size=chunk_size,
                                   user_question=user_question,
                                   args=args)
    texts = []
    for (path, start, end), lines in chunkdict.items():
        txt = f'File: {path} (lines {start}-{end})\n'
        txt += '```\n'
        txt += '\n'.join(lines)
        txt += '\n```\n'
        texts.append(txt)
    return texts
