def reverse(path):
    fileRead = open(path, "r")
    lines = fileRead.readlines()
    reversed_lines= ''

    for line in lines:
        reversed_lines = line[::-1]

    fileWrite = open(path, "w")
    fileWrite.writelines(reversed_lines)