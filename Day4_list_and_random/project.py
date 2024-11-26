import game_module
import random

player = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors\n"))
computer = random.randint(0, 2)

if player == 0:
    print(game_module.rock)
elif player == 1:
    print(game_module.paper)
elif player == 2:
    print(game_module.scissor)
else:
    print("Invalid input")


print("Computer chose: ")

if computer == 0:
    print(game_module.rock)
elif computer == 1:
    print(game_module.paper)
else:
    print(game_module.scissor)

result = (player - computer + 3) % 3

if result == 0:
    print("It's a draw")
elif result == 1:
    print("You Win")
else:
    print("You lose")
