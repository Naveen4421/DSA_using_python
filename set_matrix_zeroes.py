class Solution(object):
    def setZeroes(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """
        m=len(matrix)
        n=len(matrix[0])
        rows_to_zero=set()
        column_to_zero=set()

        #find out the zeroes row and column number
        for i in range(m):
            for j in range(n):
                if matrix[i][j]==0:
                    rows_to_zero.add(i)  # set function to store zeroes which is not repeated 
                    column_to_zero.add(j)
        # make rows and columns zero
        for i in range(m):
            for j in range(n):
                if i in rows_to_zero or j in column_to_zero:
                    matrix[i][j]=0
        return matrix

        
