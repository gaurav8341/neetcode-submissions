class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # this is basically probelm of finding cycles in graph

        # We need to convert this list into adjacency list

        adj_map = {i: [] for i in range(numCourses)}
        for cls, pre in prerequisites:
            adj_map[cls].append(pre)
        

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
            # in case if any course is in progress. 
            # then it will be in visisted unless all prerequisites aare fulfileed 
            # once they are fulfilled we can remove it.
            # adj_map[v] = [] # we are doing this for if the list is empty 
            #then the course can be fulfilled
            # we dont want to go through prereq of any course if we have fulfilled it
            # think of this in conjunction with above 2nd if statement
            return True

        for c in range(numCourses):
            if not dfs(c):
                return False
        return True

