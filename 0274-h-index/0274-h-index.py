class Solution:
    def hIndex(self, c: List[int]) -> int:
        c.sort()
        n=len(c)
        for i in range (n):
            h=n-i
            if c[i]>=h:
                return h
        return 0
