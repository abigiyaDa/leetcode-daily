from collections import Counter
class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        res = []
        checker = Counter(nums)
        atleast = len(nums)//3
        for num, count in checker.items():
            if count >atleast:
                res.append(num)

        return res
        

        