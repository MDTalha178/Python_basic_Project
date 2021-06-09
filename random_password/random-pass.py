import random

upper_char = ['A','B','C','D','E','F','G','H','I']
lower_char = ['a','b','c','d','e','f','g','i']
nums =['1','2','3','4','5','6']
special= ['!','@','#','$','%','&']

password= random.choice(upper_char)+random.choice(lower_char)+random.choice(nums)+random.choice(special)+random.choice(upper_char)+random.choice(lower_char)+random.choice(nums)+random.choice(special)
print(f"Congratulation! your password is {password}")