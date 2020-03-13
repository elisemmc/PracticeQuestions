#!/usr/bin/env python
"""Retrieve and print words from a URL.

Usage:

    python words.py <URL>
"""

import sys
from urllib.request import urlopen


def fetch_words(url):
    """Fetch a list of words from a URL.
    
    Args:
        url: the URL of a UTF-8 text document.

    Returns:
        A list of strings containing the words from the document.
    """
    story = urlopen(url)
    story_words = []
    for line in story:
        line_words = line.decode('utf-8').split()
        for word in line_words:
            story_words.append(word)
    story.close()
    return story_words


def print_items(items):
    """Print items one per line.
    
    Args:
        An iterable series of printable items.
    """
    for item in items:
        print(item)


def main(url):
    """Print each word from a text document at a URL.
    
    Args:
        url: the URL of a UTF-8 text document.
    """
    words = fetch_words(url)
    print_items(words)


DIGIT_MAP = {
    'zero'  : '0',
    'one'   : '1',
    'two'   : '2',
    'three' : '3',
    'four'  : '4',
    'five'  : '5',
    'six'   : '6',
    'seven' : '7',
    'eight' : '8',
    'nine'  : '9',
}


def convert(s):
    try:
        number = ''
        for token in s:
            number += DIGIT_MAP[token]
        x = int(number)
        print(f'Conversion succeeded: x = {x}')
        return x
        
    except (KeyError, TypeError) as e:
        print(f'HELLO {e!r}')
        raise


# execute if run from terminal
if __name__ == '__main__':
    # print(convert('seven one oe'.split()))
    main(sys.argv[1])