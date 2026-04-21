from collections import Counter
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        window_len = len(s1)
        if len(s2) < window_len :
            return False
        left = 0
        window_counter = Counter()
        s1_counter = Counter(s1)
        # initialize
        for i in range(window_len):
            window_counter[s2[i]] +=1
        if window_counter == s1_counter:
            return True
        for right in range(window_len,len(s2)):
            window_counter[s2[right]] += 1
            window_counter[s2[left]] -=1
            # if the item has value 0 - remove
            if window_counter[s2[left]] == 0:
                del window_counter[s2[left]]
            left+=1
            if window_counter == s1_counter:
                return True
        return False
        