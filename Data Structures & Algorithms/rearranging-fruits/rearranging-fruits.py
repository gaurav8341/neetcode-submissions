from collections import Counter

class Solution:
    def minCost(self, basket1: List[int], basket2: List[int]) -> int:
        # 2 baskets with n fruits
        # have 2 array indicating cost of fruits in them
        # make both baskets equal

        ## ops allowed
        # swap the fruits in both baskts ith in b1 jth in b2
        # cost of swap is min(b1[i], b2[j])

        # return min cost to make them equal

        # baskts are equal if sorting makes them identical

        # we can only swap elements appeared more than once in each array

        # Sort both arrays nlogn 
        # get count of each elem.
        # if frequency dicts match then baskets match 

        # if number of keys do not match -1
        # if for any key total sum from both dict is odd -1

        # basket1.sort()
        # basket2.sort()

        b1_frequencies = Counter(basket1)
        # b2_frequencies = Counter(basket2)
        total_counts = Counter(basket1) + Counter(basket2)

        for count in total_counts.values():
            if count % 2 != 0:
                return -1
        
        fruits_to_swap = []
        for key, count in total_counts.items():
            # for both baskets to be equal 
            # this amount should be in each basket
            target = count // 2 
            diff = target - b1_frequencies.get(key, 0)

            ## diff is surpluc if diff > 0 b2 surplus
            ## diff < 0 b1 surplus
            # diff is amount of swap needed to balance the baskets

            for _ in range(abs(diff)):
                fruits_to_swap.append(key)
        
        # cost calculation

        # 2 ways to calc cost oone find fruits from both baskets to swap
        # x from b1 and y from b2 
        # cost is min(x, y)

        # helper swap
        # swap x with min valuein overall basket
        # swap x, minval cost (x, minval)
        # swap minval with another elem which we will have

        # first sort
        fruits_to_swap.sort()
        cost = 0
        swaps = len(fruits_to_swap) // 2
        min_val = min(total_counts.keys())

        for i in range(swaps):
            cost += min(fruits_to_swap[i], 2*min_val)
        
        return cost        