from collections import Counter
class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        # map time - o(n log n) space-o(n) + 0(k) = o(n)(1 for checker and the other for res) 
        checker = Counter(arr1)
        res = []
        for j in arr2:
            count = checker[j]
            res.extend([j]*count)
            del checker[j]

        # then sort the remaining and add them to res 
        sorted_checker = dict(sorted(checker.items()))  
        for key,val in sorted_checker.items():
            if key not in arr2:
                res.extend([key] * val)
        return res
