# Hangman

Hangman is a Python command-line game after the classic paper and pencil guessing game.

Users try to guess a word suggesting letters and words within six tries. A row of dashes represents the word to guess.
![Display](assets/images/responsive.jpg)

[The live version of the project can be accessed here.](https://hangman-r13n.onrender.com)

## How to play

This version is based on the same rules as the traditional game. More about game history and rules can be found on [Wikipedia](https://en.wikipedia.org/wiki/Hangman_(game)).

In this version, the player introduces his name and a chosen number of rounds between 1-10.

A raw of dashes will arise representing each letter of a random word to be guessed within six tries.

The player can introduce letters or entire words until out of tries, or the word is guessed. 

Game progress will be displayed all the time, represented by score, round number, lists of used letters and words.

Graphically, each new body part of the Hangman represent an incorrect input.

## Features

The game is following this flow diagram:

![Welcome screen](assets/images/flowchart.png)

### Existing Features

- User input:
    - Every user input is validated and error checked.
    - In the initial phase user is allowed to pick his name and the number of rounds.
    - Allows the user to insert single letters and whole words.
    - Letters and words are not case sensitive.

- ASCII art was used to improve the visual aspect of the game.

![Welcome screen](assets/images/welcome-screen.jpg)

- Dashboard
    - The game continuously updates the player about the progress via the dashboard. It contains information about the score, tries left, current round number, used letters, and used words.
    - Has the classic hangman drawing, which updates based on tries.
    - Has an incremental display of the secret word.
    - The player cannot see the complete word until a correct guess is made or round is over.

![Board img](assets/images/Board1.jpg)

- User feedback messages like "Nice try!" and "That's right!".

- Terminal is frequently cleared to keep the game in player's focus.

- One randomly selected word per round.

- Play against the computer.

- Possibility to start a new game exists in the game.

- Possibility to easily change the word bank by adding/replacing text into the `words.txt` file.

- No external or third-party dependencies.

### Future features
- Add 2-player mode, where one `user1` introduces the word, while `user2` guesses. If `user2` guesses his score goes up by one point, otherwise `user1`'s score goes up.
- Add multiple difficulty levels.
- Add the possibility for user to select the list of words from which to choose.
- Refactor the game to use classes.

## Testing
I have tested the code manually by:
- Frequently linting the code using PEP8 and Pylint linters. Errors have been detected, and I fixed them incrementally. Refer to [this page](docs/test.md) for more details.
- Trying inputs that are close to the extremes:
    - since `round` is restricted between 1-10, I tried playing 1, 5, and 10 rounds. Everything outside this range was reported invalid by the game. 
    - during testing I inserted both uppercase and lowercase characters.
    - when guessing I inserted both characters between [a-z], and numbers, punctuation signs and special characters.


## Bugs

### Solved bugs
- Used letters allowed duplicated values if the user selected the same wrong character twice. Solved by checking if the character is already in the list before appending it.
- Sometimes, words with punctuation were randomized from the file, which creates an imposibility to win. Solved by removing the punctuation in the text file.
- The case sensitivity was making the game impossible to win. I removed this sensitivity by converting both the randomized word and user inputs to uppercase.
- Because of the `clearing` terminal approach, the end of round display was not visible to the user. Next round started automatically. This bug was visible only when a number of rounds was greater than one. I solved this by asking the user to press any key to start a new round. 

### Open bugs
- None

## Deployment

This project was deployed using Code Institute's mock terminal for Heroku.

Steps for deployment:
- Fork or clone repository
- Create a new Heroku application
- Set the buildpacks to `Python` and `NodeJS`
- Link the Heroku app to the repository
- Click on *Deploy*

## Credits
- Code Institute for deployment mock terminal
- [Wikipedia](https://en.wikipedia.org/wiki/Hangman_(game)) for information on Hangman(game)
- [This file](https://gist.github.com/chrishorton/8510732aa9a80a03c829b09f12e20d9c) for Hangman ASCII art
- [ASCII art](https://fsymbols.com/text-art/#all_cats)
- [Creating FlowChart](https://mermaid.live) as inspiration
- [For suggestion](https://www.geeksforgeeks.org/pulling-a-random-word-or-string-from-a-line-in-a-text-file-in-python/) in order to extract a random word from a text.
- Oxford Internationals English Schools, for words.txt [text content](https://www.oxfordinternationalenglish.com/a-brief-history-of-the-english-language/)



```mermaid
graph TD 
    A[Start game] -->A0[/Welcome to Hangman!/]
    A0 --> A1[/Enter your name:/]
    A1 --> A2[/Insert number of rounds:/]
    A2 --> A3{if character != number}
    A3 --> A2
    A3 --> A4
    A4[Play] --> B[/Enter a letter/]
    B --> b1{if character != letter}
    b1 --> B
    b1 --> b2{if letter in word}
    b2 -- Yes --> D[/Display letter in line/]
    b2 --No --> E[/Draw hangman/]
    E --> F{if attempts left != 0}
    F --> B
    F --> G[/You have lost this round/] 
    D --> H{if word is complete}
    H --> B
    H --> J[/You won this round/] 
    J --> K[End round]
    G --> K 
    K --> L{if rounds left}
    L --> A4
    L-->M[End game]
    
    
```