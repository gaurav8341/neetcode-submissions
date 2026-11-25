class Solution:
    def minCostConnectPoints(self, points: list[list[int]]) -> int:
        n = len(points)
        min_cost = 0
        visited = [False] * n
        pq = [(0, 0)] # cost and index

        while pq:
            cost, idx = heapq.heappop(pq)

            if visited[idx]:
                continue
            
            visited[idx] = True
            min_cost += cost

            for v in range(n):
                if not visited[v]:
                    dist = abs(points[idx][0] - points[v][0]) + \
                            abs(points[idx][1] - points[v][1])
                    heapq.heappush(pq, (dist, v))
            

        return min_cost
