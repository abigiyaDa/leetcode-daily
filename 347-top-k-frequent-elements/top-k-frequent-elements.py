from collections import Counter
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        checker = Counter(nums) # [1,1,1,2,2,3] = {1:3,2:2, 3:1}
        sorted_checker = checker.most_common(k)

        res = [num[0] for num in sorted_checker]
        return res

        