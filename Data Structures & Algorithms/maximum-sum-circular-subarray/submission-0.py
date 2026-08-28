class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        m1 = nums[0]
        for i in range(len(nums)):
            nums1 = nums[i:] + nums[:i]
            m = nums1[0]
            s = nums1[0]
            for x in nums1[1:]:
                m = max(x, m + x)
                s = max(s, m)
            m1 = max(m1, s)
        return m1