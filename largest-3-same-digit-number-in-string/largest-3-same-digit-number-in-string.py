class Solution:
    def largestGoodInteger(self, num: str) -> str:
        largest_int = -1

        num = [int(c) for c in num]
        found = False
        for i in range(2,len(num)):
            if num[i-2] == num[i-1] and num[i-1] == num[i]:
                largest_int = max(num[i], largest_int)

        if largest_int != -1:
            largest_num = [str(largest_int)] * 3
            return "".join(largest_num)
        return ""