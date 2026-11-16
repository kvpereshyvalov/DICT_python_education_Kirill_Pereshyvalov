
import random


WORDS = ["python", "java", "javascript", "php"]
MAX_ATTEMPTS = 8

secret_word = random.choice(WORDS)
guessed_letters = set()
remaining_attempts = MAX_ATTEMPTS

print("HANGMAN")
print()

displayed_word = "-" * len(secret_word)
print(displayed_word)

while remaining_attempts > 0:
    player_letter = input("Input a letter: > ")

    if player_letter not in secret_word:
        print("That letter doesn't appear in the word")

    guessed_letters.add(player_letter)

    displayed_word = "".join(
        letter if letter in guessed_letters else "-"
        for letter in secret_word
    )

    print()
    print(displayed_word)

    remaining_attempts -= 1

print()
print("Thanks for playing!")
print("We'll see how well you did in the next stage")
