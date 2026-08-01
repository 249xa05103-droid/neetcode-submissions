class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        l = 0
        r = 1
        while l < len(nums) and r < len(nums):
            if nums[l] == val and nums[r] != val:
                nums[l], nums[r] = nums[r], nums[l]
            if nums[l] != val:
                l += 1
            if r <= l:
                r = l + 1
            elif nums[r] == val:
                r += 1
        c=0
        for i in range(len(nums)):
            if nums[i]==val:
                break
            c+=1
        return c