from typing import List
class Solution:
    def partition(self, s: str) -> List[List[str]]:
        ans = []
        curr = []
        def backtrack(idx):
            if idx == len(s):
                ans.append(curr.copy())
                return
            for i in range(idx, len(s)):
                substring = s[idx:i + 1]
                if substring == substring[::-1]:
                    curr.append(substring)
                    backtrack(i + 1)
                    curr.pop()
        backtrack(0)
        return ans
