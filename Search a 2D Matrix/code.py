class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        curr_col, curr_row = 0, 0
        if target < matrix[0][0]:
            return False
        while curr_row < len(matrix):
            curr = matrix[curr_row][0]
            if curr < target:
                curr_row += 1
            elif curr > target:
                break
            else:
                return True
        curr_row -= 1
        while curr_col < len(matrix[0]):
            curr = matrix[curr_row][curr_col]
            if curr < target:
                curr_col += 1
            elif curr == target:
                return True
            else:
                return False
        return False
