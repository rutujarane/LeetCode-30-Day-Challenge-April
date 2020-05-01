class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        if text1 == "" or text2 == "" or len(text1) == 0 or len(text2) == 0:
            return 0
        
        m = len(text1)
        n = len(text2)
        dp = []
        d = []
        for i in range(m+1):
            for j in range(n+1):
                d.append(0)
            dp.append(d)
            d = []
            
        for i in range(m,-1,-1):
            for j in range(n,-1,-1):
                if i == m or j == n:
                    dp[i][j] = 0;
                elif text1[i] == text2[j]:
                    dp[i][j] = dp[i + 1][j + 1] + 1;
                else:
                    dp[i][j] = max(dp[i + 1][j], dp[i][j + 1]);
        
        return dp[0][0];