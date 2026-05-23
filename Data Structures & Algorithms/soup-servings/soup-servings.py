class Solution:
    def soupServings(self, n: int) -> float:
        # This is a graph problem. 
        # Think of it like this <=25 ml = 1 serving
        # divide n to get total serving couunt

        # a -- 100, b 0 a: 4 b: 0
        # a 75 b: 25, a: 3, b: 1
        # a : 50, b : 50, a = b  = 2
        # a 25, b 75 a= 1, b= 3

        # continue this untill one is empty

        # for larger n probability is =~ 1

        if n > 5000:
            return 1.0
        
        m = ceil(n/25)
        print(m)

        cache = [[-1] * (m + 1) for _ in range(m + 1)]
        # print(cache, m)

        def cal_prob(s_A, s_B):
            if s_A <= 0 and s_B <= 0:
                return 0.5
            if s_A <= 0:
                return 1.0
            if s_B <= 0:
                return 0.0
            
            if cache[s_A][s_B] != -1:
                return cache[s_A][s_B]

            # 0.25 = 1/4
            prob =  0.25 * (
                cal_prob(s_A - 4, s_B) + 
                cal_prob(s_A - 3, s_B - 1) +
                cal_prob(s_A - 2, s_B - 2) +
                cal_prob(s_A - 1, s_B - 3)
                )
            
            cache[s_A][s_B] = prob
            return prob #cache[s_A][s_B]
        
        return cal_prob(m, m)


        # once we have that do dfs and have a count of how many traversal happens 
        # how many of them coumed A first. 