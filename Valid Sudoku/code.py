class Solution(object):

    def isValidList(self, l):
        cnt = [0, 0, 0, 0, 0, 0, 0, 0, 0]
        for ele in l:
            if ele != '.':
                cnt[int(ele)] += 1
        for tmp in cnt:
            if tmp > 1:
                return False
        return True

    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        #Row
        for i in range(9):
            if not self.isValidList(board[i]):
                return False

        #col
        for i in range(9):
            l = [board[j][i] for j in range(9)]
            if not self.isValidList(l):
                return False

        #sub_box
        for i in range(3):
            for j in range(3):
                l = []
                for n in range(3):
                    for m in range(3):
                        l.append(board[n + 3 * i][m + 3 * j])
                if not self.isValidList(l):
                    return False
        return True
