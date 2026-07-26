class Solution:
    def maximumProduct(self, nums: List[int]) -> int:
        first=float('-inf')
        second=float('-inf')
        third=float('-inf')
        min1=float('inf')
        min2=float('inf')
        for lastd in nums:
            if lastd>=first:
                third=second
                second=first
                first=lastd
            elif lastd>=second:
                third=second
                second=lastd
            elif lastd>=third:
                third=lastd
            if lastd<=min1:
                min2=min1
                min1=lastd
            elif lastd<=min2:
                min2=lastd
        return max(first*second*third,first*min1*min2)


        