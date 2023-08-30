import random
list=['stone','paper','ciesor']
print("Your choices",list)
l=random.choice(list)
print("Enter Any one")
In=input()
if(In==l):
    print(f'you win our choice is {In} and Random is {l}')
else:
    print(f'you loss our choice is {In} and Random is {l}')
