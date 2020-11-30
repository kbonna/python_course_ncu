def test_coins(fn):
    score = 0
    inputs = [0, 1, 23, 75, 99]
    outputs = [
        [0, 0, 0, 0, 0, 0], 
        [0, 0, 0, 0, 0, 1], 
        [0, 1, 0, 0, 1, 1], 
        [1, 1, 0, 1, 0, 0], 
        [1, 2, 0, 1, 2, 0]]
    for i, o in zip(inputs, outputs):
        try:
            score += fn(i) == o
        except:
            pass
    return score / len(inputs)
        
def test_decipher(fn):
    score = 0
    inputs = ['xxc01', 'cc01', '', '010101c01', 'PPP']
    outputs = [True, False, False, True, False]
    for i, o in zip(inputs, outputs):
        try:
            score += fn(i) == o
        except:
            pass
    return score / len(inputs)