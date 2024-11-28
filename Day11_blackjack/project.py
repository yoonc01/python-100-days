from cards_module import pop_random_card, calculate_score

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

user_cards = []
computer_cards = []
user_score = 0
computer_score = 0

is_game_over = False

for _ in range(2):
    # dealer와 user 번갈아가며 hit함
    computer_cards.append(pop_random_card())
    user_cards.append(pop_random_card())

while not is_game_over:
    user_score = calculate_score(user_cards)
    computer_score = calculate_score(computer_cards)
    print(f"Your cards: {user_cards}, current cards: {user_score}")
    print(f"Computer's second card: {computer_cards[1]}")
    if user_score == 21 or computer_score == 21 or user_score > 21:
        is_game_over = True
    else:
        user_want_to_deal = return_valid_input("Type 'y' to get another card, type 'n' to pass: ", ['y', 'n'])
        if (user_want_to_deal == 'y'):
            user_cards.append(pop_random_card())
        else:
            is_game_over = True

if user_score > 21:
    print(f"Your cards: {user_cards}, total score: {user_score}.")
    print("You went over 21 and busted. Game over.")
else:
    while computer_score < 17:
        computer_cards.append(pop_random_card())
        computer_score = calculate_score(computer_cards)

    print(f"Computer's cards: {computer_cards}, total score: {computer_score}.")
    if computer_score > 21:
        print("The computer went over 21 and busted. You win!")
    elif computer_score == user_score:
        print(f"It's a draw! Both you and the computer have a score of {user_score}.")
    elif computer_score == 21:
        print(f"The computer hit Blackjack with a score of {computer_score}. You lose.")
    elif user_score == 21:
        print(f"You hit Blackjack with a score of {user_score}. You win!")
    elif user_score > computer_score:
        print(f"Your score of {user_score} beats the computer's score of {computer_score}. You win!")
    else:
        print(f"The computer's score of {computer_score} beats your score of {user_score}. You lose.")
