import random

print("Rules: Gun beats Snake | Snake beats Water | Water beats Gun..\n")

choices = ["snake", "water", "gun"]


winning_rules = {
    "snake": "water",   # snake beats water
    "water": "gun",     # water beats gun
    "gun": "snake"      # gun beats snake
}

user_score = 0
computer_score = 0

while True:
    user = input("Enter snake/water/gun: ").lower()

    if user not in choices:
        print("Invalid choice! Please enter snake / water / gun.\n")
        continue

    computer = random.choice(choices)

    print(f"\nYou selected: {user}")
    print(f"Computer selected: {computer}")

    if user == computer:
        print("It's a draw!")
    elif winning_rules[user] == computer:
        print(" You Win this round!")
        user_score += 1
    else:
        print("You Lose this round!")
        computer_score += 1

    print(f"Score \n  You: {user_score}  |  Computer: {computer_score}\n")

    play_again = input("Do you want to play again? (yes/no): ").lower()
    if play_again != "yes":
        print("\n---------- Final Score ----------")
        print(f" You: {user_score}")
        print(f" Computer: {computer_score}")
        print("---------------------------------")

        if user_score > computer_score:
            print(" Congratulations! You are the overall winner!")
        elif computer_score > user_score:
            print(" Computer wins the game! Better luck next time.")
        else:
            print(" The game is a draw!")

        print("\nThanks for playing! ")
        break
