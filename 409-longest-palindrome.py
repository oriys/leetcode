import collections 
class Solution:
    def longestPalindrome(self, s: str) -> int:
        count = collections.Counter(s).values()
        x = sum([item//2*2 for item in count if (item//2 > 0)])
        return x if x == len(s) else x + 1
