class Solution:
    def dividePlayers(self, skill: List[int]) -> int:
        skill.sort()
        first,last = 0, len(skill)-1 
        x = skill[first] + skill[last]
        res = 0

        while first < last :
            if (skill[first] + skill[last]) != x:
                return -1
            res += (skill[first] * skill[last])
            first +=1
            last -= 1
        return res

# Sort → O(n log n)
# Two pointer scan → O(n)
# Space → O(1) (ignoring sort)