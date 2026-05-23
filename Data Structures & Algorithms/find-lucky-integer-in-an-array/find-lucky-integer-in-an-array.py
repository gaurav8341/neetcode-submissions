class Solution:
    def findLucky(self, arr: List[int]) -> int:
        
        cnt_map = [0] * (max(arr) + 1) 
        
        for a in arr:
            cnt_map[a] += 1
        
        for i in range(len(cnt_map)-1, 0, -1):
            if cnt_map[i] == i and i != 0:
                return cnt_map[i]

        return -1