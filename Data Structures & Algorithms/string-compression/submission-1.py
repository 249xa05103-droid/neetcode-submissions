class Solution:
    def compress(self, chars: List[str]) -> int:
        l = 0
        r = 0
        n = len(chars)
        idx = 0

        while r < n:
            while r < n and chars[l] == chars[r]:
                r += 1

            count = r - l

            chars[idx] = chars[l]
            idx += 1

            if count > 1:
                for c in str(count):
                    chars[idx] = c
                    idx += 1

            l = r

        return idx