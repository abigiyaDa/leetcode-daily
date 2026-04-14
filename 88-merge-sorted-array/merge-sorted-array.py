class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        # Time Complexity: O(m × n)
        if n == 0 :
            return
        first, second = 0,0
        while first < m and second < n:
            if nums1[first] > nums2[second]:
                # shift 
                nums1[first+1:m+1] = nums1[first:m]
                nums1[first] = nums2[second]

                m+=1
                first +=1
                second+=1
            else:
                first+=1
        while second < n:
            nums1[first] = nums2[second]
            first+=1
            second +=1