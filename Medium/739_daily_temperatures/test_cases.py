cases = []

cases.append({
    'input': {
        'temps': [73, 74, 75, 71, 69, 72, 76, 73],
    },
    'output': [1,1,4,2,1,1,0,0]
})

cases.append({
    'input': {
        'temps': [30,40,50,60],
    },
    'output': [1,1,1,0]
})

cases.append({
    'input': {
        'temps': [30,60,90],
    },
    'output': [1,1,0]
})