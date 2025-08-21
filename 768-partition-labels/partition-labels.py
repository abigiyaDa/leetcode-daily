class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        last = {}
        for i in range(len(s)):
            last[s[i]] = i
        res = []
        i = 0
        while i<len(s):
            x = last[s[i]]
            j=i
            while j<=x:
                x = max(x,last[s[j]])
                j+=1
            res.append(j-i)
            i=j
        return res
            



        
        