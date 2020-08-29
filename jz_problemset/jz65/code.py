class Solution:
    def hasPath(self, matrix, rows, cols, path):
        # write code here
        for i in range(rows):
            for j in range(cols):
                if matrix[i * cols + j] == path[0]:
                    if self.findpath(i, j, path[1:], list(matrix), rows, cols):
                        return True
        return False

    def findpath(self, i, j, path, matrix, rows, cols):
        if i < 0 or j < 0 or i > rows or j > cols:
            return False
        if not path:
            return True
        matrix[i * cols + j] = None
        if i + 1 < rows and matrix[(i + 1) * cols + j] == path[0]:
            if self.findpath(i + 1, j, path[1:], matrix, rows, cols):
                return True
        if j + 1 < cols and matrix[i * cols + j + 1] == path[0]:
            if self.findpath(i, j + 1, path[1:], matrix, rows, cols):
                return True
        if i - 1 >= 0 and matrix[(i - 1) * cols + j] == path[0]:
            if self.findpath(i - 1, j, path[1:], matrix, rows, cols):
                return True
        if j - 1 >= 0 and matrix[i * cols + j - 1] == path[0]:
            if self.findpath(i, j - 1, path[1:], matrix, rows, cols):
                return True
        else:
            return False