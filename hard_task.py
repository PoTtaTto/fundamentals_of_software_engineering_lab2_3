if __name__ == '__main__':
    word1, word2 = [input(f'Enter word{i+1}: ') for i in range(2)]
    result = ''
    for letter in word1:
        if letter not in word2:
            result += letter
    for letter in word2:
        if letter not in word1:
            result += letter
    print(result)
