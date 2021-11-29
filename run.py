import os
import random
from screen import HANGMANPICS as hangman


def get_random_word(file_name):
    with open(file_name, "r") as file:
        all_text = file.read()
        words = list(map(str, all_text.split()))
        word = random.choice(words).upper()
        file.close()
        return word


def refresh_board(name, rounds_nr, word, tries, score, message):
    os.system("clear")
    print(f"Name: {name}")
    print(f"Tries left: {tries}")
    # print("Used letters: ")
    print(f"Round number: {rounds_nr}")
    print(f"Score: {score}")
    print(hangman[len(hangman)-1 - tries])
    print(message)
    print(word)


def game(name, rounds_nr, word):
    """
    Starts game, colecting user imput in form of letter or words.
    Each validated imput, will prompt a message in terminal for 3 scenarios:
    letter is in word, already used letter/word or incorrect. 
    """
    word_to_guess = "_ " * len(word)
    tries = 6
    guessed = False
    message = ""
    # used_letters = []
    guessed_words = []

    while not guessed and tries > 0:
        refresh_board(name, rounds_nr, word_to_guess, tries, 0, message)

        guess = input("Enter a letter/word: ").upper()
        if guess.isalpha():
            if guess in word:
                message = "That's right!"
            else:
                tries -= 1
        elif len(guess) == len(word):
            if guess in guessed_words:
                message = f"You already tried {guess}!"

            elif guess != word:
                message = "Incorrect!"
                tries -= 1
                guessed_words.append(guess)
            else:
                guessed = True
        else:
            message = "Character not valid. Try again!"

    refresh_board(name, rounds_nr, word_to_guess, tries, 0, "You're dead!")


def main():
    rounds_nr = 0
    print("Let's play Hangman!")
    name = "Mihaela"
    rounds_nr = 2
    # Uncomment later
    # name = input("Enter your name: ")
    # print(f"Welcome, {name}")
    # while True:
    #     rounds_nr = input("Insert number of rounds from 1 to 10: ")
    #     if rounds_nr.isnumeric():
    #         break
    #     else:
    #         print("Oops! Try again")
    # word = get_random_word("words.txt")
    game(name, rounds_nr, "MAMELON")


if __name__ == "__main__":
    main()
