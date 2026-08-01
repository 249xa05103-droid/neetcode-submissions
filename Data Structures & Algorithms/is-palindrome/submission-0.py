import string
class Solution:
    def isPalindrome(self, s: str) -> bool:
        l=0
        r=len(s)-1
        alpha=list(string.ascii_lowercase)+['1','2','3','4','5','6','7','8','9','0']
        while l<=r:
            if s[l].lower() not in alpha:
                l+=1
                continue
            if s[r].lower() not in alpha:
                r-=1
                continue
            if s[l].lower()==s[r].lower():
                l+=1
                r-=1
            else:
                break
        if l>=r:
            return True
        return False