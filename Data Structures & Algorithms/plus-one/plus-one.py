class Solution:

    def arr_to_num(self, digits):
        num = 0
        for i in digits:
            num = num * 10
            num += i
        
        return num

    def plusOne(self, digits: List[int]) -> List[int]:
        num = self.arr_to_num(digits)

        num += 1

        digits = str(num)

        return [int(n) for n in list(digits)]

