tests = []

tests.append({
    'input': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10 ,11],
    'output': 10
})

tests.append({
    'input': [1, 2, 3, 11, 5, 6, 7, 8, 9, 10 ,11],
    'output': 10
})

tests.append({
    'input': [11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1],
    'output': 0
})

tests.append({
    'input': [],
    'output': 0
})

tests.append({
    'input': [0],
    'output': 0
})

tests.append({
    'input': [1, 10, 2, 11, 3, 12, 4, 14, 5, 19],
    'output': 18
})


def test_series(func, tests):
    for i, case in enumerate(tests):
        if func(case['input']) == case['output']:
            print(f'Test case #{i+1}: PASS')
        else:
            print(f'Test case #{i+1}: FAIL')