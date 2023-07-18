cases = []

cases.append({
    'input': {
        'matrix':
            [[1, 2, 3, 4, 5],
             [6, 7, 8, 9, 10],
             [11, 12, 13, 14, 15],
             [16, 17, 18, 19, 20],
             [21, 22, 23, 24, 25]],
        'target': 5,
    },
    'output': True
})

cases.append({
    'input': {
        'matrix':
            [[1, 3, 5, 7],
             [10, 11, 16, 20],
             [23, 30, 34, 60]],
        'target': 3,
    },
    'output': True
})

cases.append({
    'input': {
        'matrix':
            [[1, 3]],
        'target': 3,
    },
    'output': True
})