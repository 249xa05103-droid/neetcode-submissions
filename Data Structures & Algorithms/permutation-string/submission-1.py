class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        d = {}

        for ch in s1:
            d[ch] = d.get(ch, 0) + 1

        k = len(s1)

        for i in range(len(s2) - k + 1):
            temp = {}

            for j in range(i, i + k):
                temp[s2[j]] = temp.get(s2[j], 0) + 1

            if temp == d:
                return True

        return False
