class Solution:
    def predictTheWinner(self, nums: List[int]) -> bool:
        def player(left,right):
            if left==right:
                return nums [left]
            left_val = nums[left]-player(left+1,right)
            right_val = nums[right]-player(left,right-1)
            return max (left_val,right_val)
        return player (0, len(nums)-1)>=0
              
                 
          
