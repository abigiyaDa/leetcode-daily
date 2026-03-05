class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False 
        x = str(x)
        reverse = x[::-1]

        return x == reverse
