from py_game_of_life.main import Board, CellState
import unittest

class TestBoard(unittest.TestCase):
    def test_get_neighbors_life_state_count(self):
        board = Board(5, 5)
        board.cells = [
            [CellState.DEAD, CellState.ALIVE, CellState.DEAD, CellState.ALIVE, CellState.DEAD], 
            [CellState.ALIVE, CellState.ALIVE, CellState.DEAD, CellState.DEAD, CellState.ALIVE],
            [CellState.DEAD, CellState.DEAD, CellState.ALIVE, CellState.DEAD, CellState.DEAD],
            [CellState.ALIVE, CellState.DEAD, CellState.DEAD, CellState.ALIVE, CellState.ALIVE],
            [CellState.DEAD, CellState.ALIVE, CellState.DEAD, CellState.ALIVE, CellState.DEAD]
        ]

        # Test cell in the middle
        count = board.get_neighbors_life_state_count(2, 2)
        print(count)
        assert count[CellState.ALIVE] == 2
        assert count[CellState.DEAD] == 6

        # Test cell on the top edge 
        count = board.get_neighbors_life_state_count(1, 0) 
        assert count[CellState.ALIVE] == 2
        assert count[CellState.DEAD] == 3

        # Test cell on the bottom edge
        count = board.get_neighbors_life_state_count(3, 4)
        assert count[CellState.ALIVE] == 2 
        assert count[CellState.DEAD] == 3

        # Test cell on the left edge
        count = board.get_neighbors_life_state_count(0, 3)
        assert count[CellState.ALIVE] == 1
        assert count[CellState.DEAD] == 4

        # Test cell on the right edge  
        count = board.get_neighbors_life_state_count(4, 1)
        assert count[CellState.ALIVE] == 1
        assert count[CellState.DEAD] == 4


if __name__ == "__main__":
    unittest.main()