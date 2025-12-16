try:
    filename = input("Enter the source filename: \n")
    filename0 = input("Enter the destination filename: \n")
    file_source = open(filename, "r")
    contents = file_source.read()
    file_dest = open(filename0, "w")
    file_dest.write(contents)
    print("File copied successfully.")
except FileNotFoundError:
    print("Error: Source file not found.")
