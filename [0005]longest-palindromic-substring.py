class Solution:
    def longestPalindrome(self, s: str) -> str:
        dp = [[False for i in range(len(s))] for i in range(len(s))]
        left = right = 0
        for i in range(len(s)):
            dp[i][i] = True
            for j in range(i):
                if (s[i] == s[i - j - 1] and (j == 0 or dp[i - 1][i - j])):
                   dp[i][i- j - 1] = True
                if(dp[i][i -j - 1]) and (j + 1) > (right - left):
                   right = i
                   left = i -j - 1
        return s[left:right + 1]
