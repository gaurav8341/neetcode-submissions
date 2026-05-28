
class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        # first form adjacencylist
        # Detect cycle if cycle exists then return empty array
        # do a dfs on that.
        # maintain a visit order return that in reverse
        # O(v+E) cycle detection
        # O(V+E) order

        adj_map = {n:[] for n in range(numCourses)}
        for parent, child in prerequisites:
            adj_map[parent].append(child)

        cycle, visited = set(), set()

        dfs_path = []

        print(adj_map)
        def dfs(v):
            print(v, visited, dfs_path, cycle)
            if v in cycle:
                # there is cycle
                return True
            
            if v in visited:
                # already visited no need of aggain
                return False
            
            cycle.add(v)

            for nbr in adj_map[v]:
                if dfs(nbr):
                    return True

            cycle.remove(v)
            visited.add(v)
            dfs_path.append(v)
            
            return False
        
        for n in range(numCourses):
            print(n)
            if dfs(n):
                return []
        
        return dfs_path
