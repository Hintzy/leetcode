from ds_templates import test_series
from test_cases import tests


def valid_sudoku_1(board: list[list[str]]) -> bool:
    def valid_check(hm: dict, char):
        if not char.isdigit():
            return True
        char = int(char)
        hm[char] = hm.get(char, 0) + 1
        if hm[char] > 1:
            return False
        else:
            return True

    # search through each row for duplicates
    for row in board:
        temp = {}
        for num in row:
            if not valid_check(temp, num):
                return False

    # search through the columns for duplicates
    for column in range(9):
        temp = {}
        for row in board:
            if not valid_check(temp, row[column]):
                return False

    # search through the sectors for duplicates
    for x in range(0, 7, 3):
        for y in range(0, 7, 3):
            temp = {}
            for row in range(0 + x, 3 + x):
                for column in range(0 + y, 3 + y):
                    if not valid_check(temp, board[row][column]):
                        return False

    return True


# test_series.test_series(valid_sudoku_1, tests)


# __________________________________________________________________________________________
# Attempting to recreate Neetcode's method from memory (watched his video a few weeks ago)

def valid_sudoku_neet(board: list[list[str]]) -> bool:
    rows = [[] for _ in range(9)]
    cols = [[] for _ in range(9)]
    sects = {}

    for row in range(9):
        for col in range(9):
            num = board[row][col]
            if num == '.':
                continue
            elif num in rows[row] or num in cols[col] or num in sects.setdefault((row//3, col//3), []):
                return False
            else:
                rows[row].append(num)
                cols[col].append(num)
                sects[row//3, col//3].append(num)

    return True


test_series.test_series(valid_sudoku_neet, tests)
