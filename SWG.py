print("WELCOME TO 'SNAKE WATER GUN'!\n")
import random
number=int(input("Number Of Rounds: "))
print("INSTRUCTIONS:\n1. Gun Beats Snake.\n2. Snake Beats Water.\n3. Water Beats Gun.\n")
print("1 Point For Win, 0 Point For Draw/Lose. READY?")
comp_point=0
user_point=0

for i in range(0,number):
    print(f"ROUND {i+1}\n")
    print("Press 0-Stop\n1-Snake\n2-Water\n3-Gun")
    choice=(int(input("Enter Number: ")))
    if(choice==0):
        print("EXITING.")
        break
    else:
        comp_rand=random.randint(1,3)
        print(f"Computer Chose {comp_rand}")
        if(comp_rand==choice):
            print("Draw\n")
            comp_point=comp_point+0
            user_point=user_point+0
        elif(comp_rand==1 and choice==2):
            print("Computer Won\n")
            comp_point=comp_point+1
            user_point=user_point+0
        elif(comp_rand==1 and choice==3):
            print("Player Won\n")
            comp_point=comp_point+0
            user_point=user_point+1
        elif(comp_rand==2 and choice==1):
            print("Player Won\n")
            comp_point=comp_point+0
            user_point=user_point+1
        elif(comp_rand==2 and choice==3):
            print("Computer Won\n")
            comp_point=comp_point+1
            user_point=user_point+0
        elif(comp_rand==3 and choice==1):
            print("Computer Won\n")
            comp_point=comp_point+1
            user_point=user_point+0
        elif(comp_rand==3 and choice==2):
            print("Player Won\n")
            comp_point=comp_point+0
            user_point=user_point+1
print("GAME OVER!")
if(comp_point>user_point):
    print(f"You Lost!\nYour Score: {user_point}\nComputer's Score: {comp_point}")
elif(comp_point==user_point):
    print("Match Draw.")
else:
    print(f"YOU WON!\nYour Score: {user_point}\nComputer's Score: {comp_point}")
print("THANK YOU!")