class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        ans = []
        nums.sort()

        def ss(l, idx):
            ans.append(l[:])

            for i in range(idx, len(nums)):
                if i > idx and nums[i] == nums[i-1]:
                    continue

                l.append(nums[i])
                ss(l, i+1)
                l.pop()

        ss([], 0)
        return ans
