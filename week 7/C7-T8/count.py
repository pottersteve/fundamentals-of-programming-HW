def count(path):
    file = open(path, 'r')
    input = file.read()

    #characters = 0
    #words = 1

    characters = len(input)
    words = len(input.split())

    #for i in range(len(input)):
    #   if input[i] != ' ':
    #        characters += 1
    #    else:
    #        words +=1
    #        characters += 1

    return [characters, words]