
import random


WORDS = ["python", "java", "javascript", "php"]

secret_word = random.choice(WORDS)

print("HANGMAN")

player_guess = input("Guess the word: > ")

if player_guess == secret_word:
    print("You survived!")
else:
    print("You lost!")
