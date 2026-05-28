class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        
        adj_map = {i:[] for i in range(n)}

        for u, v in edges:
            adj_map[u].append(v)
            adj_map[v].append(u)

        visit = set()

        count = 0

        def dfs(v, parent = -1):
            nonlocal count
            if v in visit:
                return 
            
            if parent == -1:
                count += 1
            
            visit.add(v)

            for nei in adj_map[v]:
                dfs(nei, v)
            
        for i in range(n):
            dfs(i, -1)
        
        return count
