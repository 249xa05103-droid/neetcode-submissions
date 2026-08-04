class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        ans=[]
        def cc(l,nums,idx,n,k):
            if len(l)==k:
                ans.append(l[:])
                return
            for i in range(idx,n):
                l.append(nums[i])
                cc(l,nums,i+1,n,k)
                l.pop()
        nums=[i for i in range(1,n+1)]
        cc([],nums,0,n,k)
        return ans