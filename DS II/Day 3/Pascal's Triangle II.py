class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        result = []
        
        rows = {}
        
        
        rows[0] = [1]
        rows[1] = [1, 1]
        
        if rowIndex == 0:
            return rows[0]
        
        if rowIndex == 1:
            return rows[1]
        
        
        for row in range(2, rowIndex + 1):
            n = row + 1       
            rows[row] = [None for i in range(n)]
            rows[row][0] = 1
            rows[row][row] = 1

            for i in range(1, row):
                rows[row][i] = rows[row - 1][i - 1] + rows[row - 1][i]

        return rows[rowIndex]