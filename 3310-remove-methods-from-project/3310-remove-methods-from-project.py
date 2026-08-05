class Solution:
    def remainingMethods(self, n: int, k: int, invocations: List[List[int]]) -> List[int]:
        graph={}
        for a,b in invocations:
            if a not in graph:
                graph[a]=[]
            graph[a]. append(b)
        suspicious = set()
        def dfs (node):
            if node in suspicious:
                return
            suspicious.add(node)
            for x in graph.get(node,[]):
                dfs(x)
        dfs(k)
        for a, b in invocations:
            if a not in suspicious and b in suspicious:
                return list(range(n))
        ans=[]
        for i in range(n):
            if i not in suspicious:
                ans.append(i)
        return ans
        