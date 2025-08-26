class Solution:
    def isPalindrome(self, s: str) -> bool:
        # # time o(n) space o(1)
        # # filtter only the letters and convert it to lower case .lower()
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

        # # time o(n) space o(1)
        # i, j = 0, len(s) - 1
        # while i < j:
        #     # skip non-alphanumeric characters
        #     while i < j and not s[i].isalnum():
        #         i += 1
        #     while i < j and not s[j].isalnum():
        #         j -= 1

        #     # compare in lowercase
        #     if s[i].lower() != s[j].lower():
        #         return False

        #     i += 1
        #     j -= 1
        # return True      
