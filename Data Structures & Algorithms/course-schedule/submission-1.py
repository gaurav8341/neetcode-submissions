class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # this is basically probelm of finding cycles in graph

        # We need to convert this list into adjacency list

        adj_map = {i: [] for i in range(numCourses)}
        for cls, pre in prerequisites:
            adj_map[cls].append(pre)
        
        print(adj_map)


        visited = set()

        def dfs(v):
            if v in visited:
                return False
            if adj_map[v] == []:
                return True
            
            visited.add(v)

            for nbr in adj_map[v]:
                if not dfs(nbr):
                    return False
            visited.remove(v)
            adj_map[v] = []
            return True

        for c in range(numCourses):
            if not dfs(c):
                return False
        return True

