class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        l = 0
        r = 0
        maxi = len(blocks) + 1
        while l < len(blocks):
            x = k
            r = l
            c = 0
            while r < len(blocks) and x > 0:
                if blocks[r] == 'W':
                    c += 1
                x -= 1
                r += 1
            if x == 0:
                maxi = min(maxi, c)
            l += 1
        return maxi