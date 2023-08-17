cases = []


# Case 1 -
cases.append({
    'input': {
        's1': 'aba',
        's2': 'baa'
    },
    'output': True
})

# Case 2 -
cases.append({
    'input': {
        's1': 'aba',
        's2': 'baask'
    },
    'output': True
})

# Case 3 -
cases.append({
    'input': {
        's1': 'aba',
        's2': 'baska'
    },
    'output': False
})

# Case 4 -
cases.append({
    'input': {
        's1': 'aa',
        's2': 'baska'
    },
    'output': False
})

# Case 5 -
cases.append({
    'input': {
        's1': 'adda',
        's2': 'adskad'
    },
    'output': False
})

# Case 6 -
cases.append({
    'input': {
        's1': 'adda',
        's2': 'ddaasdkjflad'
    },
    'output': True
})

# Case 7 -
cases.append({
    'input': {
        's1': 'adda',
        's2': 'sdkjddaaflad'
    },
    'output': True
})

# Case 8 -
cases.append({
    'input': {
        's1': 'adc',
        's2': 'dcda'
    },
    'output': True
})



