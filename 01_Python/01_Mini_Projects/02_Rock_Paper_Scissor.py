import random
item_list = ["rock","paper","scissor"]
user_choice =input("Enter your choice: ")
system_choice = random.choice(item_list)

print(f'user choice = {user_choice}, system choice = {system_choice}')

if user_choice == system_choice:
    print("both chooses same: it's a draw")
elif user_choice == "rock":
    if system_choice == "paper":
        print("paper covers rock = computer win")
    else:
        print("rock smashes scissor = you win")

elif user_choice == "paper":
    if system_choice == "scissor":
        print("scissor cuts paper : computer win")
    else:
        print("paper covers rock: you win")
elif user_choice == "scissor":
    if system_choice == "paper":
        print("scissors cuts paper = user win")
    else:
        print("Rock smashes scissor = computer win")