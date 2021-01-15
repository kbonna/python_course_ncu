import unittest
from functions import create_grid, convert_to_string


class TestGameOfLifeFunctions(unittest.TestCase):
    def test_create_grid(self):
        grid = create_grid(2, 2)
        self.assertEqual(grid, [[0, 0], [0, 0]])
        grid2 = create_grid(1, 1)
        self.assertEqual(grid2, [[0]])

    def test_create_grid_reference(self):
        grid = create_grid(n_rows=2, n_columns=2)
        grid[0][0] = 1
        self.assertEqual(grid, [[1, 0], [0, 0]])

    def test_convert_to_string(self):
        state = [[1, 1], [1, 1]]
        st = "====\n|##|\n|##|\n===="
        self.assertEqual(convert_to_string(state), st)
        state = [[0]]
        st = "===\n| |\n==="
        self.assertEqual(convert_to_string(state), st)
        state = [[0, 0, 0, 1], [0, 0, 1, 0], [0, 0, 1, 0]]
        st = "======\n|   #|\n|  # |\n|  # |\n======"
        self.assertEqual(convert_to_string(state), st)

    def test_get_neighbors(self):
        state = [[0, 0, 0, 1], [0, 0, 1, 0], [0, 0, 1, 0]]
        r = 2
        self.assertEqual(get_neighbors(state, 2, 3), r)
        state = [[0, 0, 0, 1], [0, 0, 1, 1], [0, 0, 1, 1]]
        r = 2
        self.assertEqual(get_neighbors(state, 0, 3), r)
        state = [[0, 0, 0, 1], [0, 0, 1, 0], [0, 0, 1, 0]]
        r = 3
        self.assertEqual(get_neighbors(state, 1, 3), r)


unittest.main()