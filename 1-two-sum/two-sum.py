class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        checker = {}
        for index , num in enumerate(nums):
            complement = target - num
            if complement in checker:
                return [checker[complement],index]
            checker[num] = index
        
        