class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):
            l=i+1
            r=len(nums)-1
            k=target-nums[i]
            while l<=r:
                mid=(l+r)//2
                if nums[mid]==k:
                    return [i+1,mid+1]
                if nums[mid]<k:
                    l=mid+1
                else:
                    r=mid-1
