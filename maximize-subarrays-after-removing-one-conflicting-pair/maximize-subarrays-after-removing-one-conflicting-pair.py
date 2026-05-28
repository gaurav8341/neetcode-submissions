from collections import defaultdict

class Solution:
    def maxSubarrays(self, n: int, conflictingPairs: List[List[int]]) -> int:
        # this is 2 way problem. 
        # we need to find the valid subarrays (contiguous) 
        # with conflicting pair elems not present in array.

        # suppose our conflict pair is l, r
        # then we will have r-l subarrays possible

        # eg 2,4 Here 4 is non inclusive
        # 4-2 = 2
        # [2], [2, 3]

        # 2nd part is if we remove certain pair 
        # how much subarray we can add        

        # Forbidden Start
        # above eg 2 is forbidden start

        limits = defaultdict(list) # list of forbidden start for that right most value
        for a, b in conflictingPairs:
            limits[max(a, b)].append(min(a,b))
        
       # largest_forbidden, second_largest forbidden
        # for part 2 if for each forbidden idx  we will add largest_forbidden - second_largest elems
        # eg 1, 0
        # and r = 2
        # r-l = 2-1 =1 but we can take 1-0, as well 1
        # we need to take the one which gives the largest subarrays

        res = 0
        left = [0, 0] 
        bonus = [0] * (n+1)

        for r in range(1, n+1):
            for l in limits[r]:
                if l > left[0]:
                    left = [l, left[0]]
                elif l > left[1]:
                    left = [left[0], l]

            res += r - left[0]
            bonus[left[0]] += left[0] - left[1]
        
        return res + max(bonus)
