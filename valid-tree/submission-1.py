class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        adj_map = {i:[] for i in range(n)}
        for u, v in edges:
            adj_map[u].append(v)
            adj_map[v].append(u)
        
        visit = set()

        def dfs(v, parent):
            # we need parent here
            if v in visit:
                # cycle detected
                return False

            visit.add(v)

            for nei in adj_map[v]:
                # this will have parent
                if nei == parent:
                    continue
                # else:
                if not dfs(nei, v):
                    return False
            return True
        
        return dfs(0, -1) and len(visit) == n
        # second condtion to make sure all elemnts are part of the tree
            