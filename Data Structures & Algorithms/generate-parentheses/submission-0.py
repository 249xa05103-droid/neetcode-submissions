class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        ans=[]
        def gp(s,o,c,n):
            if o+c==2*n:
                ans.append(s[:])
                return
            if o<n:
                gp(s+'(',o+1,c,n)
            if o>c:
                gp(s+')',o,c+1,n)
        gp('',0,0,n)
        return ans