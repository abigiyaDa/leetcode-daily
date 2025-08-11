class Solution:
    def maximumTripletValue(self, nums: List[int]) -> int:
        # time o(n) and space o(1)
        res = 0
        max_diff = 0
        prefix_max = nums[0]
        for i in range(1,len(nums)):
            res = max(max_diff * nums[i],res)
            prefix_max = max(prefix_max,nums[i])
            max_diff = max(max_diff,prefix_max-nums[i])
        return max(res,0)

        #         # timn o(2n) = o(n), space o(n)
        # suffix_max = [0]* len(nums)
        # suffix_max[len(nums)-1] = nums[len(nums)-1]
        # for i in range(len(nums)-2,-1,-1):
        #     suffix_max[i] = max(nums[i],suffix_max[i+1])
        # max_val = 0
        # prefix_max = nums[0]
        # for i in range(1,len(nums)-1):
        #     max_val = max((prefix_max -nums[i])*suffix_max[i+1],max_val)
        #     prefix_max = max(prefix_max,nums[i])
        # return max(max_val,0)
