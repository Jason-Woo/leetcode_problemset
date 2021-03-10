class Solution(object):
    def exist(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """
        m, n = len(board), len(board[0])
        for i in range(m):
            for j in range(n):
                if board[i][j] == word[0]:
                    if helper(board, word[1:], i, j):
                        return True
        return False


def helper(board, word, i, j):
    if len(word) == 0:
        return True
    find = False
    myboard = board
    myboard[i][j] = "#"
    if i > 0 and board[i - 1][j] == word[0]:
        find = find and helper(myboard, word[1:], i - 1, j)
    if i < len(board) and board[i + 1][j] == word[0]:
        find = find and helper(myboard, word[1:], i + 1, j)
    if j > 0 and board[i][j - 1] == word[0]:
        find = find and helper(myboard, word[1:], i, j - 1)
    if j < len(board) and board[i][j + 1] == word[0]:
        find = find and helper(myboard, word[1:], i, j + 1)
    return find
