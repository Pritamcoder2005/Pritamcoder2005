
class Solution:
    def findMissingElements(self, nums: List[int]) -> List[int]:
        ans=[]
        small=min(nums)
        large=max(nums)
        for i in range(small,large+1):
            if i not in nums:
                ans.append(i)
        return ans
       