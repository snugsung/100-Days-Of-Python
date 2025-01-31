import random

weapon_choice = ''
computer_choice = random.randint(0, 2)
player_choice = int(input("What do you choose?\nType 0 for Rock, 1 for Paper, or 2 for Scissors: "))

if player_choice == 0 and computer_choice == 1:
    print("Player loses!")
    if player_choice == 0 and computer_choice == 2:
        print("Player wins!")
    if player_choice == 0 and computer_choice == 0:
        print("It's a draw!")
    if player_choice == 1 and computer_choice == 2:
        print("Player loses!")
    if player_choice == 1 and computer_choice == 0:
        print("Player wins!")
    if player_choice == 1 and computer_choice == 1:
        print("It's a draw!")
    if player_choice == 2 and computer_choice == 0:
        print("Player loses!")
    if player_choice == 2 and computer_choice == 1:
        print("Player wins!")
    if player_choice == 2 and computer_choice == 2:
        print("It's a draw!")
    else:
        print("Please choose a valid option.")