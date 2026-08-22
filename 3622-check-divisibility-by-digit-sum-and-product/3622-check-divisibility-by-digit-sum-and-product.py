class Solution:
    def checkDivisibility(self, n: int) -> bool:
        original=n
        sum=0
        product=1
        while n>0:
            digit=n%10
            sum+=digit
            product *= digit
            n//=10
        total=sum+product
        return original%total==0