print("Enter a string:")
text = input()
print("Enter an integer:")
p = int(input())

if p<len(text):
    result = f"{text[:p-1]}@{text[p:]}"
    print("The new string is: ", result)