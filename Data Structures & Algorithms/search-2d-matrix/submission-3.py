class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        l_r, l_c, r_r, r_c = 0, 0, len(matrix) - 1, len(matrix[-1]) - 1

        while l_r<=r_r:
            m_r = int((l_r+r_r)/2)

            cont=False

            if matrix[m_r][0] <= target <=matrix[m_r][-1]:
                cont=True
            elif matrix[m_r][0] > target:
                r_r = m_r -1
            elif matrix[m_r][-1] < target:
                l_r=m_r+1

            # if matrix[l_r][-1] < target:
            #     l_r+=1
            #     cont=True
            # if matrix[r_r][0] > target:
            #     r_r-=1
            #     cont=True
            
            # print(l_r, r_r)
            if cont:
                nums = matrix[m_r]

                while l_c<=r_c:
                    m=int((l_c+r_c)/2)
                    if nums[m]==target:
                        return True
                    elif nums[m]<target:
                        l_c=m+1
                    else:
                        r_c=m-1
                break
            


        return False