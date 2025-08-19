class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        res = ""
        for i in range(len(strs[0])):
            for s in strs:
                #if strs[0][i] this specific letter must equals s[i] if so continue else return res
                # what if s[i] is out of bound check if i == len(s)
                if i == len(s) or s[i] != strs[0][i]:
                    return res
            res+= strs[0][i]
        return res


        # a = strs[0]  
        # temp = ""    

        # for i in range(len(a)):
        #     current_char = a[i]  
        #     match = True
        #     for j in range(1, len(strs)):
        #         if i >= len(strs[j]) or strs[j][i] != current_char:
        #             match = False
        #             break

        #     if match:
        #         temp += current_char
        #     else:
        #         break  

        # return temp


        