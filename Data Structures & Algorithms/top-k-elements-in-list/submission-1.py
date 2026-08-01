class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        d={}
        f=[]
        for i in nums:
            d[i]=0
        for i in nums:
            d[i]+=1
        l=[[] for _ in range(len(nums)+1)]
        for i in d.keys():
            l[d[i]].append(i)
        for i in range(len(l)-1,-1,-1):
            for val in l[i]:
                if k==0:
                    break
                f.append(val)
                k-=1
        return sorted(f)