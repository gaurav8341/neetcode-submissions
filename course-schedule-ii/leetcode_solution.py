class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        adj_map = {n:[] for n in range(numCourses)}
        for parent, child in prerequisites:
            adj_map[parent].append(child)
        
        # wee need cycle detection algo 
        # we also need to maintain path
        dfs_path = []
        cycle, visit = set(), set()

        def dfs(v):
            if v in cycle:
                return True

            if v in visit:
                # no need to go through again
                return False

            cycle.add(v)
            

            for child in adj_map[v]:
                if dfs(child):
                    return True
            
            cycle.remove(v) # once course is satisfied no need of this
            visit.add(v)
            dfs_path.append(v)
            
            return False
        
        for n in range(numCourses):
            if dfs(n):
                return []
        
        return dfs_path
