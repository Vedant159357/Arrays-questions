class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        
        #first i will transpose the matrix
        n = len(matrix)
        for i in range(n-1):
            for j in range(i+1,n):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

        #now reverse the rows
        for i in range(n):
            matrix[i].reverse()
