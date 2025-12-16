word = input("Enter a word: ")

bannerUp = "*"
bannerDown = "*"

for i in range(len(word)+3):
    bannerUp = f"{bannerUp}*"
print(bannerUp)

print('*', word, '*')

for i in range(len(word)+3):
    bannerDown = f"{bannerDown}*"
print(bannerDown)