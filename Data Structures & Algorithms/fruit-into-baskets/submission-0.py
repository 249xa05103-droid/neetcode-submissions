class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        d = {}
        l = 0
        maxlen = 0
        for r in range(len(fruits)):
            d[fruits[r]] = d.get(fruits[r], 0) + 1
            while len(d) > 2:
                d[fruits[l]] -= 1
                if d[fruits[l]] == 0:
                    del d[fruits[l]]
                l += 1
            maxlen = max(maxlen, r - l + 1)
        return maxlen