class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        k= k%len(nums)
        last = nums[-k:]
        first = nums[:-k]
        nums[:] = last + first


        """
        Do not return anything, modify nums in-place instead.
        """
        