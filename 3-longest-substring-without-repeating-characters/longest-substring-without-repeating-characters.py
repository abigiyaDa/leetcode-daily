from collections import deque
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        res = 0
        store = deque()
        for i in s:
            if i not in store:
                store.append(i)
            elif i in store:
                while i in store:
                    store.popleft()
                store.append(i)
            else:
                store.append(i)
            res = max(res,len(store))
        return res
                
