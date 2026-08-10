class Solution:
    def winnerSquareGame(self, n: int) -> bool:
        dp = [False] * (n+1)
        dp[0] = False
        for i in range(1,n+1):
            for j in range(1,int(i**0.5)+1):
                square = j*j
                if dp [i-square]==False:
                    dp[i]=True
                    break
        return dp[n]