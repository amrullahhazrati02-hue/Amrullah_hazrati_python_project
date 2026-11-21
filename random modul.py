
print("Welcome to treasure Island.")
print("Your mission is to find the treasure.")
choice1=input("You\'r at a crossroad, where do you want to go? type 'right' or 'left'.")
if choice1=='left':
    choice2=input("You\'ve come to a lake.There is an island in the middle of the lake.\n Type 'wait' to wait for a boat. type 'swim' to swim across.")
    if choice2=='wait':
        choice3=input("you arrive at the island undarmed. There is a house with 2 doors.\n One red, one yellow and one blue. Which colour do you choose?")
        if choice3=='red':
            print("Game over. You lost!")
        elif choice3=='yellow':
            print("Game over. You won!")
        else:
            print("Game over. You lost!")
    else:
        print("Game over. You lost!")
else:
    print("you fall at hole!")