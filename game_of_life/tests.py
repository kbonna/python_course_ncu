import unittest

from functions import (
    create_grid,
    convert_to_string,
    get_neighbors,
    get_next_status,
    get_next_state,
    load_state_from_file,
)


class TestGameOfLifeFunctions(unittest.TestCase):
    def test_create_grid(self):
        grid = create_grid(n_rows=2, n_columns=2)
        self.assertEqual(grid, [[0, 0], [0, 0]])

        grid[0][0] = 1
        self.assertEqual(grid, [[1, 0], [0, 0]])

        grid = create_grid(n_rows=3, n_columns=7)
        self.assertEqual(
            grid, [[0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0]]
        )

    def test_convert_to_string(self):
        state = [[1, 0], [0, 0]]
        state_string = convert_to_string(state)
        self.assertEqual(state_string, "====\n|# |\n|  |\n====")

        state = [[1, 1, 1, 1]]
        state_string = convert_to_string(state)
        self.assertEqual(state_string, "======\n|####|\n======")

    def test_get_neighbors(self):
        state = [[1, 0], [0, 0]]
        neighbors = get_neighbors(state, 0, 0)
        self.assertEqual(neighbors, 0)

        neighbors = get_neighbors(state, 0, 1)
        self.assertEqual(neighbors, 1)

        state = [
            [0, 0, 0, 0, 0],
            [0, 0, 0, 1, 0],
            [0, 0, 1, 1, 0],
            [0, 0, 0, 1, 1],
            [0, 1, 0, 1, 0],
        ]
        neighbors = get_neighbors(state, 2, 2)
        self.assertEqual(neighbors, 3)

        neighbors = get_neighbors(state, 4, 4)
        self.assertEqual(neighbors, 3)

    def test_get_next_status(self):
        # Dead cell with exactly 3 living neighbors is comes alive
        current = 0
        neighbors = 3
        new = get_next_status(current, neighbors)
        self.assertEqual(new, 1)

        # Dead cell with less than 3 living neighbors is still dead
        current = 0
        neighbors = 2
        new = get_next_status(current, neighbors)
        self.assertEqual(new, 0)

        # Dead cell with more than 3 living neighbors is still dead
        current = 0
        neighbors = 4
        new = get_next_status(current, neighbors)
        self.assertEqual(new, 0)

        # Living cell with 2 living neighbors survive
        current = 1
        neighbors = 2
        new = get_next_status(current, neighbors)
        self.assertEqual(new, 1)

        # Living cell with 3 living neighbors survive
        current = 1
        neighbors = 3
        new = get_next_status(current, neighbors)
        self.assertEqual(new, 1)

        # Living cell with more than 3 living neighbors dies
        current = 1
        neighbors = 4
        new = get_next_status(current, neighbors)
        self.assertEqual(new, 0)

    def test_next_state(self):
        state = [
            [1, 0, 0, 0, 0],
            [0, 1, 1, 0, 0],
            [1, 1, 0, 0, 0],
            [0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0],
        ]
        next_state = get_next_state(state)
        self.assertEqual(
            next_state,
            [
                [0, 1, 0, 0, 0],
                [0, 0, 1, 0, 0],
                [1, 1, 1, 0, 0],
                [0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0],
            ],
        )

    def test_load_state_from_file(self):
        state = load_state_from_file("states/state1.txt")
        self.assertEqual(state, [[1, 1, 1], [0, 0, 1], [1, 0, 0]])

        state = load_state_from_file("states/state2.txt")
        self.assertEqual(state, [[1]])


if __name__ == "__main__":
    unittest.main()