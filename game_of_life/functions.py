def create_grid(n_rows=10, n_columns=20):
    """Create empty 2D array filled with zeros.

    Args:
        n_rows (int):
            Number of rows.
        n_columns (int):
            Number of columns

    Returns:
        2D array filled with zeros.
    """
    grid = []
    for i in range(n_rows):
        grid.append([0] * n_columns)
    return grid


def convert_to_string(state):
    """Convert game state to printable string representation.

    Args:
        state (list of lists):
            State of the game.

    Returns:
        Printable string representation of the state.
    """
    n_rows = len(state)
    n_columns = len(state[0])
    s = ""
    s += "=" * (n_columns + 2) + "\n"
    for row in state:
        s += "|"
        for el in row:
            if el == 0:
                s += " "
            else:
                s += "#"
        s += "|\n"
    s += "=" * (n_columns + 2)
    return s


def display(state):
    """Print state representation to the terminal.

    Args:
        state (list of lists):
            State of the game.

    Returns:
        None
    """
    print(convert_to_string(state))


def get_neighbors(state, i, j):
    """Get number of live neighbors of cell i, j for given state.

    Args:
        state (list of lists):
            State of the game.
        i (int):
            Row number.
        j (int):
            Column number.

    Returns:
        Number of live neighbors of a cell.
    """
    n_rows = len(state)
    n_columns = len(state[0])
    neighbors = []
    for di in (-1, 0, 1):
        for dj in (-1, 0, 1):
            if di != 0 or dj != 0:
                if i + di >= 0 and i + di < n_rows and j + dj >= 0 and j + dj < n_columns:
                    neighbors.append(state[i + di][j + dj])
    return sum(neighbors)


def get_next_status(current, neighbors):
    """Determine next status of a cell given its current status and current neighbors.

    Args:
        current (int):
            Current cell status. Either 1 for alive or 0 for dead.
        neighbors (int):
            Number of live neighbors of a cell.

    Returns:
        Next cell status.
    """
    if current == 0 and neighbors == 3:
        return 1
    elif current == 1 and (neighbors == 2 or neighbors == 3):
        return 1
    else:
        return 0


def get_next_state(state):
    """Run one step of game of life evolution. Return new state given current state.

    Args:
        state (list of lists):
            State of the game.

    Returns:
        Next state of the game.
    """
    n_rows = len(state)
    n_columns = len(state[0])

    # Create an empty state
    next_state = create_grid(n_rows, n_columns)

    for i in range(n_rows):
        for j in range(n_columns):
            next_state[i][j] = get_next_status(state[i][j], get_neighbors(state, i, j))

    return next_state


def load_state_from_file(filename):
    """
    Load state from a textfile.

    Args:
        filename (str):
            Filename storing game state. Each row of the board should be on separate line. Living
            cells should be represented as # while dead cells should be represented as space.

    Returns:
        Loaded state.
    """
    with open(filename, "r") as f:
        s = f.read().splitlines()

    state = []
    for line in s:
        state.append([int(digit) for digit in line.replace("#", "1").replace("-", "0")])

    return state