class Solution:
    def validSequence(self, word1: str, word2: str) -> List[int]:
        n=len(word1)
        m=len(word2)
        suf=[0]*(n+1)
        j=m-1
        for i in range (n-1,-1,-1):
            if j>=0 and word1[i]==word2[j]:
                j-=1
            suf[i]=m-1-j
        ans=[]
        j=0
        used=0
        for i in range(n):
            if j==m:
                break
            if word1[i]==word2[j]:
                ans.append (i)
                j+=1
            elif used == 0:
                remaining=m-j-1
                if suf[i+1]>=remaining:
                    ans.append(i)
                    used=1
                    j+=1
        if j==m:
            return ans
        return()