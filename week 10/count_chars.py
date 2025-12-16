def count_chars(s):
    dictionary = {}
    for char in s:
        if char in dictionary:
            dictionary[char] = dictionary[char] + 1
        else:
            dictionary[char] = 1
    return dictionary
