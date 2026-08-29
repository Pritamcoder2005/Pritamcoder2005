class Solution:
    def jump(self, nums: List[int]) -> int:
        jump=0
        n=0
        m=0
        for i in range (len(nums)-1):
            m=max(m,i+nums[i])
            if i==n:
                jump += 1
                n=m
        return jump