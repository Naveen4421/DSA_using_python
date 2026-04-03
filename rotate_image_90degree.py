def rotate(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """
        n=len(matrix)
        result=[]
        for i in range(n):
            row=[]
            for j in range(n-1,-1,-1):
                row.append(matrix[j][i])
            result.append(row)
        for i in range(n):
            for j in range(n):
                matrix[i][j]=result[i][j]

        return matrix
