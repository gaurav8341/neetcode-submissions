class Solution:
    def _2pointer(self, nums1: List[int], nums2: List[int]) -> float:
        # we have two sorted arrays.
        # we need to find the median of array if they are merged.

        # median will hold the postion (m+n)/2 
        # where m and n are length of arrays

        # mid point 
        ## approach 1
        """
            In below approach we are parsing through 
            the first halves of the arrays

            We are taking minimum of the two elements 
            from two arrays as the median

            This is easy solution.
        """
        m, n = len(nums1), len(nums2)
        i, j = 0, 0
        median1,median2 = 0, 0
        # time complexity o(m+n) space complexity: o(1)

        for count in range((m+n)//2 + 1):
            median2 = median1
            if i < m and j < n:
                if nums1[i] > nums2[j]:
                    median1 = nums2[j]
                    j = j + 1
                else:
                    median1 = nums1[i]
                    i = i + 1
            elif i < m:
                median1 = nums1[i]
                i = i + 1
            else:
                median1 = nums2[j]
                j = j + 1
        if (m+n)%2 == 1:
            return float(median1)
        return (median1+median2)/2
    
    def _binary_search(self, nums1: List[int], nums2: List[int]) -> float:
        pass
    
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        return self._2pointer(nums1, nums2)
