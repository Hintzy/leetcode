cases = []

cases.append({
    'input': {'s': '', 't': 'word'}, 'output': False
})

cases.append({
    'input': {'s': 'word', 't': ''}, 'output': False
})

cases.append({
    'input': {'s': '', 't': ''}, 'output': True
})

cases.append({
    'input': {'s': 'w', 't': 'w'}, 'output': True
})

cases.append({
    'input': {'s': 'w', 't': ''}, 'output': False
})

cases.append({
    'input': {'s': 'stuff', 't': 'stuff'}, 'output': True
})

cases.append({
    'input': {'s': 'fstuff', 't': 'stuff'}, 'output': False
})

cases.append({
    'input': {'s': 'stuff', 't': 'stuf'}, 'output': False
})

cases.append({
    'input': {'s': 'great', 't': 'tearg'}, 'output': True
})

cases.append({
    'input': {'s': 'interview', 't': 'vewirteni'}, 'output': True
})

cases.append({
    'input': {'s': 'interview', 't': 'vewieni'}, 'output': False
})


def evaluate_cases(func, lst):
    for i, case in enumerate(lst):
        i += 1
        if func(**case['input']) == case['output']:
            print(f'Case {i} passed.')
        else:
            print(f'Case {i} failed.')