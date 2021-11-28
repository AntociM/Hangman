
from screen import HANGMANPICS as hangman
import os

def game(name, rounds_nr, word_to_guess):
    os.system("clear")
    print(hangman[6])

def main():
    word_to_guess = "gift"
    rounds_nr = 0
    score = 0
    print("Hangman!")
    name = input("Enter your name: ")
    print(f"Welcome, {name}")
    while True:
        rounds_nr = input("Insert number of rounds from 1 to 10: ")
        if rounds_nr.isnumeric():
            break
        else:
            print("Oops! Try again")

    game(name, rounds_nr, word_to_guess)


# def update_board(name, rounds_nr, word_to_guess, strikes, score):

# class screen():
#     print("Strikes:")

if __name__ == "__main__":
    main()
    
