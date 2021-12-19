class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if not s:
            return 0
        start = 0
        max_len = 1
        d = {}
        for i in range(len(s)):
            if s[i] in d:
                start = max(d[s[i]]+1, start)
            d[s[i]] = i
            max_len = max(max_len, i-start+1)
        return max_len
