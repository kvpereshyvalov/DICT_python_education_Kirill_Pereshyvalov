
SECRET_WORD = "python"

print("HANGMAN")

player_guess = input("Guess the word: > ")

if player_guess == SECRET_WORD:
    print("You survived!")
else:
    print("You lost!")



