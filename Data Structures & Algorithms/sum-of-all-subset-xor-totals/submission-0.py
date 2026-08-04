class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        def sx(l, nums, n, idx, x):
            if idx == n:
                return x
            l.append(nums[idx])
            take = sx(l, nums, n, idx + 1, x ^ l[-1])
            l.pop()
            not_take = sx(l, nums, n, idx + 1, x)
            return take + not_take
        return sx([], nums, len(nums), 0, 0)
