from ds_templates import test_series
from test_cases import cases

# brute force iteration of every number

def dailyTemperatures(temps: list[int]) -> list[int]:
    res = []
    for i in range(len(temps)-1):
        x = i + 1
        while temps[i] >= temps[x] and x < len(temps)-1:
            x += 1
        if temps[x] > temps[i]:
            res.append(x-i)
        else:
            res.append(0)
    res.append(0)

    return res

# test_series.test_series(dailyTemperatures, cases)

# approach using a stack
def dailyTemperatures_stack(temps: list[int]) -> list[int]:
    res = [0] * len(temps)
    stack = []  # pair of (temp, index)
    for i, t in enumerate(temps):
        while stack and t > stack[-1][0]:
            currT, currInd = stack.pop()
            res[currInd] = i - currInd
        stack.append((t, i))
    return res

temps_1 = [0, 1, 2, 3, 4, 5]
print(dailyTemperatures_stack(temps_1))