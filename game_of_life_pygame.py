import random
import time
import os
import pygame
from pygame.locals import QUIT

def initialize_grid(rows, cols, density=0.2):
    """Initialize the grid with random live cells."""
    grid = [[random.choice([0, 1]) for _ in range(cols)] for _ in range(rows)]
    return grid

def draw_grid(screen, grid, cell_size):
    """Draw the current state of the grid."""
    for row in range(len(grid)):
        for col in range(len(grid[0])):
            color = (255, 255, 255) if grid[row][col] else (0, 0, 0)
            pygame.draw.rect(screen, color, (col * cell_size, row * cell_size, cell_size, cell_size))

def count_live_neighbors(grid, row, col):
    """Count the number of live neighbors for a given cell."""
    live_neighbors = 0
    rows, cols = len(grid), len(grid[0])

    for i in range(-1, 2):
        for j in range(-1, 2):
            if i == 0 and j == 0:
                continue

            neighbor_row, neighbor_col = row + i, col + j
            if 0 <= neighbor_row < rows and 0 <= neighbor_col < cols:
                live_neighbors += grid[neighbor_row][neighbor_col]

    return live_neighbors

def update_grid(grid):
    """Update the grid based on the rules of the Game of Life."""
    rows, cols = len(grid), len(grid[0])
    new_grid = [[0] * cols for _ in range(rows)]

    for row in range(rows):
        for col in range(cols):
            live_neighbors = count_live_neighbors(grid, row, col)

            if grid[row][col] == 1:
                # Cell is alive
                if live_neighbors < 2 or live_neighbors > 3:
                    new_grid[row][col] = 0  # Die due to underpopulation or overpopulation
                else:
                    new_grid[row][col] = 1  # Survive
            else:
                # Cell is dead
                if live_neighbors == 3:
                    new_grid[row][col] = 1  # Reproduction

    return new_grid

def clear_screen():
    """Clear the terminal screen."""
    os.system('cls' if os.name == 'nt' else 'clear')

# def play_sound():
#     """Play a sound after each iteration/generation."""
#     pygame.mixer.music.load("your_sound_file.mp3")  
#     pygame.mixer.music.play()

def main(rows, cols, generations, density=0.2, delay=0.5, cell_size=20):
    """Run the Game of Life simulation using Pygame with sound."""
    pygame.init()
    screen = pygame.display.set_mode((cols * cell_size, rows * cell_size))
    pygame.display.set_caption("Game of Life")

    pygame.mixer.init()  

    grid = initialize_grid(rows, cols, density)

    for generation in range(generations):
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                exit()

        clear_screen()
        print(f"Generation {generation + 1}:\n")
        draw_grid(screen, grid, cell_size)
        pygame.display.flip()
        # play_sound()
        time.sleep(delay)

        grid = update_grid(grid)

    pygame.mixer.quit()  

if __name__ == "__main__":
    
    rows, cols = 20, 40
    generations = 50
    density = 0.2  
    delay = 0.2   
    cell_size = 20

    
    main(rows, cols, generations, density, delay, cell_size)
