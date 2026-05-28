class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        # sort the arrays
        g.sort()
        s.sort()
        # For each player we need to find the trainer with least training ability
        trdx = 0 # trainer idx 
        pdx = 0
        # We will increament this if either there is a match or trainer is not sufficient
        pairings = 0
        while pdx < len(g) and trdx < len(s):
            if s[trdx] >= g[pdx]:
                pairings += 1
                pdx += 1
            # else:
            trdx += 1
        return pairings

        