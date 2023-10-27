if __name__ == '__main__':
    word = input('Enter word: ')

    center_index = len(word) // 2
    if len(word) % 2 == 1:
        updated_word = word[:center_index] + word[center_index + 1:]
    else:
        updated_word = word[:center_index - 1] + word[center_index + 1:]
    print(updated_word)