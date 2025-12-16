def longest_word(path):
    file = open(path, 'r')
    words = file.read().split()
    longest = ''
    for word in words:
        if len(word) > len(longest):
            longest = word

    return longest