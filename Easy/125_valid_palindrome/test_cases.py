tests = []

tests.append({
    'input': {
        's': 'tests'
    },
    'output': False
})

tests.append({
    'input': {
        's': 'ses'
    },
    'output': True
})

tests.append({
    'input': {
        's': 'seses'
    },
    'output': True
})

tests.append({
    'input': {
        's': 'seses12'
    },
    'output': False
})

tests.append({
    'input': {
        's': "A man, a plan, a canal: Panama"
    },
    'output': True
})