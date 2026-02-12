class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people.sort()
        first, last = 0, len(people)-1
        count = 0
        while first <= last:
            if people[first] + people[last] <=limit:
                count +=1
                first +=1
                last-=1
            elif people[first] < people[last]:
                count +=1 
                last -=1
            else:
                count += 1
                first +=1 
        return count  
