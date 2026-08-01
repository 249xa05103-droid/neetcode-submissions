class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        ele=nums[0]
        n=0
        for i in range(1,len(nums)):
            if nums[i]==ele:
                n+=1
            elif n==0:
                ele=nums[i]
            elif nums[i]!=ele:
                n-=1
        return ele