class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        # time o(n^2) space o(n)
        res = []
        nums_sorted = sorted(nums)
        for i in nums:
            idx = nums_sorted.index(i)
            res.append(idx)
        return res
        # # optimal
        # rank = {}
        # nums_sorted = sorted(nums)
        # for idx,num in enumerate(nums_sorted):
        #     if num not in rank:
        #         rank[num] = idx
        # return [rank[num] for num in nums]