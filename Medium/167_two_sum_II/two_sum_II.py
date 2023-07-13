from ds_templates import test_series
from test_cases import cases


def twoSum(numbers: list[int], target: int) -> list[int]:
    i, j = 0, len(numbers) - 1
    while i < j:
        summ = numbers[i] + numbers[j]
        if summ == target:
            return [i+1, j+1]
        elif summ > target:
            j -= 1
        else:
            i += 1
    return False


test_series.test_series(twoSum, cases)
