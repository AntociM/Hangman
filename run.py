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


def refresh_board(**kwargs):
    """
    Player's name, number of tries left, round number, score, messages,
    the ASCII HANGMAN grafic and a row of dashes for word will be displayed.
    This information will be updated acording to game result.
    """

    name = kwargs['name']
    rounds_nr = kwargs['rounds_nr']
    word = kwargs['word']
    count = kwargs['count']
    tries = kwargs['tries']
    score = kwargs['score']
    message = kwargs['message']
    used_words = kwargs['used_words']
    used_letters = kwargs['used_letters']

    os.system("clear")
    print(f'''

█░█ ▄▀█ █▄░█ █▀▀ █▀▄▀█ ▄▀█ █▄░█
█▀█ █▀█ █░▀█ █▄█ █░▀░█ █▀█ █░▀█

===============================
Name       | {name}
Score      | {score}
Round      | {count}/{rounds_nr}
Tries left | {tries}
{hangman[len(hangman)-1 - tries]}

-------------------------------
Used words: {used_words}
Used letters: {used_letters}
-------------------------------

{message}

{word}
''')


def game(name, rounds_nr):
    """
    Starts game, colecting user imput in form of letter or words.
    Each validated imput, will prompt a message in terminal for 3 scenarios:
    letter is in word, already used letter/word or incorrect.
    """

    score = 0
    message = ""
    # word_list = list(word)
    count = 0

    # Game
    while count < int(rounds_nr):
        count = count + 1
        message = "Let's start!"
        tries = 6
        used_letters = []
        guessed_words = []

        # Round
        guessed = False
        word = get_random_word("assets/words.txt")
        word_guess = ["_"] * len(word)
        word_list = list(word)

        while not guessed and tries > 0:
            refresh_board(
                name=name,
                rounds_nr=rounds_nr,
                word=' '.join(word_guess),
                count=count,
                tries=tries,
                score=score,
                message=message,
                used_words=',  '.join(guessed_words),
                used_letters=',  '.join(used_letters)
            )

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
                        if guess not in used_letters:
                            used_letters.append(guess)
                else:
                    # User introduce a word
                    if list(guess) == word_list:
                        word_guess = guess
                        message = "Great job!"
                        score += 1
                        guessed = True
                    else:
                        message = "Wrong word!"
                        if guess not in guessed_words:
                            guessed_words.append(guess)
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
            message = f"You're dead! The correct word was: \
                {''.join(word_list)}"
        refresh_board(
            name=name,
            rounds_nr=rounds_nr,
            word=' '.join(word_guess),
            count=count,
            tries=tries,
            score=score,
            message=message,
            used_words=',  '.join(guessed_words),
            used_letters=',  '.join(used_letters)
        )

        if count < int(rounds_nr):
            input("Enter any key to continue: ")

    # if count == int(rounds_nr):
        print("Game over!")


def main():
    """
    Get input from the user.
    User will introduce a name (all characters accepted) and
    a welcome message will be displayed.
    Run a while loop to collect a numeric imput for rounds number from the user
    via the terminal. The loop will repeatedly request data, until it is valid.

    """

    os.system('clear')
    print('''

█░█ ▄▀█ █▄░█ █▀▀ █▀▄▀█ ▄▀█ █▄░█
█▀█ █▀█ █░▀█ █▄█ █░▀░█ █▀█ █░▀█

===============================

Let's play Hangman!
Player tries to guess a word by suggesting
letters/words within 6 guesses. The word to
guess is represented by a row of dashes,
representing each letter of the word.
''')

    name = input("Enter your name: ")
    while True:
        os.system('clear')
        print(f"Welcome, {name}!")

        # Run until valid input
        while True:
            rounds_nr = input("Insert number of rounds from 1 to 10: ")
            if rounds_nr.isnumeric() and int(rounds_nr) in range(1, 11):
                break
            else:
                print("Oops! Try again")

        game(name, rounds_nr)

        # Exit
        if input("Do you want to play a new game?\nPress 'Y' to continue, \
anything else to exit: ").upper() == "Y":
            continue
        else:
            break


if __name__ == "__main__":
    main()
