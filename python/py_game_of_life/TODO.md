# Game of life rules

Life’s simple, elegant rules give rise to astonishingly complex emergent behavior. It is played on a 2-D grid. Each square in the grid contains a cell, and each cell starts the game as either “alive” or “dead”. Play proceeds in rounds. During each round, each cell looks at its 8 immediate neighbors and counts up the number of them that are currently alive.

* Any live cell with 0 or 1 live neighbors becomes dead, because of underpopulation
* Any live cell with 2 or 3 live neighbors stays alive, because its neighborhood is just right
* Any live cell with more than 3 live neighbors becomes dead, because of overpopulation
* Any dead cell with exactly 3 live neighbors becomes alive, by reproduction


# Milestones

- [ ] Build a data structure to store the board state
- [ ] "Pretty-print" the board to the terminal
- [ ] Given a starting board state, calculate the next one
- [ ] Run the game forever

