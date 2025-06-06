import random

print("Welcome to Snake-Water-Gun Game!")
print("Choices: 's' for Snake, 'w' for Water, 'g' for Gun")

choices = ["s", "w", "g"]
choice_map = {"s": 1, "w": -1, "g": 0}

# Randomly generate computer's choice
computer_choice = random.choice(choices)
computer = choice_map[computer_choice]

# Get user's choice
youstr = input("Enter your choice (s/w/g): ").lower()

# Validate input
if youstr not in choice_map:
    print("Invalid input! Please enter 's', 'w', or 'g'.")
else:
    you = choice_map[youstr]

    print(
        f"\nYou chose: {youstr.upper()}  |  Computer chose: {computer_choice.upper()}"
    )

    # Game Logic
    if you == computer:
        print("It's a Draw!")
    elif (
        (you == 1 and computer == -1)
        or (you == 0 and computer == 1)
        or (you == -1 and computer == 0)
    ):
        print("You Win!")
    else:
        print("You Lose!")
