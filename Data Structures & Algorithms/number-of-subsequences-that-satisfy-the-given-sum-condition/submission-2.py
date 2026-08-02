class Solution:
    def numSubseq(self, nums: List[int], target: int) -> int:
        mod=10**9 + 7
        nums.sort()
        c=0
        l=0
        r=len(nums)-1
        while l<=r:
            if nums[l]+nums[r]<=target:
                c += 2**(r-l)
                c=c%mod
                l+=1
            else:
                r-=1
        return c
        
