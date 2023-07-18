from ds_templates import test_series
from test_cases import cases
from math import ceil


def minEatingSpeed(piles: list[int], h: int) -> int:

    def test_val(piles: list[int], k: int, h: int) -> (bool, int or None):
        time = 0
        for amt in piles:
            time += ceil(amt / k)
        if time <= h:
            return True, k
        return False, None

    l, r, min_hrs = 1, max(piles), float('inf')
    hrs = [i for i in range(l, r+1)]
    while l <= r:
        mid = (l + r) // 2
        it_works, time = test_val(piles, mid, h)
        if it_works:
            min_hrs = min(min_hrs, time)
            r = mid - 1
        else:
            l = mid + 1

    return min_hrs


test_series.test_series(minEatingSpeed, cases)
