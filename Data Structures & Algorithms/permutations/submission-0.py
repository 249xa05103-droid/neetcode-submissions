class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        ans=[]
        def per(l,nums,visited,n):
            if len(l)==n:
                ans.append(l[:])
                return
            for i in range(n):
                if not visited[i]:
                    l.append(nums[i])
                    visited[i]=True
                    per(l,nums,visited,n)
                    l.pop()
                    visited[i]=False
        per([],nums,[False]*len(nums),len(nums))
        return ans