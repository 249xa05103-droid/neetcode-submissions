class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        ans = []
        def ss(l, nums, idx, n):
            ans.append(l[:])
            for i in range(idx, n):
                l.append(nums[i])
                ss(l, nums, i + 1, n)
                l.pop()
        ss([], nums, 0, len(nums))
        return ans
