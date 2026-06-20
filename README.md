# Turtle Crossing 🐢

A classic *Frogger*-style arcade game built with Python's built-in `turtle` graphics module. Guide your turtle from the bottom of the screen to the top while dodging a never-ending stream of cars. Survive a crossing and you advance a level — and the cars get faster.

## Demo

▶️ **[Watch the demo video](https://drive.google.com/file/d/1aSMK5cjDvLs057si_pKZjek1K6vxnxYy/view?usp=drive_link)**

## Gameplay

- You control a turtle that starts at the bottom of the screen.
- Press the **Up arrow** key to move the turtle forward (upward).
- Cars spawn on the right edge and drive left across the screen.
- Reach the finish line at the top to advance to the next level. The turtle resets to the start and every car speeds up.
- Touch a car and it's **Game Over**.

## Requirements

- Python 3.x (developed with Python 3.11)
- The `turtle` module, which ships with the standard library (no extra installation needed).

> Note: `turtle` requires Tkinter. On most platforms it comes with Python, but some minimal Linux installs may need `sudo apt install python3-tk`.

## How to Run

From the project directory:

```bash
python main.py
```

A 600×600 game window will open. Click on the window first if the Up arrow doesn't respond, then start crossing.

## Controls

| Key | Action |
| --- | --- |
| ↑ (Up arrow) | Move the turtle forward |

## Project Structure

| File | Responsibility |
| --- | --- |
| [main.py](main.py) | Sets up the screen and runs the main game loop (spawning cars, detecting collisions, handling level progression). |
| [player.py](player.py) | The `Player` turtle — movement, position reset, and finish-line detection. |
| [car.py](car.py) | The `Car` turtle — a single car's appearance and movement. |
| [car_manager.py](car_manager.py) | The `CarManager` — generates cars at random positions/colors, moves them, and increases their speed. |
| [scoreboard.py](scoreboard.py) | The `Scoreboard` — displays the current level and the "Game Over" message. |

## How It Works

The game runs an infinite loop in [main.py](main.py) that:

1. Spawns a new car roughly every 5 ticks.
2. Moves all active cars one step to the left.
3. Checks the distance between each car and the player — a distance under 20 pixels counts as a collision and ends the game.
4. Checks whether the player has crossed the finish line (`y > 280`); if so, it increases the level, resets the player, and bumps up the car speed.

Cars get faster by `MOVE_INCREMENT` (10) each level, starting from a base speed of 5.
