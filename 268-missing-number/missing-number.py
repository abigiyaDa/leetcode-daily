class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n =len(nums)
        checker = {}
        res = 0
        for i in range(n+1):
            if i in nums:
                checker[i] = checker.get(i, 1)
            else:
                res = i
        return res

        