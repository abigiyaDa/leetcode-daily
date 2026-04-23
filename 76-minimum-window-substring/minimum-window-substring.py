from collections import Counter
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if not t or not s:
            return ""
        # have = number of characters that meet required frequency
        # need_unique = number of unique characters in t
        # if have == need_unique --> then valid window
        
        need = Counter(t)
        window = Counter()
        
        have, need_unique = 0, len(need)
        
        res = (float('inf'), 0, 0)  # length, left, right
        left = 0
        
        for right in range(len(s)):
            char = s[right]
            window[char] += 1
            
            if char in need and window[char] == need[char]:
                have += 1
            
            while have == need_unique:
                # update result
                if (right - left + 1) < res[0]:
                    res = (right - left + 1, left, right)
                
                # shrink window
                window[s[left]] -= 1
                if s[left] in need and window[s[left]] < need[s[left]]:
                    have -= 1
                
                left += 1
        
        return "" if res[0] == float('inf') else s[res[1]:res[2]+1]