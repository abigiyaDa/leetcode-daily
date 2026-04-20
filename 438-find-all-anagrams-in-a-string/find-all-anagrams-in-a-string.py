from collections import Counter
class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        if len(s) < len(p):
            return []
        size = len(p)
        p_counter =Counter(p)
        window_counter = Counter()
        result = []
        left = 0
        # Initialize 1st window
        for i in range(size):
            window_counter[s[i]]+=1
        # check 1st window
        if window_counter == p_counter:
            result.append(0)

        # lets iterate
        for right in range(size,len(s)):
            window_counter[s[right]] +=1
            window_counter[s[left]] -= 1

            if window_counter[s[left]] == 0:
                del window_counter[s[left]]

            left+=1 # move left pointer forward
            
            if window_counter == p_counter:
                result.append(left)
        return result 

        