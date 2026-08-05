class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        ans=[]
        nums.sort()
        def ss(l,nums,idx,n):
            if l not in ans:
                ans.append(l[:])
            if idx==n:
                return
            for i in range(idx,n):
                l.append(nums[i])
                ss(l,nums,i+1,n)
                l.pop()
        ss([],nums,0,len(nums))
        return ans