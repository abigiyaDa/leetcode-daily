class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # reverse the whole then reverse the 1st k then reverse the rest 
        # nums = [1,2,3,4,5,6,7], k = 3
        # Step 1: reverse all
        # → [7,6,5,4,3,2,1]
        # Step 2: reverse first k
        # → [5,6,7,4,3,2,1]
        # Step 3: reverse rest
        # → [5,6,7,1,2,3,4]

        # option 1 

        # time O(n) optimal in-place solution
        m = len(nums)
        k = k % m # bc k is the same as k % m and if k > m then code breaks 

        def to_rev(left,right):
            # reverse 
            while left < right:
                nums[left], nums[right] = nums[right], nums[left]
                left += 1
                right -= 1
        # reverse the whole list
        to_rev(0,m-1)
        # reverse the 1st k
        to_rev(0,k-1)
        # reverse the rest after k
        to_rev(k,m-1)

        # option 2

        # time O(n × k) n- for the slicing
        # m = len(nums)
        # k = k % m # bc k is the same as k % m
        # for i in range(k):
        #     last = nums[-1]
        #     # shift
        #     nums[1:m] = nums[:-1]
        #     nums[0] = last