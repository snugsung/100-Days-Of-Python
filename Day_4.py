import random

computer_score = 0
player_score = 0

computer_choice = random.randint(0, 2)
player_choice = int(input("What do you choose?\nType 0 for Rock, 1 for Paper, or 2 for Scissors: "))

if player_choice == 0:
    player_choice = "Rock"
elif player_choice == 1:
    player_choice = "Paper"
elif player_choice == 2:
    player_choice = "Scissors"
else:
    print("Please choose a valid option.")

if computer_choice == 0:
    computer_choice = "Rock"
elif computer_choice == 1:
    computer_choice = "Paper"
elif computer_choice == 2:
    computer_choice = "Scissors"
else:
    print("Please choose a valid option.")

if player_choice == "Rock" and computer_choice == "Paper":
    print(f"\nPlayer loses! Player chose {player_choice} and Computer chose {computer_choice}.\n")
elif player_choice == "Rock" and computer_choice == "Scissors":
    print(f"\nPlayer wins! Player chose {player_choice} and Computer chose {computer_choice}.\n")
elif player_choice == "Rock" and computer_choice == "Rock":
    print(f"\nIt's a draw! Player chose {player_choice} and Computer chose {computer_choice}.\n")
elif player_choice == "Paper" and computer_choice == "Scissors":
    print(f"\nPlayer loses! Player chose {player_choice} and Computer chose {computer_choice}.\n")
elif player_choice == "Paper" and computer_choice == "Rock":
   print(f"\nPlayer wins! Player chose {player_choice} and Computer chose {computer_choice}.\n")
elif player_choice == "Paper" and computer_choice == "Paper":
     print(f"\nIt's a draw! Player chose {player_choice} and Computer chose {computer_choice}.\n")
elif player_choice == "Scissors" and computer_choice == "Rock":
    print(f"\nPlayer loses! Player chose {player_choice} and Computer chose {computer_choice}.\n")
elif player_choice == "Scissors" and computer_choice == "Paper":
    print(f"\nPlayer wins! Player chose {player_choice} and Computer chose {computer_choice}.\n")
elif player_choice == "Scissors" and computer_choice == "Scissors":
    print(f"\nIt's a draw! Player chose {player_choice} and Computer chose {computer_choice}.\n")   
