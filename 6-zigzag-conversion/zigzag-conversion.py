class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1:
            return s
        res = ""
        
        for r in range(numRows):
            increment = (numRows-1)*2
            for i in range(r,len(s),increment):
                res += s[i]
                exp = (i+increment)-(2*r)
                if r > 0 and r < numRows-1 and exp < len(s): 
                    res+= s[exp]
        return res