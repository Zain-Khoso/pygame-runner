# Pygame Runner

A classic 2D infinite runner built with Python and the Pygame library. Dodge ground-based snails and airborne flies to rack up your high score.

## Features

- Sprite-Based Animation: Smooth frame switching for the player, snails, and flies.

- Dynamic Obstacle Spawning: Randomly generated enemies with varied spawn intervals and types.

- Physics System: Gravity-based jumping mechanics.

- Game States: Interactive menu system with score tracking and music toggling.

- Modular Architecture: Clean separation of concerns between game logic, settings, and entities.

## Installation

Ensure you have Python installed.

1. Clone the repository:

```bash
git clone https://github.com/zain-khoso/pygame-runner.git
cd pygame-runner
```

2. Install dependencies:

```bash
pip install -r requirements.txt
```

3. Run the game:

```bash
python main.py
```

## How to Play

- Spacebar: Start the game / Jump.

- Escape: Return to menu / Quit game.

- Goal: Avoid the enemies. Every obstacle that leaves the screen increases your score.

## Project Structure

Given the modular setup of the project:

- **main.py**: The entry point of the application.

- **game/**
    - **game.py**: Main game engine and event loop handling.

    - **settings.py**: Centralized configuration for paths, colors, and constants.

    - **player.py**: Sprite class for the player (input and gravity).

    - **obsticle.py**: Sprite class for enemies (movement and animation).

    - **score.py**: Logic for tracking and rendering the score.

- **assets/**: Contains all graphics, fonts, and audio files.

---

Made with Problem Solving by [Zain Khoso](https://linkedin.com/in/zain-khoso)