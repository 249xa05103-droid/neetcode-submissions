class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        n=len(nums)
        def sx(x, idx ):
            if idx == n:
                return x
            return sx(x^nums[idx],idx+1)+sx(x,idx+1)
        return sx(0,0)
