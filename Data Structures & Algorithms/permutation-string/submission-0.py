class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        d = {}
        for ch in s1:
            d[ch] = d.get(ch, 0) + 1
        k = len(s1)
        for i in range(len(s2) - k + 1):
            temp = d.copy()
            for j in range(i, i + k):
                if s2[j] not in temp or temp[s2[j]] == 0:
                    break
                temp[s2[j]] -= 1
            else:
                return True
        return False