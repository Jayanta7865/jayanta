#snake,water,gun game
import random

rules="Rules:-[The gun beats the snake] and [the water beats the gun] and [snake beats the water]..\n"
print(rules)
your_turn=input("Please write snake/water/gun : ").lower()
print("You select",your_turn)
computer=random.choice(["snake", 
                        "water", 
                        "gun"])
print("Computer select",computer)


if computer==your_turn:
    print("The match is draw.")
elif computer == "snake" and your_turn == "water":
    print("You lose!.computer win")
elif computer == "water" and your_turn == "snake":
    print(" You win!.")
elif computer == "snake" and your_turn == "gun":
    print("You win!")
elif computer == "gun" and your_turn == "snake":
    print("You lose!!.Computer win!")

elif computer == "water" and your_turn == "gun":
    print("You lose.Computer win!")
elif computer == "gun" and your_turn == "water":
    print("You win!")
else:
    print("Please chose correct option..")


