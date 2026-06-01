class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        
        adj_map = defaultdict(list)
        for course, prerq in prerequisites:
            adj_map[course].append(prerq)

        visited = [0] * numCourses

        def has_cycle(course):
            nonlocal visited
            if visited[course] == 1:
                # vertex is processed already
                return False
            if visited[course] == -1:
                # we have a cycle as this is already process:
                return True
            
            visited[course] = -1

            for i in adj_map[course]:
                if has_cycle(i):
                    return True
            
            visited[course] = 1
            return False
        
        for key in range(numCourses):
            if has_cycle(key):
                return False
        
        return True



        