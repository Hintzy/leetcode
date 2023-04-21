cases = []

cases.append({
    'input': [2, 2, 1],
    'output': 1
})

cases.append({
    'input': [4, 4, 2, 2, 1],
    'output': 1
})

cases.append({
    'input': [4, 2, 1, 2, 4],
    'output': 1
})

cases.append({
    'input': [1, 2, 2, 4, 4],
    'output': 1
})

cases.append({
    'input': [1],
    'output': 1
})

# def run_test_cases(func, inp, outp):
#     for case in cases:
#         if func(case[inp]) == outp:

stuff = {
    'david': None,
    'michael': None,
    'hintz': None,
    'sean': None
}

for key in stuff.keys():
    print(key)