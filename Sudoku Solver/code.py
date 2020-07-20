class Solution(object):
    def findempty(self):
        for i in range(9):
            for j in range(9):
                if self.board[i][j] == '.':
                    return i, j
        return -1, -1

    def valid_row(self, row, num):
        for n in range(9):
            if self.board[row][n] == num:
                return False
        return True

    def valid_col(self, col, num):
        for n in range(9):
            if self.board[n][col] == num:
                return False
        return True

    def valid_block(self, row, col, num):
        i, j = row // 3, col // 3
        for m in range(3):
            for n in range(3):
                if self.board[i * 3 + m][j * 3 + n] == num:
                    return False
        return True

    def solver(self):
        row, col = self.findempty()
        if row == -1 and col == -1:
            return True
        for num in ['1', '2', '3', '4', '5', '6', '7', '8', '9']:
            if self.valid_row(row, num) and self.valid_col(col, num) and self.valid_block(row, col, num):
                self.board[row][col] = num
                if self.solver():
                    return True
                self.board[row][col] = '.'
        return False

    def solveSudoku(self, board):
        self.board = board
        """
        :type board: List[List[str]]
        :rtype: None Do not return anything, modify board in-place instead.
        """
        self.solver()
        return self.board
