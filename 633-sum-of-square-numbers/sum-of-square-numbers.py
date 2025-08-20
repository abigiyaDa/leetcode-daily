class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        left = 0
        right = int(math.sqrt(c))
        while left <= right :
            a = left*left
            b = right*right
            if c == (a+b):
                return True
            elif c < (a+b):
                right -=1
            else:
                left += 1
        return False

        