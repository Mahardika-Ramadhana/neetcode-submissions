class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        hrow, hcol, hbox = {}, {}, {}

        for i in range(9):
            for j in range(9):
                digit = board[i][j]

                if digit == ".":
                    continue

                if (i, digit) in hrow or (j, digit) in hcol or (i // 3, j // 3, digit) in hbox:
                    return False

                hrow[(i, digit)] = 1
                hcol[(j, digit)] = 1
                hbox[(i // 3, j // 3, digit)] = 1

        return True
