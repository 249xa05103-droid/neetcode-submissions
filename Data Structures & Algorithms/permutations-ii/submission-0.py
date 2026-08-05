class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        ans=[]
        def per(l,nums,idx,n,visited):
            if len(l)==n:
                ans.append(l[:])
                return
            for i in range(n):
                if visited[i]:
                    continue
                if i>0 and nums[i] == nums[i-1] and not visited[i-1]:
                    continue
                l.append(nums[i])
                visited[i]=True
                per(l,nums,i+1,n,visited)
                l.pop()
                visited[i]=False
        nums.sort()
        per([],nums,0,len(nums),[False]*len(nums))
        return ans
            