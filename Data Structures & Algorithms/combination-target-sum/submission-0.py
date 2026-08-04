class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        ans = []
        def cs(l, s, nums, n, target, idx):
            if s == target:
                ans.append(l[:])
                return
            if s > target:
                return
            for i in range(idx, n):
                l.append(nums[i])
                cs(l, s + nums[i], nums, n, target, i)
                l.pop()
        cs([], 0, nums, len(nums), target, 0)
        return ans
