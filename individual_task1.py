#!/usr/bin/env python3
# -*- coding: utf-8 -*-

if __name__ == '__main__':
    sentence = input('Enter sentence: ')
    [print(letter, end=' ') for letter in sentence if letter == 'и']
