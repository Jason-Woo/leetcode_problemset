class Solution(object):
    def generateMatrix(self, n):
        """
        :type n: int
        :rtype: List[List[int]]
        """
        matrix = [[-1 for _ in range(n)] for _ in range(n)]
        l_border, r_border, u_border, d_border = 0, n - 1, 0, n - 1
        num = 1
        while l_border <= r_border and u_border <= d_border:
            for i in range(l_border, r_border + 1):
                matrix[u_border][i] = num
                num += 1
            u_border += 1
            for i in range(u_border, d_border + 1):
                matrix[i][r_border] = num
                num += 1
            r_border -= 1
            if u_border <= d_border:
                for i in range(r_border, l_border - 1, -1):
                    matrix[d_border][i] = num
                    num += 1
                d_border -= 1
            if l_border <= r_border:
                for i in range(d_border, u_border - 1, -1):
                    matrix[i][l_border] = num
                    num += 1
                l_border += 1
        return matrix
