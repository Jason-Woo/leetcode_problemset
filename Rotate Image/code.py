class Solution(object):
    def rotate(self, matrix):
        n = len(matrix)
        matrix.reverse()
        for i in range(n):
            for j in range(i + 1, n):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]


'''
1|2|3                 7|8|9             7|4|1
4|5|6  --reverse-->   4|5|6  --ans-->   8|5|2
7|8|9                 1|2|3             9|6|3
'''
