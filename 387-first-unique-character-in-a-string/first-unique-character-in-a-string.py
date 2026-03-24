from collections import Counter
class Solution:
    def firstUniqChar(self, s: str) -> int:
        checker = Counter(s)
        for item,count in checker.items():
            if count == 1:
                return s.index(item)
        return -1
        