from collections import Counter
class Solution:
    def minSteps(self, s: str, t: str) -> int:
        steps = 0
        counter_1 = Counter(s)
        counter_2 = Counter(t)
        for index, count in counter_1.items():
            if index not in counter_2:
                steps += count
            elif (count - counter_2[index]) > 0:
                steps += counter_1[index] - counter_2[index]
        return steps
        
        