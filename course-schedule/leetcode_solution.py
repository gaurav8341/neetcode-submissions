class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        
        adj_map = {i:[] for i in range(numCourses)}

        for crs, adj in prerequisites: 
            # prerequisietes is supposed to be a pair
            adj_map[crs].append(adj) 
        
        visited = set()
        
        def dfs(crs):
            if crs in visited:
                # crs is in visited its a cycle
                return False
            if adj_map[crs] == []:
                return True
            
            visited.add(crs)
            for pre in adj_map[crs]:
                if not dfs(pre):
                    return False
            visited.remove(crs)# why this line
            adj_map[crs] = []# This course is done remove from prerequisites
            return True
        
        for crs in range(numCourses):
            # need to check all courses'dependancy
            if not dfs(crs):
                return False
        return True