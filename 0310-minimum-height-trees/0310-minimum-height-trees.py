class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        
        if n == 1:
            return [0]
            
        adj_map = defaultdict(list)
        degrees = [0] * n 
        for u, v in edges:
            adj_map[u].append(v)
            adj_map[v].append(u)
            degrees[u] += 1
            degrees[v] += 1
        
        leaves = deque([l for l in range(len(degrees)) if degrees[l] == 1])

        while n > 2:
            l_count = len(leaves)
            n = n - l_count
            for _ in range(l_count):
                leaf = leaves.popleft()
                for nei in adj_map[leaf]:
                    degrees[nei] -= 1
                    if degrees[nei] == 1:
                        leaves.append(nei)

        return list(leaves)