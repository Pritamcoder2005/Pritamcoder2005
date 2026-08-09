class Solution:
    def stoneGameII(self, piles: List[int]) -> int:
        n = len(piles)
        suffix = [0] * (n + 1)
        for i in range(n - 1, -1, -1):
            suffix[i] = suffix[i + 1] + piles[i]
        @cache
        def dfs (i,M):
            if i>=n:
                return 0
            if 2*M >= n-i:
                return suffix[i]
            best = 0
            for x in range (1,min(2*M,n-i)+1):
                new_M=max(M,x)
                current = suffix[i] - dfs(i+x,new_M)
                best = max(best,current)
            return best
        return dfs(0,1)
        