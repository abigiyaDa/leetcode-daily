class Solution:
    def maximumTripletValue(self, nums: List[int]) -> int:
        # timn o(2n) = o(n), space o(n)
        suffix_max = [0]* len(nums)
        suffix_max[len(nums)-1] = nums[len(nums)-1]
        for i in range(len(nums)-2,-1,-1):
            suffix_max[i] = max(nums[i],suffix_max[i+1])
        max_val = 0
        prefix_max = nums[0]
        for i in range(1,len(nums)-1):
            max_val = max((prefix_max -nums[i])*suffix_max[i+1],max_val)
            prefix_max = max(prefix_max,nums[i])
        return max(max_val,0)
