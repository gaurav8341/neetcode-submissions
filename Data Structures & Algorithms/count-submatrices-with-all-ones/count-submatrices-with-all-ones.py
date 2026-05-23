class Solution:
    def numSubmat(self, mat: List[List[int]]) -> int:
        
        # nums = [[0]*len(mat[0])]*len(mat)
        h = [0] * len(mat[0])

        ans = 0
        # m*n
        for i in range(len(mat)):
            for j in range(len(mat[0])):
                if mat[i][j] == 1:
                    h[j] = h[j] + 1
                else:
                    h[j] = 0
            
            sums = [0] * len(mat[0]) # sums
            st = []  # monotonic stack strictly increasing order #store idxes here
            for j in range(len(mat[0])):
                while st and h[st[-1]] >= h[j]:
                    st.pop()
                if st:
                    top = st[-1]
                    sums[j] = sums[top] + h[j] * (j-top)
                else:
                    sums[j] = h[j] * (j + 1)
                st.append(j)
                ans += sums[j]
        return ans