class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        # reason (a+b)2=a2+b2+2ab
        left = 0
        right = int(math.sqrt(c))
        while left<=right:
            current = left*left + right*right
            if c == current:
                return True
            elif current < c:
                left+=1
            else:
                right -= 1
        return False
        