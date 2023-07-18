# from ds_templates import test_series
from test_cases import cases


def searchMatrix(matrix: list[list[int]], target: int) -> bool:

    def lst_lvl1_search(matrix: list[list[int]], target: int) -> int or None:
        l, r = 0, len(matrix) - 1
        while l <= r:
            mid_ind = int((l + r) // 2)
            mid = matrix[mid_ind]
            if target < mid[0]:
                r = mid_ind - 1
            elif target > mid[-1]:
                l = mid_ind + 1
            else:
                return mid_ind
        return None

    def lst_lvl2_search(lst: list[int], target: int) -> bool:
        l, r = 0, len(lst) - 1
        mid = (l + r) // 2
        if lst[mid] == target:
            return True
        while l <= r:
            mid = (l + r) // 2
            if target > lst[mid]:
                l = mid + 1
            elif target < lst[mid]:
                r = mid - 1
            else:
                return True
        return False

    res = lst_lvl1_search(matrix, target)
    if res is None:
        return False
    return lst_lvl2_search(matrix[res], target)


matr = [[2, 3, 4, 5],
        [6, 7, 8, 9, 10],
        [11, 12, 13, 14, 15],
        [16, 17, 18, 19, 20],
        [21, 22, 23, 24, 25]]
tar = 5

print(searchMatrix(matr, tar))
