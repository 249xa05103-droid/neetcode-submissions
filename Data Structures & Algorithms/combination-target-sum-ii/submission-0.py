class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        ans = []

        def ss(l, s, nums, idx, target, n):
            if s == target:
                ans.append(l[:])
                return

            if s > target:
                return

            for i in range(idx, n):
                if i > idx and nums[i] == nums[i-1]:
                    continue

                l.append(nums[i])
                ss(l, s + nums[i], nums, i + 1, target, n)
                l.pop()

        candidates.sort()
        ss([], 0, candidates, 0, target, len(candidates))

        return ans
