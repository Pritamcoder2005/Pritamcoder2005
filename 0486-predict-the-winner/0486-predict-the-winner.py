class Solution:
    def predictTheWinner(self, nums: List[int]) -> bool:
           def player(left,right):
            if left==right:
                return nums[left]
            left_choice=nums[left]-player(left+1,right)
            right_choice=nums[right]-player(left,right-1)
            return max (left_choice,right_choice)
           return player (0,len(nums)-1)>=0
