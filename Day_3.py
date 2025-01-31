print('''

*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_______/
*******************************************************************************
''')

print("Welcome to treasure island!\nYour mission is to find the scroll of wisdom.\nYou're at a cross road. Where do you want to go?\n")
user_choice = input('Type "left" or "right" ').capitalize()

def terminate_game():
    exit()

if user_choice == "Left":
    print('''
                                ,-.
                        _,-' - `--._
                      ,'.:  __' _..-)
                    ,'     /,o)'  ,'
                   ;.    ,'`-' _,)
                 ,'   :.   _.-','
               ,' .  .    (   /
              ; .:'     .. `-/
            ,'       ;     ,'
         _,/ .   ,      .,' ,
       ,','     .  .  . .\,'..__
     ,','  .:.      ' ,\ `\)``
     `-\_..---``````-'-.`.:`._/
     ,'   '` .` ,`- -.  ) `--..`-..
     `-...__________..-'-.._  \ 
        ``--------..`-._ ```
                     ``    
    
    You encounter a wizard who turns you into a frog. Game over
    ''')
    terminate_game()
    
elif user_choice == "Right":
    print('''
  _            _
 / \          / \ 
#"'"|'"'"'"'"|"'"|
#   |  _.._  |   |
#   |.'    `.|   |
#   |        |   |
#   |.   /~~/~~/~~/
#   | './  /  /  /
#   |  /--/--/--/|
#   | /  /  /  / |
#   |/--/--/--/  |
#   |========#   | 
    
    \nYou arrive at a castle moat.\nThe drawbridge is raised.\nHow do you cross over?\n''')

    swim_or_jump = input('Type "swim" or "jump" ').capitalize()
    if swim_or_jump == "Swim":
        print('''

         .-''-.__.-'00  '-' ' ' ' ' ' ' ' '-.
         '.___ '    .   .--_'-' '-' '-' _'-' '._
          V: V 'vv-'   '_   '.       .'  _..' '.'.
            '=.____.=_.--'   :_.__.__:_   '.   : :
                    (((____.-'        '-.  /   : :
                                      (((-'\ .' /
                                    _____..'  .'
                                   '-._____.-'   

        You were devoured by a hungry crocodile. Game over''')
        terminate_game()

    if swim_or_jump == "Jump":
        print("\nYou jump and scrape your knee on the ground but manage to get across.\nYou see three doors with three different colors.\nWhich door do you choose?\n")
        door_choice = input('Options: "Red" | "Blue" | "Yellow" | ').capitalize()
        
        if door_choice == "Red":
            print(''''
____._________________
    _|_      
    \  \ 
     \  \ 
      \  \ 
       \  \                    
        \  \                   
         \/                                     
            
            You fell into a trap door. Game over''') 
            terminate_game()
        
        if door_choice == "Blue":
            print('''

        emmmmmm~~~~~~~~~~oT
        """"""|          |
              |          |
              `----------'
            
            You find a mad butcher who turns you into mince meat. Game over''')
            terminate_game()   
        
        if door_choice == "Yellow":
            print('''
         _______________
    ()==(              (@==()
         '______________'|
           |             |
           |             |
         __)_____________|
    ()==(               (@==()
         '--------------'

            You found the legendary scroll of wisdom! You win!!!''')
            terminate_game()
else: 
    print("You did not follow instructions.\n*Bonk*\nGame over.")
    terminate_game()



