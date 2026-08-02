class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        l = 0
        r = 0
        n = len(blocks)
        maxi = n + 1

        while l <= n - k:
            x = k
            r = l
            c = 0

            while r < l + k and x > 0:
                if blocks[r] == 'W':
                    c += 1
                x -= 1
                r += 1

            maxi = min(maxi, c)
            l += 1

        return maxi