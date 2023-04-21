cases = []

cases.append({
    'input': {
        'nums': []
    },
    'output': []
})

cases.append({
    'input': {
        'nums': [0]
    },
    'output': [0]
})

cases.append({
    'input': {
        'nums': [1]
    },
    'output': [1]
})

cases.append({
    'input': {
        'nums': [0, 1, 2, 3]
    },
    'output': [1, 2, 3, 0]
})

cases.append({
    'input': {
        'nums': [1, 2, 3, 0]
    },
    'output': [1, 2, 3, 0]
})

cases.append({
    'input': {
        'nums': [1, 0, 2, 0, 3, 0]
    },
    'output': [1, 2, 3, 0, 0, 0]
})

cases.append({
    'input': {
        'nums': [1, 0, 0, 0, 2, 0, 0, 3, 0]
    },
    'output': [1, 2, 3, 0, 0, 0, 0, 0, 0]
})

def evaluate_cases(func, lst):
    for i, case in enumerate(lst):
        i += 1
        if func(case['input']['nums']) == case['output']:
            print(f'Case {i} passed')
        else:
            print(f'Case {i} failed')
            print(f'Input: {case["input"]}')
            print(f'Output: {func(**case["input"])}')
            print(f'Expected Output: {case["output"]}')
