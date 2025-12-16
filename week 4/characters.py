print("Enter a string: ")
text = input()

print(f"All characters in the string \"{text}\" are:")
for i in range(len(text)):
    print(text[i])