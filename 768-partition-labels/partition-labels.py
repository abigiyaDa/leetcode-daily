class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        last_occurrence = {}
        for i in range(len(s)):
            last_occurrence[s[i]] = i
        partitions = []
        start = 0
        while start<len(s):
            end = last_occurrence[s[start]]
            j = start

            while j<=end:
                end = max(end,last_occurrence[s[j]])
                j+=1
            partitions.append(j-start)
            start=j
        return partitions
            



        
        