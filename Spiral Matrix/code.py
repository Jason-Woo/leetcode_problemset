class Solution(object):
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        m = len(matrix)
        if m == 0:
            return []
        n = len(matrix[0])
        l_border, r_border, u_border, d_border = 0, n - 1, 0, m - 1
        ans = []
        while l_border <= r_border and u_border <= d_border:
            for i in range(l_border, r_border + 1):
                ans.append(matrix[u_border][i])
            u_border += 1
            for i in range(u_border, d_border + 1):
                ans.append(matrix[i][r_border])
            r_border -= 1
            if u_border <= d_border:
                for i in range(r_border, l_border - 1, -1):
                    ans.append(matrix[d_border][i])
                d_border -= 1
            if l_border <= r_border:
                for i in range(d_border, u_border - 1, -1):
                    ans.append(matrix[i][l_border])
                l_border += 1
        return ans
