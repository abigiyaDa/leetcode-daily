class Solution:
    def intToRoman(self, num: int) -> str:
        #tuple: (value, symbol)-in tuples order matters
        romans = {
            1000 : "M", 900 : "CM",
            500 : "D",  400 : "CD",
            100 : "C",  90 : "XC",
            50 : "L",   40 : "XL",
            10 : "X",   9 : "IX",
            5 : "V",   4 : "IV",
            1 : "I", 
        }
        #       #first and easy approach 
        # res = []
        # for i in romans:
        #     sym = romans[i]
        #     while num >= i:
        #         num -= i
        #         res.append(sym)
        # return ''.join(res)

        res = []
        for key,sym in romans.items():
            if num // key:
                count = num // key
                res.append(sym*count)
                num = num%key
        return ''.join(res)