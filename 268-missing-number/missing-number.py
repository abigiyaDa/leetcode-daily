class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        # better option - the sum from 0 - n is [n(n+1)]/2
        # time - o(n) space - o(1)
        n = len(nums)
        total_sum = (n*(n+1))//2
        return total_sum - sum(nums)
        # time - n
        # space - n
        # n =len(nums)
        # checker = {num : True for num in nums}
        # for i in range(n+1):
        #     if i not in nums:
        #         return i

        