if __name__ == '__main__':
    word = input('Enter word: ')

    result_word, letter_count = '', {}
    for letter in word:
        if letter not in letter_count:
            letter_count[letter] = 0
        letter_count[letter] += 1
        if letter_count[letter] > 1:
            continue
        result_word += letter

    print(result_word)
