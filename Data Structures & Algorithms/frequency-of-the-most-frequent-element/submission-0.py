class Solution:
    def maxFrequency(self, nums: List[int], k: int) -> int:
        nums.sort()
        n = len(nums)
        prefix = [0] * (n + 1)
        for i in range(n):
            prefix[i + 1] = prefix[i] + nums[i]
        maxlen = 1
        for i in range(n):
            for j in range(i + 1, n):
                cost = nums[j] * (j - i) - (prefix[j] - prefix[i])
                if cost <= k:
                    maxlen = max(maxlen, j - i + 1)
        return maxlen
