class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        # j=1
        # count = 1
        # n=len(nums)
        # for i in range(1,n):
        #     if nums[i] == nums[i-1]:
        #         count +=1
        #     else:
        #         count = 1
                
        #     if count <= 2:
        #         nums[j] = nums[i]
        #         j+=1
        # return j
        j=0
        for i in range(len(nums)):
            if j < 2 or nums[i] != nums[j-2]:
                nums[j] = nums[i]
                j+=1
        return j

        