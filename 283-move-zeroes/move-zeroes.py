class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        first,second = 0,0
        while second < len(nums):
            if nums[second] != 0:
                nums[first],nums[second] = nums[second],nums[first]
                first +=1
            second+=1
        
            
        