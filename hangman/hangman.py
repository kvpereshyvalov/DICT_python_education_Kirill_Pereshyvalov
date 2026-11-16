
import random


WORDS = ["python", "java", "javascript", "php"]

secret_word = random.choice(WORDS)

word_hint = secret_word[:3] + "-" * (len(secret_word) - 3)

print("HANGMAN")

player_guess = input(f"Guess the word {word_hint}: > ")

if player_guess == secret_word:
    print("You survived!")
else:
    print("You lost!")
