from collections import deque
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # optimal o(n) use set and 2 pointers 
        # time - o(n) space - o(n)
        seen = set()
        left = 0
        res = 0
        for right in range(len(s)):
            while s[right] in seen:
                seen.remove(s[left])
                left+=1
            seen.add(s[right])
            res = max(res, right-left + 1)
        return res

        # not optimal bc the look up i in store takes o(n) making the time complexity 
        # time o(n^2) 

        # res = 0
        # store = deque()
        # for i in s:
        #     if i not in store:
        #         store.append(i)
        #     elif i in store:
        #         while i in store:
        #             store.popleft()
        #         store.append(i)
        #     else:
        #         store.append(i)
        #     res = max(res,len(store))
        # return res