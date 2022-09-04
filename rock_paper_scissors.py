import random

user_wins = 0
computer_wins = 0
options = ["rock","paper" , "scissors"]

while True :
    user_input = input ("type Rock/Paper/scissors or Q to quit the game: ").lower()
    if user_input == "q":
        break
    if user_input not in ["rock","paper" , "scissors"] :
        continue
    


    randomnumber = random.randint(0,2)
    # rock:0 , paper : 1 , scissors :2
    computer = options[randomnumber]
    print("computer picked",computer)

    if user_input == "rock" and computer =="scissors" :
        print("you won !")
        user_wins += 1
        
    elif user_input == "paper" and computer =="rock" :
        print("you won !")
        user_wins += 1
        
    elif user_input == "scissors" and computer =="paper" :
        print("you won !")
        user_wins += 1
    elif user_input== computer :
        print("Draw")
    else :
        print("you lost ;(")
        computer_wins += 1

print ("you won",user_wins,"times")
print ("computer won",computer_wins,"times")








