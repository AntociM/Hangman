import random
from screen import HANGMANPICS as hangman
import os

def get_random_word(file_name):
    with open(file_name, "r") as file:
        all_text = file.read()
        words = list(map(str, all_text.split()))
        word = random.choice(words)
        return word



def main():
    rounds_nr = 0
    score = 0
    print("Let's play Hangman!")
    name = "Mihaela"
    rounds_nr = 2
    # Uncomment later
    # name = input("Enter your name: ")
    # print(f"Welcome, {name}")
    # while True:
        # rounds_nr = input("Insert number of rounds from 1 to 10: ")
        # if rounds_nr.isnumeric():
            # break
        # else:
            # print("Oops! Try again")
    word123456 = get_random_word("words.txt")
    


# class screen():
    # print("Strikes:")

if __name__ == "__main__":
    main()
    
