class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        l_r, l_c, r_r, r_c = 0, 0, len(matrix) - 1, len(matrix[-1]) - 1

        while l_r<=r_r:
            m_r = int((l_r+r_r)/2)

            cont=False
            # first find the right array
            if matrix[m_r][0] <= target <=matrix[m_r][-1]:
                cont=True
            elif matrix[m_r][0] > target:
                r_r = m_r -1
            elif matrix[m_r][-1] < target:
                l_r=m_r+1

            if cont:
                # Once the right array is found run Binary search on it.
                nums = matrix[m_r]

                while l_c<=r_c:
                    m=int((l_c+r_c)/2)
                    if nums[m]==target:
                        return True
                    elif nums[m]<target:
                        l_c=m+1
                    else:
                        r_c=m-1
                # In case target is not in the right array break the external loop
                # as the external loop wont exit
                return False
        return False