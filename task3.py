#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys


if __name__ == '__main__':
    string = input('Enter sentence: ')
    needed_length = int(input('Enter length: '))

    if len(string) >= needed_length:
        print('Input length must be greater than length of sentence!', file=sys.stderr)
        exit(1)

    words = string.split()

    if len(string.split()) < 2:
        print('Sentence must contain at least several words!', file=sys.stderr)
        exit(1)

    # Calculate the difference in length needed to reach the desired length
    delta = needed_length - sum([len(word) for word in words])

    # Calculate the width and remainder for distributing the extra spaces
    w, r = delta // (len(words) - 1), delta % (len(words) - 1)

    lst = []

    for i, word in enumerate(words):
        lst.append(word)
        if i < len(words) - 1:
            width = w
            if r > 0:
                width += 1
                r -= 1
            if width > 0:
                lst.append(' ' * width)

    print(''.join(lst))
