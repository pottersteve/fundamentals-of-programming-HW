def read_contents(path):
    try:
        file = open(path, 'r')
        contents = file.read()
        return contents
    except FileNotFoundError:
        return None