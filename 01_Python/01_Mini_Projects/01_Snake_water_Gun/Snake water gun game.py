# PROJECT 1: SNAKE, WATER, GUN GAME
# We all have played snake, water gun game in our childhood. If you haven’t, google the
# rules of this game and write a python program capable of playing this game with the
# user

"""
1 for snake
-1 for water
0 for gun
"""
import random

computer = random.choice([1,0,-1]) # random is used to choose between 1 0 -1 randomly
you_Str=input("Enter Your choice:")
you_Dic={"s":1, "w":-1,"g":0}  # it's a simple dictionary for "You"
reverse_Dic={1:"s",-1:"w",0:"g"} # we reversed the dictionary for computer's choice

you=you_Dic[you_Str]
# uptil now we have 2 number(variables),"You" and "Computer"
print(f'You chose: {reverse_Dic[you]}\nComputer Chose:{reverse_Dic[computer]}')

if(computer==you):
    print("It's a draw:")
else:
    if (computer == -1 and you == 1): #Sum = -1+1=0  or computer - you = -1-1=- 2
        print("You Win!")
    elif (computer == -1 and you == 0): #Sum = -1    or computer - you = -1-0=- 1
        print("You lose!")
    elif (computer == 1 and you == -1): #Sum = 0     or computer - you = 1-(-1)= 2
        print("You lose!")
    elif (computer == 1 and you == 0): #Sum = 1     or computer - you = 1-0= 1
        print("You Win!")
    elif (computer == 0 and you == -1): #Sum = -1     or computer - you = 0-(-1)= 1
        print("You Win!")
    elif (computer == 0 and you == 1): #Sum = 1     or computer - you = 0-1= -1
        print("You lose!")
    else:
        print("something went wrong!")


"""
from the above comment line analysis we can also write this code like this,
and it will work the same.

if(computer == you):
    print("It's a draw:")
else:
    if( ( computer - you ) == -1 or ( computer - you ) == 2):
        print("You Lose")
    else:
        print("You win")
"""