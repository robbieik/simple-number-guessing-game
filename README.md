# Number Guessing Game

A simple Python-based guessing game where players try to guess a randomly generated number within a spcified range.

## How to play
1. Set the range, by entering the desired lower and upper limit
2. Try to guess the number
3. The game will let you know if the number is too high or too low
4. See how many attempts it took and try to beat your best score
5. Choose to play multiple rounds and improve your score

## Simple features

- 6 difficulty levels: From 'Very Easy'(1-10) to 'Are you insane?'(1-1.000.000) + custom ranges
- Input Validation
- Score tracking
- Multiple Rounds
- Simple hint system with 4 different hint types. which vary depending on the attempt number
- Hint usage penalties
- Save system that saves between sessions using JSON

Game Balance
- Hints are disabled on 'very easy'
- The penalty system motivates the player to strategically use hints
- Dynamic range hints provide great help, but it does so with a higher penalty.

To run the game, simply download the file, navigate to the download directory and run it - please note that Python needs to be installed on the system.

## Potential features I might add:

- Difficulty levels with preset ranges - Added in v2.0
- Hints - Added in v2.0
- Save high scores across different sessions - Added in v2.0
- GUI
- Multiplayer mode

*This project was created as part of my Python learning journey.*
