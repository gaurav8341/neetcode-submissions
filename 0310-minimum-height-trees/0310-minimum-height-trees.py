class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        # basicaaly we make this list by trimming the tree at the leaves until there are only 2 elemnts or less than 2 elements in th tree

        if n == 1:
            return [0]# [i for i in range(n)]

        adj_map = defaultdict(list)
        degree = [0] * n
        for n1, n2 in edges:
            adj_map[n1].append(n2)
            adj_map[n2].append(n1)
            degree[n1] += 1
            degree[n2] += 1
        
        # get all the leaves
        leaves = deque([i for i in range(n) if degree[i] == 1])

        remaining_nodes = n
        while remaining_nodes > 2:
            leaves_count = len(leaves)
            remaining_nodes -= leaves_count

            for _ in range(leaves_count):
                leaf = leaves.popleft()
                for nei in adj_map[leaf]:
                    degree[nei] -= 1
                    if degree[nei] == 1:
                        leaves.append(nei)
            
        return list(leaves)
