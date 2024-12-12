from random import randint

def return_valid_input(statement, valid_values):
    # 아래 문구는 docstring이라는 함수를 설명하는 문장
    # IDLE에서 함수 위에 마우스를 hover하면 아래 내용이 설명으로 나옴
    """
    statement을 요청하고 유효한 값이 입력되지 않으면 statement를 재요청
    """
    while True:
        data = input(statement).lower()
        if data in valid_values:
            return data
        print(f"Invalid input! Please choose from {valid_values}.")

def number_guessing_game():
    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100")

    number = randint(1, 100)

    difficulty = return_valid_input("Choose a difficulty. Type 'easy' or 'hard': ", ["easy", "hard"])

    if difficulty == "easy":
        attempts = 10
    else:
        attempts = 5

    correct = False
    while (not correct and attempts != 0):
        guessed_number = input(f"Make a guess (Attempts left: {attempts}): ")

        if (guessed_number.isdigit()):
            guessed_number = int(guessed_number)
            if (guessed_number < 1 or guessed_number > 100):
                print("The number is between 1 and 100. Guess again (no attempts reduced).")
                continue
            if (guessed_number < number):
                print("Too low.")
            elif (guessed_number > number):
                print("Too High")
            else:
                print("Correct!")
                print(f"The number is {number}")
                return
            attempts = attempts - 1
        else:
            print("Invalid input! Please enter a number. Guess again (no attempts reduced).")
    print(f"The Number was {number}")

number_guessing_game()

while return_valid_input("Do you want to play again? (yes/no): ", ["yes", "no"]) == "yes":
    number_guessing_game()