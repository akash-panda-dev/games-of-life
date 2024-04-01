import curses
import random
import time
from collections import Counter
from enum import Enum

import pygame


class CellState(Enum):
    ALIVE = 1
    DEAD = 0


class Board:
    def __init__(self, width, height, cell_size) -> None:
        self.width = width
        self.height = height
        self.cell_size = cell_size
        self.cells = self.dead_state()

    def dead_state(self):
        return [[CellState.DEAD for _ in range(self.width)] for _ in range(self.height)]

    def random_state(self):
        self.cells = [
            [random.choice(list(CellState)) for _ in range(self.width)]
            for _ in range(self.height)
        ]

    def render(self, screen):
        screen.fill((255, 255, 255))  # Clear the screen
        for y, row in enumerate(self.cells):
            for x, cell in enumerate(row):
                if cell == CellState.ALIVE:
                    pygame.draw.rect(
                        screen,
                        (0, 0, 0),
                        (
                            x * self.cell_size,
                            y * self.cell_size,
                            self.cell_size,
                            self.cell_size,
                        ),
                    )
        pygame.display.flip()  # Update the display

    def next_board_state(self):
        # 1. Any live cell with 0 or 1 live neighbors becomes dead, because of underpopulation
        # 2. Any live cell with 2 or 3 live neighbors stays alive, because its neighborhood is just right
        # 3. Any live cell with more than 3 live neighbors becomes dead, because of overpopulation
        # 4. Any dead cell with exactly 3 live neighbors becomes alive, by reproduction
        next_cells = self.dead_state()

        for h in range(self.height):
            for w in range(self.width):
                neighbors = self.get_neighbors_life_state_count(w, h)
                if self.cells[h][w] == CellState.ALIVE:
                    if neighbors[CellState.ALIVE] in [2, 3]:
                        next_cells[h][w] = CellState.ALIVE
                else:
                    if neighbors[CellState.ALIVE] == 3:
                        next_cells[h][w] = CellState.ALIVE

        self.cells = next_cells

    def get_neighbors_life_state_count(self, w, h):
        delta_w = [-1, -1, 0, 1, 1, 1, 0, -1]
        delta_h = [0, -1, -1, -1, 0, 1, 1, 1]

        life_count = []

        for i in range(len(delta_w)):
            nw = w + delta_w[i]
            nh = h + delta_h[i]
            if (0 <= nw <= (self.width - 1)) and (0 <= nh <= (self.height - 1)):
                life_count.append(self.cells[nh][nw])

        return Counter(life_count)


def main():
    cell_size = 30

    with open(
        "/Users/akashpanda/Documents/PandaWS/games-of-life/games_of_life/python/py_game_of_life/glider.txt",
        "r",
    ) as f:
        lines = f.read().split("\n")
        height = len(lines)
        width = len(lines[0].strip())

        board = Board(width, height, cell_size)

        for h, line in enumerate(lines):
            for w, cell in enumerate(line.strip()):
                if cell == "O":
                    board.cells[h][w] = CellState.ALIVE

    pygame.init()
    screen = pygame.display.set_mode((width * cell_size, height * cell_size))
    pygame.display.set_caption("Game of Life")

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        board.render(screen)
        board.next_board_state()
        time.sleep(0.1)

    pygame.quit()


if __name__ == "__main__":
    main()
