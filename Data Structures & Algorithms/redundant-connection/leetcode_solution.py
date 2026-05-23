class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        
        # find the number of nodes 
        n = len(edges) # in the first line they mentioned edges

        adj_map = {i:set() for i in range(1, n+1)} # we are using set as addition and deletion would be easier
        for u, v in edges:
            adj_map[u].add(v)
            adj_map[v].add(u)

        def dfs(node, visit, parent):
            if node in visit:
                # cycle detected
                return False
            
            visit.add(node)
            for nei in adj_map[node]:
                if nei == parent:
                    # parents will give cycle if there isnt any
                    continue
                if not dfs(nei, visit, node):
                    return False
            
            return True
        
        result = []
        for u, v in edges:
            adj_map[u].remove(v)
            adj_map[v].remove(u)
            visit = set()
            if dfs(u, visit, -1) and len(visit) == n:
                result = [u, v]
            adj_map[u].add(v)
            adj_map[v].add(u)
            
        return result
