class Solution:
    def majorityElement(self, nums: List[int]) -> int: 
        #Boyer-Moore Voting Algorithm 
        count = 0
        x=0
        for i in range(len(nums)):
            if count == 0:
                x = nums[i]
            if nums[i] == x:
                count += 1
            else :
                count-=1
        return x


        
        
        
        