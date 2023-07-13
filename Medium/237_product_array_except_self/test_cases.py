tests = []


# Case 1 -
tests.append({
    'input': {
        'nums': [10, 0]
    },
    'output': [0, 10]
})

# Case 2 -
tests.append({
    'input': {
        'nums': [10, 5]
    },
    'output': [5, 10]
})

# Case 3 -
tests.append({
    'input': {
        'nums': [1, 3, 7]
    },
    'output': [21, 7, 3]
})

# Case 4 -
tests.append({
    'input': {
        'nums': [1, 0, 7]
    },
    'output': [0, 7, 0]
})

# Case 5 -
tests.append({
    'input': {
        'nums': [1, 0, 7, 1, 1, 1, 1, 1, 1]
    },
    'output': [0, 7, 0, 0, 0, 0, 0, 0, 0]
})


