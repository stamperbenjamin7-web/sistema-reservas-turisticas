import numpy as np
import time
import os


def print_grid(grid):
    os.system("cls" if os.name == "nt" else "clear")
    for row in grid:
        print("".join(["⬛" if cell else "⬜" for cell in row]))


def game_of_life(grid, generations):
    for gen in range(generations):
        print(f"Generation {gen + 1}")
        print_grid(grid)
        next_grid = np.zeros(grid.shape, dtype=int)
        for i in range(grid.shape[0]):
            for j in range(grid.shape[1]):
                # Contar vecinos vivos
                neighbors = np.sum(
                    grid[max(0, i-1):i+2, max(0, j-1):j+2]) - grid[i, j]
                # Aplicar reglas
                if grid[i, j] == 1 and (neighbors == 2 or neighbors == 3):
                    next_grid[i, j] = 1  # Celda viva sobrevive
                elif grid[i, j] == 0 and neighbors == 3:
                    next_grid[i, j] = 1  # Celda muerta revive
        grid = next_grid
        time.sleep(0.5)


# Configuración inicial
rows, cols = 10, 10
# Generar un estado inicial aleatorio
grid = np.random.randint(2, size=(rows, cols))

# Ejecutar el Juego de la Vida
game_of_life(grid, generations=20)