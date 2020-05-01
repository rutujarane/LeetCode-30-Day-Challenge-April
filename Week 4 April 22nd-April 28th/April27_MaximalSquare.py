class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        rows = len(matrix)
        if rows>0:
            cols = len(matrix[0])
        else:
            cols = 0
            
        dp = [0]*(cols+1)
        max_sqlen = 0
        prev = 0
        
        for i in range(1,rows+1):
            for j in range(1,cols+1):
                temp = dp[j]
                if matrix[i - 1][j - 1] == '1':
                    dp[j] = min(min(dp[j - 1], prev), dp[j]) + 1
                    max_sqlen = max(max_sqlen, dp[j])
                else:
                    dp[j] = 0;
                prev = temp;
                
        return max_sqlen * max_sqlen;