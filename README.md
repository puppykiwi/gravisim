# Gravitation Slingshot Effect

## Overview
This project simulates the gravitational slingshot effect using Pygame. It features a central planet and spacecrafts that the user can launch, which then interact with the planet's gravity.

## Requirements
- Python 3.x
- Pygame
- `util.py`, `planet.py`, `spacecraft.py`

## Installation
1. Clone the repository or download the code.
2. Ensure you have Python 3 installed.
3. Install Pygame using pip:
   ```sh
   pip install pygame
   ```
4. Ensure `util.py`, `planet.py`, and `spacecraft.py` are in the same directory as the main script.

## Files
- `main.py`: The main script containing the game logic.
- `util.py`: Utility functions and constants.
- `planet.py`: Contains the `Planet` class.
- `spacecraft.py`: Contains the `Spacecraft` class.

## Running the Simulation
Run the main script:
```sh
python main.py
```

## Controls
- **Mouse Click**: 
  - First click sets the starting position of the spacecraft.
  - Second click sets the direction and speed (based on distance from the starting position) and launches the spacecraft.
- **Arrow Keys**:
  - Up/Down: Increase/Decrease the velocity scale (controls the spacecraft's initial speed).
  - Right/Left: Increase/Decrease the gravitational constant (controls the planet's gravity strength).

## Code Explanation

### Imports and Initialization
```python
import math
import pygame
from util import *
from planet import Planet
from spacecraft import Spacecraft

pygame.init()
disp = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Gravitation Slingshot Effect")
pygame.display.set_icon(pygame.image.load("assets/jupiter.png"))
```
This section initializes Pygame and sets up the display window with a title and icon.

### Create Spacecraft
```python
def create_ship(Location, mouse):
    t_x, t_y = Location
    m_x, m_y = mouse
    vel_x = (m_x - t_x) / VEL_SCALE
    vel_y = (m_y - t_y) / VEL_SCALE
    obj = Spacecraft(t_x, t_y, vel_x, vel_y, SHIP_MASS, disp)
    return obj
```
This function creates a spacecraft object with an initial position and velocity based on the user's mouse clicks.

### Control Function
```python
def control(key):
    global VEL_SCALE, G
    if (key == pygame.K_UP) & (VEL_SCALE > 10):
        VEL_SCALE -= 10
    elif (key == pygame.K_DOWN) & (VEL_SCALE < 100):
        VEL_SCALE += 10
    if (key == pygame.K_RIGHT) & (G < 11):
        G += 1
    elif (key == pygame.K_LEFT) & (G > 1):
        G -= 1
```
This function adjusts the velocity scale and gravitational constant based on arrow key inputs.
