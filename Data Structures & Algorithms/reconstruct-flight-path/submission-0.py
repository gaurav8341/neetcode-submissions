from collections import defaultdict

class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        adj_map = defaultdict(list)

        tickets.sort()

        for origin, dest in tickets[::-1]:
            adj_map[origin].append(dest)
        
        res = []

        def dfs(src):
            while adj_map[src]:
                dst = adj_map[src].pop()
                dfs(dst)
            res.append(src)
        
        dfs("JFK")
        return res[::-1]


