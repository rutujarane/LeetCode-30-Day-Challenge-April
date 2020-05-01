class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        if len(grid)<=0 or not grid:
            return 0
    
        # for row in range(len(grid)):
        #     for col in range(len(grid[0])):
        #         if row==0 and col==0:
        #             continue
        #         if row==0:
        #             grid[row][col] = grid[row][col] + grid[row][col-1]
        #         elif col==0:
        #             grid[row][col] = grid[row][col] + grid[row-1][col]
        #         else:
        #             grid[row][col] = grid[row][col] + min(grid[row-1][col], grid[row][col-1])
        
        dp=[[float('inf') for i in range(len(grid[0])+1) ] for j  in range(len(grid)+1)]
        
        dp[0][0] = 0
        dp[0][1] = 0
        dp[1][0] = 0
        for row in range(1,len(grid)+1):
            for col in range(1,len(grid[0])+1):
                dp[row][col] = grid[row-1][col-1] + min(dp[row-1][col],dp[row][col-1])
        
        return dp[-1][-1]