class Solution:
    def rotate(self, matrix) -> None:
        n = len(matrix)
        temp = [[0 for i in range(n)] for j in range(n)]
        for i in range(n):
            for j in range(n):
                temp[i][j] = matrix[j][i]
        for i in range(n):
            for j in range(n):
                matrix[i][j] = temp[i][n-j-1]