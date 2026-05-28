class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        # i1 = 0
        # find = target - numbers[i1]
        # i2 = -1

        # i = 0
        # j =  len(numbers) - 1
        # m = int(i+j/2)
        # i = -1
        i, j = 0, len(numbers) - 1
        while i<j:
            # m = int(i+j/2)
            # print(m)
            curr_sum  = numbers[i]+numbers[j]
            if curr_sum == target:
                return [i+1, j+1]
            elif curr_sum < target:
                i = i+1
            elif curr_sum > target:
                j = j-1

        # return [i1+1, i2+1]