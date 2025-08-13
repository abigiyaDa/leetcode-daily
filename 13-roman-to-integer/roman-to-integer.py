class Solution:
    def romanToInt(self, s: str) -> int:
        romans = {
            "I" : 1,
            "V" : 5,
            "X" : 10,
            "L" : 50,
            "C" : 100,
            "D" : 500,
            "M" : 1000,
        }
        before = s[0]
        res = romans[before]
        for x in range(1,len(s)):
            if romans[before] < romans[s[x]]:
                # b/c i add it before hand we need to remove romans[s[x-1]] twice 
                # example before = 'I', res = 1
                # x = 1 → romans['I'] < romans['X'] → y = 10 - 1 = 9 → res = 1 + 9 = 10 ❌
                y = romans[s[x]] -(2*romans[s[x-1]]) 
                res += y
            else:
                res+=romans[s[x]]
            before = s[x]
        return res