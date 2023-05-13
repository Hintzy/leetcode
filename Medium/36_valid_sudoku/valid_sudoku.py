

def valid_sudoku(board: list[list[str]]) -> bool:

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

board = [["5","3",".",".","7",".",".",".","."],
         ["6",".",".","1","9","5",".",".","."],
         [".","9","8",".",".",".",".","6","."],
         ["8",".",".",".","6",".",".",".","3"],
         ["4",".",".","8",".","3",".",".","1"],
         ["7",".",".",".","2",".",".",".","6"],
         [".","6",".",".",".",".","2","8","."],
         [".",".",".","4","1","9",".",".","5"],
         [".",".",".",".","8",".",".","7","9"]]

