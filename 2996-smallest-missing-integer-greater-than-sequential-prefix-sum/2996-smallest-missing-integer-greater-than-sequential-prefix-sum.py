class Solution:
    def missingInteger(self, nums: List[int]) -> int:
        total = 0
        for i in range(0,len(nums)):
            if i == 0:
                total+=nums[i]
            elif nums[i]==nums[i-1]+1:
                total+=nums[i]
            else:
                break
        n=total
        while n in nums:
            n+=1
        return n
      
        