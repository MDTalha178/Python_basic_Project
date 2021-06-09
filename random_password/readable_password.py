import random

wordlist = []
special= ['@','#','$','%','&']

with open("wekipidia-text.txt", "r") as file:
    data = file.readlines()
    for line in data:
        words = line.split()
    for item in words:
        if len(item)>5:
            wordlist.append(item.capitalize())
word = random.choice(wordlist)
s_char = random.choice(special)
num = str(random.randint(101,999))

password = word+s_char+num
print(f"Congratulations your password is {password}")

    