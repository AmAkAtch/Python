print("Welcome to Treasure Island. Your choices will make to reach the Treasure...")
print("Be carefull on your way adventurer !")

choice = input('You are at Crossroads, Go "left" or "Right"?').lower()

if choice == "left":
    choice = input('You encountered River on the way, "Swim" or "wait"').lower()
    if(choice == "wait"):
        choice = input('3 doors stand infront of you as final hurdle, Which door will you choose?"Red", "Blue", "Yellow" ?').lower()
        if(choice=="yellow"):
            print("Hurray !! You found the lost trasure from 100 years before...")
        elif(choice=="blue"):
            print("Tood bad !! You found monster, Game Over !")
        elif(choice == "red"):
            print("Too bad, You got blown to pieces!!! Game Over !")
        else:
            print("Wish your mamma taught you how to wright, Invalid choice - Game over !!!")
    elif(choice=="swim"):
        print("Brother, You can't Swim, Game over !!!")
    else:
        print("Brother, ooo!!! Wass that brother?? Invalid option - Game over !!!")
elif (choice == "right"):
    print("Too bad, Right was leading towards valley, Game over !")
else:
    print("Invalid choice, Game over Brother!")