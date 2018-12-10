#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Crossword Solver Program"""

__author__ = "???"

# YOUR HELPER FUNCTION GOES HERE
import re


def main():
    with open('dictionary.txt') as f:
        words = f.read().split()

    w_pattern = r'[a-z]'
    test_word = raw_input(
        'Please enter a word to solve.\nUse spaces to signify unknown letters:'
        ).lower()
    w_replace = test_word.replace(' ', w_pattern)

    for w in words:
        if re.search(w_replace, w):
            if len(test_word) == len(w):
                print w


if __name__ == '__main__':
    main()
