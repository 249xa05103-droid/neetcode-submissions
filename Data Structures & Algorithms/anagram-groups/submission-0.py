class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        d={}
        for i in strs:
            s=''.join(sorted(i))
            if s in d:
                d[s].append(i)
            else:
                d[s]=[]
                d[s].append(i)
        ans=[]
        for i in d:
            ans.append(d[i])
        return ans