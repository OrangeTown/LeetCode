class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        dp = [[False for i in range(len(s)+1)] for j in range(len(p)+1)]
        dp[0][0] = True
        for i in range(len(s)+1):
            for j in range(1, len(p)+1):
                if(p[j-1] == '*'):
                    dp[j][i] = ((j>=2) and dp[j-2][i]) or ((i>=1) and (s[i-1]==p[j-2] or p[j-2]=='.') and dp[j][i-1])
                else:
                    dp[j][i] = (i>=1) and (s[i-1]==p[j-1] or p[j-1]=='.') and dp[j-1][i-1]
        return dp[len(p)][len(s)]
