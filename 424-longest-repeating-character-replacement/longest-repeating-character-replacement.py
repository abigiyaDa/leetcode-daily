from collections import defaultdict
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        left = 0
        freq = defaultdict(int)
        res = 0
        for right in range(len(s)):
            freq[s[right]] +=1
            max_freq = max(freq.values())
            curLen = right - left +1
            if curLen-max_freq > k:
                # shrink 
                freq[s[left]] -=1
                left +=1
            else:
                # valid 
                res = max(res,curLen)
        return res
            

        