# Cycle

Re-do of Cycles Repository

# Cycles Game

Cycle is a game where the players try to cut each other off using cycles that leave a trail behind them. Can you destroy your opponent with your trail?

## Getting Started

Make sure you have Python 3.8.0 or newer and Raylib Python CFFI 3.7 installed and running on your machine. You can install Raylib Python CFFI by opening a terminal and running the following command.

```
python3 -m pip install raylib
```

After you've installed the required libraries, open a terminal and browse to the project's root folder. Start the program by running the following command.

```
python3 Cycles
```

You can also run the program from an IDE like Visual Studio Code. Start your IDE and open the
project folder. Select the main module inside the Cycles folder and click the "run" icon.

## Project Structure

The project files and folders are organized as follows:

```
root                    (project root folder)
+-- Cycles              (source code for game)
  +-- game              (specific game classes)
    +-- casting         (game artifacts and actor)
    +-- directing       (game director)
    +-- scripting       (control actors actions)
    +-- services        (keyboard and video services)
    +-- shared          (game color and point)
  +-- __main__.py       (entry point for program)
  +--constants          (constant values)
+-- README.md           (general info)
```

## Required Technologies

- Python 3.8.0
- Raylib Python CFFI 3.7

## Rules

- Players can move up, down, left and right:
- Player one moves using the W, S, A and D keys.
- Player two moves using the I, K, J and L keys.
- Each player's trail grows as they eat food.
- Players try to maneuver so the opponent collides with their trail.
- If a player collides with their opponent's trail or eats the food of the other snake...THE GAME IS OVER!

## Requirements

- The program must have a README file.
- The program must have at least 16 classes.
- Each module, class and method must have a corresponding comment.
- The game must remain generally true to the order of play described in the overview.

## Team

Group name: team-01

- Aaron Bechtel
- Jared Malan
- Jessica Angulo
- Oscar Peterson
- Nayra Rebeca Ferreira
