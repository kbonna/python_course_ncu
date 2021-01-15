def create_grid(n_rows, n_columns):
    """Creates grid with n_rows and n_columns filled with zeros.

    Args:
        n_rows (int):
            Number of grid rows.
        n_columns (int):
            Number of grid columns.

    Returns:
        2D array representing grid filled with zeros.
    """
    return [[0 for n in range(n_columns)] for m in range(n_rows)]


def convert_to_string(state):
    """Converts state to string.

    Args:
        state (list of lists):
            State of the game.

    Returns:
        String representation of the state.
    """
    n_columns = len(state[0])
    n_rows = len(state)

    out = "=" * (n_columns + 2) + "\n"

    for x in range(n_rows):
        out += "|"
        for y in range(n_columns):
            if state[x][y] == 1:
                out += "#"
            elif state[x][y] == 0:
                out += " "
            else:
                raise ValueError
        out += "|\n"

    out += "=" * (n_columns + 2)
    return out


def display(state):
    """Print string representation of the state."""
    s = convert_to_string(state)
    print(s)