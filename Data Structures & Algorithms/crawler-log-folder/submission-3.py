class Solution:
    def minOperations(self, logs: List[str]) -> int:
        x = 0
        for i in logs:
            if i == './':
                x += 0
            elif i == '../':
                x = max(0, x - 1)
            else:
                x += 1
        return x