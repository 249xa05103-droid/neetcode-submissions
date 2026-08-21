class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        for i in range(1, len(nums)):
            nums[i] += nums[i - 1]
        if nums[0] >= target:
            return 1
        minlen = float('inf')
        l = 0
        r = 1
        while r < len(nums):
            if l == 0:
                current_sum = nums[r]
            else:
                current_sum = nums[r] - nums[l - 1]

            if current_sum < target:
                r += 1
            else:
                minlen = min(minlen, r - l + 1)
                l += 1
        return 0 if minlen == float('inf') else minlen