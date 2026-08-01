class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l=[0]*len(prices)
        l[-1]=prices[-1]
        for i in range(len(l)-2,-1,-1):
            l[i]=max(prices[i],l[i+1])
        for i in range(len(l)):
            l[i]-=prices[i]
        print(l)
        return max(l)
