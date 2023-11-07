#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys


if __name__ == '__main__':
    sentence = input('Enter sentence: ')
    if ',' in sentence:
        n_count = sentence.split(',', 1)[0].count('н')
        print('Letter "н" count before first comma:', n_count)
    else:
        print('There is no commas in sentence', file=sys.stderr)