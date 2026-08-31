from typing import List

class Solution:
    def canJump(self, nums: List[int]) -> bool:
        i = 0
        while i < len(nums) - 1:
            if nums[i] == 0:
                return False
            maxi = 0
            idx = i
            for j in range(i + 1, min(i + nums[i] + 1, len(nums))):
                if j + nums[j] > maxi:
                    maxi = j + nums[j]
                    idx = j
            if idx == i:
                return False
            i = idx
        return True
