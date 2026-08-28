class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        m = nums[0]
        s = nums[0]
        for x in nums[1:]:
            m = max(x, m + x)
            s = max(s, m)
        return s
