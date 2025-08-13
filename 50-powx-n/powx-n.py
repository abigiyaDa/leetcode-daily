class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n < 0:
            n=-n
            x=1/x
        result = 1
        while n>0:
            if n%2 != 0:
                result *= x
            x*=x
            n//=2
        return result
        # x=float(x)
        # n=int(n)
        # output=x**n
        # return output
        