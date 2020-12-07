from functools import wraps

def test_score(test_fn, unpack=False):
    inputs, outputs = test_fn()
    @wraps(test_fn)
    def inner(fn):
        score = 0
        for i, o in zip(inputs, outputs):
            try:
                if unpack:
                    score += fn(*i) == o
                else:
                    score += fn(i) == o
            except:
                pass
        return score / len(inputs)
    return inner


@test_score
def test_coins():
    inputs = [0, 1, 23, 75, 99]
    outputs = [
        [0, 0, 0, 0, 0, 0], 
        [0, 0, 0, 0, 0, 1], 
        [0, 1, 0, 0, 1, 1], 
        [1, 1, 0, 1, 0, 0], 
        [1, 2, 0, 1, 2, 0]]
    return inputs, outputs
       

@test_score
def test_decipher():
    inputs = ['xxc01', 'cc01', '', '010101c01', 'PPP']
    outputs = [True, False, False, True, False]
    return inputs, outputs


@test_score
def test_dragon():
    inputs = [0, 1, 2, 4]
    outputs = [
        'F', 
        'FRFR', 
        'FRFRRLFLFR', 
        'FRFRRLFLFRRLFRFRLLFLFRRLFRFRRLFLFRLLFRFRLLFLFR'
    ]
    return inputs, outputs


def test_moving_average():
    inputs = [
        ([1, 2, 3], 4),
        ([1, 1, 3, 3, 5, 5], 2),
        ([1, 2, 3, 4], 4),
        ([10, 20, 30, 40, 50, 60, 70, 80], 3)
    ]
    outputs = [
        None, 
        [1.0, 2.0, 3.0, 4.0, 5.0], 
        [2.5], 
        [20.0, 30.0, 40.0, 50.0, 60.0, 70.0]
    ]
    return inputs, outputs
test_moving_average = test_score(test_moving_average, unpack=True)


@test_score
def test_only_homogenous():
    inputs = [
        [[], [1, 2, 3]],
        [[1, 2], ['1', '2'], [1, '2']],
        [[1], ['2'], [1, 2, 3, 4, 5, '6']],
        [[1, 2], ['1', '2']],
    ]
    outputs = [
        [[1, 2, 3]],
        [[1, 2], ['1', '2']],
        [[1], ['2']],
        [[1, 2], ['1', '2']],
    ]
    return inputs, outputs


@test_score
def test_who_win():
    board_1 = [['o', ' ', ' '],
               ['x', 'x', 'x'],
               [' ', 'o', ' ']]
    board_2 = [['x', ' ', ' '],
               ['x', 'o', ' '],
               ['x', 'o', ' ']]
    board_3 = [['o', ' ', ' '],
               ['x', 'o', 'x'],
               [' ', 'x', 'o']]
    board_4 = [[' ', ' ', ' '],
               ['x', 'o', ' '],
               ['x', 'o', ' ']]
    inputs = [board_1, board_2, board_3, board_4]
    outputs = ['x', 'x', 'o', 'd']
    return inputs, outputs