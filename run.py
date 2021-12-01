'''
Main hangmand files
'''
import os
import random
from screen import HANGMANPICS as hangman


def get_random_word(file_name):
    """
    Get a random word from a file.txt.
    """
    with open(file_name, "r", encoding="UTF-8") as file:
        all_text = file.read()
        words = list(map(str, all_text.split()))
        word = random.choice(words).upper()
        file.close()
        return word


def refresh_board(name, rounds_nr, word, count, tries, score, message):
    """
    Player's name, number of tries left, round number, score, messages,
    the ASCII HANGMAN grafic and empty lines for word will be displayed.
    This information will be updated acordin to game result.
    """
    os.system("clear")
    print(f"Name: {name}")
    print(f"Tries left: {tries}")
    # print("Used letters: ")
    print(f"Round: {count}/{rounds_nr}")
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
    # TODO:
    # [x] implement round_nr calculator, same with score.
    # [ ] display word at the end of the game
    # [ ] create used letter and words lists
    # [ ] at the end of the game, option to continue playing or exit (y/n)

    score = 0
    message = ""
    # used_letters = []
    # guessed_words = []
    word_list = list(word)
    count = 0

    # Game
    while count < rounds_nr:
        count = count + 1
        message = f"Welcome to round {count}"
        tries = 6

        # Round
        guessed = False
        word_guess = ["_"] * len(word)

        while not guessed and tries > 0:
            refresh_board(name, rounds_nr, ' '.join(
                word_guess), count, tries, score, message)

            guess = input("Enter a letter/word: ").upper()

            # Check if word contains only letters
            if guess.isalpha():

                if len(guess) == 1:
                    # It's a letter
                    if guess in word_list:
                        message = "That's right!"
                    else:
                        message = "Nice try!"
                        tries -= 1
                else:
                    # User introduce a word
                    if list(guess) == word_list:
                        word_guess = guess
                        message = "Great job!"
                        score += 1
                        guessed = True
                    else:
                        message = "Wrong word!"
                        tries -= 1

            else:
                message = "Character not valid. Try again!"

            for i in range(len(word_guess)):
                if guess == word_list[i]:
                    word_guess[i] = guess

            if word_guess == word_list:
                message = "You won!"
                score += 1
                guessed = True

        if tries == 0:
            message = "You're dead!"
        refresh_board(name, rounds_nr, ' '.join(
            word_guess), count, tries, score, message)


def main():
    """
    Get input from the user.
    User will introduce a name (all characters accepted) and
    a welcome message will be displayed.
    Run a while loop to collect a numeric imput for rounds number from the user
    via the terminal. The loop will repeatedly request data, until it is valid.

    """
    # test values
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
    # word = get_random_word("assets/words.txt")
    game(name, rounds_nr, "MAMA")


if __name__ == "__main__":
    main()
