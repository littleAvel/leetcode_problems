class Solution:
    def computePrefixSums(self, grid: List[List[str]], prefixX: List[List[int]], prefixY: List[List[int]]) -> None:
        rows = len(grid)
        cols = len(grid[0])
        
        for i in range(1, rows + 1):
            for j in range(1, cols + 1):
                prefixX[i][j] = prefixX[i-1][j] + prefixX[i][j-1] - prefixX[i-1][j-1] + (1 if grid[i-1][j-1] == 'X' else 0)
                prefixY[i][j] = prefixY[i-1][j] + prefixY[i][j-1] - prefixY[i-1][j-1] + (1 if grid[i-1][j-1] == 'Y' else 0)
    
    def isValidSubmatrix(self, xCount: int, yCount: int, topLeftChar: str) -> bool:
        return xCount == yCount and xCount > 0 and (topLeftChar == 'X' or topLeftChar == 'Y' or topLeftChar == '.')
    
    def countValidSubmatrices(self, prefixX: List[List[int]], prefixY: List[List[int]], grid: List[List[str]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        validCount = 0
        
        for i in range(1, rows + 1):
            for j in range(1, cols + 1):
                xCount = prefixX[i][j]
                yCount = prefixY[i][j]
                
                if self.isValidSubmatrix(xCount, yCount, grid[0][0]):
                    validCount += 1
        
        return validCount
    
    def numberOfSubmatrices(self, grid: List[List[str]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        
        # Initialize prefix sum arrays to count 'X' and 'Y'
        prefixCountX = [[0] * (cols + 1) for _ in range(rows + 1)]
        prefixCountY = [[0] * (cols + 1) for _ in range(rows + 1)]
        
        # Compute prefix sums
        self.computePrefixSums(grid, prefixCountX, prefixCountY)
        
        # Count valid submatrices
        return self.countValidSubmatrices(prefixCountX, prefixCountY, grid)
