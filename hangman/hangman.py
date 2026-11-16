
import random


WORDS = ["python", "java", "javascript", "php"]
MAX_LIVES = 8


def display_word(secret_word, guessed_letters):
    """Показує вгадані літери та дефіси замість невгаданих."""
    return "".join(
        letter if letter in guessed_letters else "-"
        for letter in secret_word
    )


def play_game():
    secret_word = random.choice(WORDS)
    guessed_letters = set()
    remaining_lives = MAX_LIVES

    print("HANGMAN")
    print()

    displayed_word = display_word(secret_word, guessed_letters)
    print(displayed_word)

    while remaining_lives > 0:
        player_letter = input("Input a letter: > ")

        if player_letter not in secret_word:
            print("That letter doesn't appear in the word")
            remaining_lives -= 1

        elif player_letter in guessed_letters:
            print("No improvements")
            remaining_lives -= 1

        else:
            guessed_letters.add(player_letter)

        displayed_word = display_word(secret_word, guessed_letters)

        print()
        print(displayed_word)

        if displayed_word == secret_word:
            print("You guessed the word!")
            print("You survived!")
            return

    print("You lost!")


if __name__ == "__main__":
    play_game()
