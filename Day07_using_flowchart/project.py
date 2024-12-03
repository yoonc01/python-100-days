from random import choice

hang_man = [
    """
  +---+
  |   |
  O   |
      |
      |
      |
=========
""",
"""
  +---+
  |   |
  O   |
  |   |
      |
      |
=========""",
"""  +---+
  |   |
  O   |
 /|   |
      |
      |
=========
""",
"""
  +---+
  |   |
  O   |
 /|\\  |
      |
      |
=========
""",
"""
  +---+
  |   |
  O   |
 /|\\  |
 /    |
      |
=========
""",
"""
  +---+
  |   |
  O   |
 /|\\  |
 / \\  |
      |
=========
"""
]


word_list = ["hello", "baby", "camel", "snake", "abcdefg"]

chosen_word = choice(word_list)
word_length = len(chosen_word)
display = ["-" for _ in range(word_length)]
filled = 0
life = 6
print("".join(display))

while (life != 0):
    guess = input("Guess a letter: ").strip().lower()
    if (len(guess) != 1):
        print("Enter a letter")
    success = False
    for idx in range(word_length):
        if guess == chosen_word[idx]:
            filled = filled + 1
            success = True
            display[idx] = guess
    if not success:
        life = life - 1
        print(f"You Guessed {guess}, that's not in the word. You lose a life.")
        print(hang_man[5 - life])
        print(f"****************************{life}/6 LIVES LEFT****************************")
    # 아래 조건 대신 "-" not in display 조건 적용해도 됨
    if filled == word_length:
        break
    print("".join(display))

if life == 0:
    print("You lose...")
    print(f"The answer is {chosen_word}")
else:
    print(f"Yes! The answer is {chosen_word}")
    print("You Win")

