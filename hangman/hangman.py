
import random


WORDS = ["python", "java", "javascript", "php"]
MAX_LIVES = 8


def display_word(secret_word: str, guessed_letters: set[str]) -> str:
    """Displays guessed letters and hides the remaining ones."""
    return "".join(
        letter if letter in guessed_letters else "-"
        for letter in secret_word
    )


def play_game() -> None:
    """Starts one round of Hangman."""
    secret_word = random.choice(WORDS)
    guessed_letters = set()
    remaining_lives = MAX_LIVES

    print()
    print("-" * len(secret_word))

    while remaining_lives > 0:
        player_letter = input("Input a letter: > ")

        if len(player_letter) != 1:
            print("You should input a single letter")

        elif not ("a" <= player_letter <= "z"):
            print("Please enter a lowercase English letter")

        elif player_letter in guessed_letters:
            print("You've already guessed this letter")

        else:
            guessed_letters.add(player_letter)

            if player_letter not in secret_word:
                print("That letter doesn't appear in the word")
                remaining_lives -= 1

        displayed_word = display_word(secret_word, guessed_letters)

        print()
        print(displayed_word)

        if displayed_word == secret_word:
            print(f"You guessed the word {secret_word}!")
            print("You survived!")
            return

        if remaining_lives == 0:
            print("You lost!")
            return


def main() -> None:
    """Displays the main menu and controls the game."""
    print("HANGMAN")

    while True:
        menu_choice = input(
            'Type "play" to play the game, "exit" to quit: > '
        ).strip()

        if menu_choice == "play":
            play_game()

        elif menu_choice == "exit":
            break


if __name__ == "__main__":
    main()
