class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l = 0
        r = 0
        d = {}
        maxi = 0
        while r < len(s):
            if s[r] not in d:
                d[s[r]] = 0
            d[s[r]] += 1
            while d[s[r]] > 1:
                d[s[l]] -= 1
                l += 1
            maxi = max(maxi, r - l + 1)
            r += 1
        return maxi