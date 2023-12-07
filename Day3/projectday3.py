print("Welcome to Treasure Island!!")


print('''
                 _
                ;`',
                `,  `,
                 ',   ;   ,,-""==..,
                  \    ','          ),
          ,-""'-., ;    '    __.-="-.;
        ," ,,_    "V      _."
       ;,'   ''-,          "=--,_
              ,-''    _  _       `,
             /   ,.-+(_)(_)�--.,   ;
            ,'  /   ; (_)       `\ ,
            ; ,/    ;._.;         ;
            !,'     ;   ;
            V'      ;   ;
                    ;._.;
                    ;   ;
                    ;   ;        ~
     ~              ;._.;
               ~    ;   ;
                   .�   `.                ~
             __,.--;.___.;--.,___
       _,,-""      ;     ;       ""-,,_
   .-��            ;     ;             ``-.
  ",              �       `               ,"        ~
    "-_                                _-"
~       ``----..,_          __,,..bmw-�
                  ```'"'"''���                  ~
                              ~
             ~''')


print("Your mission is to find the treasure.")


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
/______/______/______/______/______/______/______/______/______/______/______/_
*******************************************************************************''')


direction = input("You're at a cross road. Where do you want to go? Type \"Left\" or \"Right\" \n")
direction_case = direction.lower()
if direction_case == "left":
    swim_or_wait = input("You came to a lake. There is an island in the middle of the lake. Type \"Wait\" to wait for a boat. Type \"Swim\" to swim across. \n")
    swim_or_wait_case = swim_or_wait.lower()
    if swim_or_wait_case == "wait":
        doors = input("You arrived at the island unharmed. There is a house with 3 doors. One red, one yellow and one blue. Which colour do you choose?\n")
        doors_case = doors.lower()
        if doors_case == "yellow":
            print("BRAVO!! \n You found the treasure!!")
        elif doors_case == "red":
            print("GAME OVER. \n You got burned by fire.")
        elif doors_case == "blue":
            print("GAME OVER. \n You got munched by the beasts.")
        else:
            print("GAME OVER. \n W A S T E D")
    else:
        print("GAME OVER. \n You got attacked by an angry trout.")
else:
    print("GAME OVER. \n You fell into a hole.")