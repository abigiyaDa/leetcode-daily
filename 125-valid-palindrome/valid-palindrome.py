class Solution:
    def isPalindrome(self, s: str) -> bool:
        # filtter only the letters and convert it to lower case .lower()
        letters_only = ''.join(ch for ch in s if ch.isalnum()).lower()
        first = 0
        last = len(letters_only)-1
        if len(letters_only) == 1:
            return True
        while first<last:
            if letters_only[first] == letters_only[last]:
                first += 1
                last -=1
            else:
                return False
        return True


        