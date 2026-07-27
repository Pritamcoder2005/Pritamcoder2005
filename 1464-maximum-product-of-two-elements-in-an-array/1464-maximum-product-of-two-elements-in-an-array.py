class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        a=0
        b=0
        for n in nums:
            b= max (b,min(a,n))
            a=max(a,n)
        return (a-1)*(b-1)