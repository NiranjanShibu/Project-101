import random

response = input("Press Y when you want to roll the dice, press N to quit")

while(response == "y"):
    no = random.randint(1,6)
    print("-------")

    if(no == 2 or no == 3):
        print("|    0|")
    elif(no == 4 or no == 5):
        print("|0   0|")
    elif(no == 6):
        print("|0 0 0|")
    elif(no == 1):
        print("|     |")

    if(no == 2 or no == 4 or no == 6):
        print("|     |")
    elif(no == 1 or no == 5 or no == 3):
        print("|  0  |")

    if(no == 2 or no == 3):
        print("|0    |")
    elif(no == 4 or no == 5):
        print("|0   0|")
    elif(no == 6):
        print("|0 0 0|")
    elif(no == 1):
        print("|     |")

    print("-------")

    response = input("Press Y when you want to roll the dice, press N to quit")