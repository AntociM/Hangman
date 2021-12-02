# Hangman

Hangman is a Python command-line game, after the classic paper and pencil guessing game.

Users try to guess a word suggesting letters or words,
within 6 guesses. The word to guess is represented by a row of dashes.

![Display](../assets/images/responsive.jpg)

[The live version of the project can be accessed here.](https://antocim-hangman.herokuapp.com/)

## How to play

This version is based on the same rules as the traditional game. More about game history and rules, can be found on [Wikipedia](https://en.wikipedia.org/wiki/Hangman_(game)).

In this version, the player introduces his name and a chosen number of rounds between 1-10.

A raw of dashes will arise representing each letter of a random word to be guessed, within 6 tries.

The player can introduce letters or words until out of tries or the right word is guessed. 

Game progress will be displayed all the time, represented by score, round number, lists of used letter and words.

Graphically, each new body part of the Hangman simbolyse an inccorect input.



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