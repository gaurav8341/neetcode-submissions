class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        
        adj_map = defaultdict(list)
        for course, prerq in prerequisites:
            adj_map[course].append(prerq)

        visited = [0] * numCourses
        cycle = [0] * numCourses
        dfs_path = list()

        def dfs(course):
            nonlocal visited
            if visited[course] == 1:
                # vertex is processed already
                return False
            if cycle[course] == 1:
                # we have a cycle as this is already process:
                return True
            
            cycle[course] = 1

            for i in adj_map[course]:
                if dfs(i):
                    return True
            
            cycle[course] = 0
            visited[course] = 1
            dfs_path.append(course)
            return False
        
        for key in range(numCourses):
            if dfs(key):
                return []
        
        return dfs_path



        