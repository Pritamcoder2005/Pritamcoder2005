class Solution:
    def missingMultiple(self, nums: List[int], k: int) -> int:
        num=k
        while num in nums:
            num +=k
        return num