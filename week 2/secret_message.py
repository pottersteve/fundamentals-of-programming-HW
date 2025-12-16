#secret_message = "l[A0IM'eneXtP bm7eF qo|n. ~tShTeE db rJiwd=g,e0 Ga t* !1Z9]:70i0^.9&}"
decoded_message = ""

#Version 1
#for char in range(5, len(secret_message)-3, 2):
#    if char < len(secret_message):
#        decoded_message = f"{decoded_message}{secret_message[char]}"


#Version 2
decoded_message = secret_message[5:][:-3]
decoded_message = decoded_message[::2]

print(decoded_message)