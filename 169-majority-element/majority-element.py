from collections import Counter
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        checker = Counter(nums)
        atleast = len(nums)//2
        for num, count in checker.items():
            if count >atleast:
                return num
        