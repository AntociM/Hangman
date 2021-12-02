'''
Main hangmand files
'''
import os
import random
from screen import HANGMANPICS as hangman


def get_random_word(file_name):
    """
    Get a random word from a file.
    Args:
        file_name   : path to a text file
    Return:
        word        : a string containing the random word
    """
    with open(file_name, "r", encoding="UTF-8") as file:
        all_text = file.read()
        words = list(map(str, all_text.split()))
        word = random.choice(words).upper()
        file.close()
        return word


def refresh_board(**kwargs):
    """
    This function is used to print the game progress in terminal.
    First it clears the terminal, then player's name, number of
    tries left, round number, score, extra messages, used words/letters,
    the ASCII HANGMAN grafic and a row of dashes for word will be displayed.
    """

    name = kwargs['name']
    max_rounds = kwargs['max_rounds']
    word = kwargs['word']
    current_round = kwargs['current_round']
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
Round      | {current_round}/{max_rounds}
Tries left | {tries}
-------------------------------
Used words: {used_words}
Used letters: {used_letters}
-------------------------------
{hangman[len(hangman)-1 - tries]}

{message}

{word}
''')


def play_round(name, current_round, max_rounds, score):
    '''
    This task contains the main hangman functionality.
    It chooses a random word from the text file, then
    it asks the user to insert characters or words,
    until the word is guessed or tries are 0.

    Args:
        name            : name of the user
        current_round   : the round number inside the game
        max_rounds      : the maximum number of rounds in the game
        score           : the score
    Return:
        0               : when the round is lost
        1               : when the round is won
    '''
    message = "Let's start !"
    tries = 6
    used_letters = []
    guessed_words = []
    guessed = False
    word = get_random_word("assets/words.txt")
    word_guess = ["_"] * len(word)
    word_list = list(word)
    win = 0

    while not guessed and tries > 0:
        refresh_board(
            name=name,
            max_rounds=max_rounds,
            word=' '.join(word_guess),
            current_round=current_round,
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
                    win = 1
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
            win = 1
            guessed = True

        if tries == 0:
            word_guess = word_list
            message = "You lost! The correct word was: "

        refresh_board(
            name=name,
            max_rounds=max_rounds,
            word=' '.join(word_guess),
            current_round=current_round,
            tries=tries,
            score=score,
            message=message,
            used_words=',  '.join(guessed_words),
            used_letters=',  '.join(used_letters)
        )
    return win


def game(name, rounds_nr):
    """
    One game is composed from one or more rounds. This function
    controls how many rounds are played, and keep tracks or the
    score.

    Args:
        name        : the name of the player
        rounds_nr   : how many rounds the game has
    Return:
        none
    """

    score = 0
    count = 0

    # Game
    while count < int(rounds_nr):

        # Round
        count = count + 1

        score += play_round(name, count, rounds_nr, score)

        if count < int(rounds_nr):
            input("Press enter to start the next round: ")

        print(f'''
-----------------------------------

█▀▀ ▄▀█ █▀▄▀█ █▀▀   █▀█ █░█ █▀▀ █▀█
█▄█ █▀█ █░▀░█ ██▄   █▄█ ▀▄▀ ██▄ █▀▄

You guessed {score} out of {rounds_nr}.

-----------------------------------

''')


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
Welcome to Hangman!

Rules of the game:
------------------
You will need to guess a random word by suggesting letters or words,
within 6 guesses. The word to guess is represented by a row of dashes,
with each dash representing a letter of the word. Good luck!
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

    print('''
Thank you for playing! Hope to see you soon.
    ''')


if __name__ == "__main__":
    main()
