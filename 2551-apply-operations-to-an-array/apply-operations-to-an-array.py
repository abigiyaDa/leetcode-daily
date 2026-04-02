class Solution:
    def applyOperations(self, nums: List[int]) -> List[int]:
        n = len(nums)
        for i in range(n-1):
            if nums[i] == nums[i+1]:
                nums[i] *= 2
                nums[i+1] =0
        first = 0
        second = 0
        while second<n:
            if nums[second] != 0:
                nums[first],nums[second] = nums[second] ,nums[first]
                second +=1
                first +=1
            else:
                second += 1
        return nums




        