#!/usr/bin/env python3
# -*- coding: utf-8 -*-

if __name__ == '__main__':
    word = input('Enter word: ')

    center_index = len(word) // 2  # Index of center element
    if len(word) % 2 == 1:
        # Removing central letter
        updated_word = word[:center_index] + word[center_index + 1:]
    else:
        # Removing two central letters
        updated_word = word[:center_index - 1] + word[center_index + 1:]
    print(updated_word)