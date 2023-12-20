# Pong Game
This is a WIP simple Pong game implementation in Python using the Pygame library.


## Description:
The game features a player paddle that can be controlled with the up and down arrow keys to hit a ball back and forth. There is also an AI paddle that tries to predict the ball's path and move to intercept it. 

The player scores a point when the AI misses the ball and vice versa. The first to 3 points wins.


## Features:
- Player paddle control with arrow keys
- AI paddle with basic ball path prediction
- Scoring system and winning condition
- Ball physics with paddle collision detection
- Background music and sound effects

## Requirements:
- Python 3
- Pygame 

## Usage:
To run the game, simply execute `python game.py` from this directory. Use the up/down arrows to control the player paddle. Press spacebar to serve the ball when a point is scored.

## Customization:
The game parameters like paddle size, ball speed, screen size etc. can be tweaked by modifying the constants defined in `game.py` and `display.py`. New sounds effect or background music can be added by replacing the files in this directory.

## License:
See LICENCE for mor info.

## Credits:
- Pong was originally created by Atari in 1972. This implementation was created for educational purposes.