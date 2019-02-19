def find(word, letter):
    index = 0
    while index < len(word):
        if word[index] == 0:
            return index
        index = index + 1
    return -1

find(word, letter)
