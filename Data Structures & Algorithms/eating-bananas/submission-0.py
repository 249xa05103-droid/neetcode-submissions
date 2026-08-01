class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        if len(piles)==h:
            return max(piles)
        r=max(piles)
        l=1
        ans=r
        while l<=r:
            c=0
            mid=(l+r)//2
            if mid == 0: mid = 1
            for i in range(len(piles)):
                c+=math.ceil(piles[i]/mid)
            if c<=h:
                ans = mid
                r=mid-1
            else:
                l=mid+1
        return ans