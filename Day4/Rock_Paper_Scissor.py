#Rock wins againstr scissors
# Scissor wins against paper
# paper wins against Rock
import random
print("This is the game of stone , paper , scissor...enjoy playing it and let me know...")
users_choice = int(input("Please enter your choice ...\n 1 for stone , 2 for paper and 3 for scissor\n\n"))
print ( users_choice)

paper='''
88888b.  .d88b. 888  888  888.d8888b 88888b.  8888b. 88888b.  .d88b. 888d888 
888 "88bd8P  Y8b888  888  88888K     888 "88b    "88b888 "88bd8P  Y8b888P"   
888  88888888888888  888  888"Y8888b.888  888.d888888888  88888888888888     
888  888Y8b.    Y88b 888 d88P     X88888 d88P888  888888 d88PY8b.    888     
888  888 "Y8888  "Y8888888P"  88888P'88888P" "Y88888888888P"  "Y8888 888     
                                     888             888                     
                                     888             888                     
                                     888             888   '''
stone='''
        888                            
        888                            
        888                            
.d8888b 888888 .d88b. 88888b.  .d88b.  
88K     888   d88""88b888 "88bd8P  Y8b 
"Y8888b.888   888  888888  88888888888 
     X88Y88b. Y88..88P888  888Y8b.     
 88888P' "Y888 "Y88P" 888  888 "Y8888'''

scissor='''
               d8b                                
                Y8P                                
                                                   
.d8888b  .d8888b888.d8888b .d8888b  .d88b. 888d888 
88K     d88P"   88888K     88K     d88""88b888P"   
"Y8888b.888     888"Y8888b."Y8888b.888  888888     
     X88Y88b.   888     X88     X88Y88..88P888     
 88888P' "Y8888P888 88888P' 88888P' "Y88P" 888 '''

if users_choice == 1:
    print("User has entered \n " + stone)
    user_pick="stone"
elif users_choice == 2:
    print("User has entered \n " + paper )
    user_pick="paper"
elif users_choice == 3:
    print("User has entered \n" + scissor)
    user_pick="scissor"

computers_choice=random.randint(1 , 3 )
if  computers_choice == 1:
    computer_pick="stone"
elif computers_choice == 2:
    computer_pick = "paper"
elif computers_choice == 3:
    computer_pick = "scissor"

print ("computer has picked" + computer_pick )

if user_pick == "stone" and computer_pick == "scissors":
    print ("User has Won")
elif user_pick == "scissors" and computer_pick == "paper":
    print("User has won")
elif user_pick == "paper" and computer_pick == "stone":
    print("User has won1")
else:
    print("Game Tie")

