from collections import Counter
class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # time 0(n) space 0(1)
        # checker = Counter(nums)
        # n = len(nums)
        # start = 0
        # for i in [0,1,2]:
        #     count = checker[i]
        #     while count > 0:
        #         nums[start] = i
        #         start +=1
        #         count -=1
        # 3 pointer option - optimal - no counting time 0(n) space o(1)
        low,mid,high = 0,0,len(nums)-1
        while mid <= high:
            if nums[mid] == 0:
                nums[low],nums[mid] = nums[mid],nums[low]
                low+=1
                mid+=1
            elif nums[mid] == 2:
                nums[mid],nums[high] = nums[high],nums[mid]
                high -=1
            else: # if mid == 1
                mid +=1