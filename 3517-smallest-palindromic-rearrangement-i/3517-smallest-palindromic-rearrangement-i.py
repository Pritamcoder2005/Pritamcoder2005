class Solution:
    def smallestPalindrome(self, s: str) -> str:
        s=list(s)
        length=len(s)
        half=length//2
        s[:half]= sorted(s[:half])
        for i in range(half):
            s[length-1-i]=s[i]
        return"".join(s)