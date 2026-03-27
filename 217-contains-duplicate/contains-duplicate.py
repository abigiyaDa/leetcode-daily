class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        nums.sort()
        first = 0
        second = 1
        while second < len(nums):
            if nums[first] == nums[second]:
                return True
            second+=1
            first+=1
        return False
        