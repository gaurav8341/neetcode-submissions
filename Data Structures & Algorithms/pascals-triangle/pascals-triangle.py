class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        #pascal trainagle will have numRowsrows staring and ending with 1.
        # each row size incrementing by 1
        res = []
        while numRows > 0:
            if len(res) < 2:
                if len(res) == 0:
                    res.append([1])
                else:
                    res.append([1, 1])
                numRows -= 1
                continue
            
            prev_row = res[-1]
            next_row = [1]
            for i in range(1, len(prev_row)):
                next_row.append(prev_row[i-1] + prev_row[i])
            next_row.append(1)
            res.append(next_row)
            numRows -= 1
        
        return res
            

            