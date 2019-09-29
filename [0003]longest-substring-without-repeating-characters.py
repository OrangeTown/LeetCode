class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        dict_s = {}
        i, ans = 0, 0
        for j in range(len(s)):
            if s[j] in dict_s:
                i = max(dict_s[s[j]], i)
            ans = max(ans, j - i + 1)
            dict_s[s[j]] = j + 1
        return ans
