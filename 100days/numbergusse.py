import random

easy_level=10
hard_level=5

def chk_ans(ans,guess,turns):
    if guess<ans:
        print("Too low")
        return turns-1
    elif guess>ans:
        print("Too high")
        return turns - 1
    else:
        print("You'r right")



def dif():
    level=input("Enter difficulty leve: ")
    if level=="easy":
        return easy_level
    else:
        return hard_level




def game():

    ans=random.randint(1,100)
    turns=dif()
    guess=0

    while guess!=ans:
        print(f"You have {turns} turns left")
        guess=int(input("Enter number you thinking: "))
        turns=chk_ans(ans,guess,turns)
        if turns==0:
            print("you dont have attempts left!,you lose")
        elif guess!=ans:
            print("guess again")





game()

