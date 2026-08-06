class Solution:
    def smallestNumber(self, n: int, t: int) -> int:
        num = n
        while True:
            temp = num
            product = 1
            while temp > 0:
                digit = temp % 10
                product = product * digit
                temp = temp // 10
            if product % t == 0:
                return num
            num += 1
