cases = []

cases.append({
    'input': [0, 1, 2, 3, 4, 6],
    'output': 5
})

cases.append({
    'input': [0, 1, 3, 4]
    'output': 2
})

def evaluate_cases(func, lst):
    for i, case in enumerate(lst):
        if func(**case['input']) == case['output']:
            print(f'Case {i} passed')
        else:
            print(f'Case {i} failed')
