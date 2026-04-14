class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        # optimal Time Complexity: O(m + n) 
        p1 = m - 1  # last valid element in nums1
        p2 = n - 1  # last element in nums2
        p = m + n - 1  # last position in nums1
        
        while p2 >= 0:
            if p1 >= 0 and nums1[p1] > nums2[p2]:
                nums1[p] = nums1[p1]
                p1 -= 1
            else:
                nums1[p] = nums2[p2]
                p2 -= 1
            p -= 1
        # # Time Complexity: O(m × n)
        # if n == 0 :
        #     return
        # first, second = 0,0
        # while first < m and second < n:
        #     if nums1[first] > nums2[second]:
        #         # shift 
        #         nums1[first+1:m+1] = nums1[first:m]
        #         nums1[first] = nums2[second]

        #         m+=1
        #         first +=1
        #         second+=1
        #     else:
        #         first+=1
        # while second < n:
        #     nums1[first] = nums2[second]
        #     first+=1
        #     second +=1