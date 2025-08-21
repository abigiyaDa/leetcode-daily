class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people.sort(reverse=True)
        count = 0
        i = 0
        last = len(people)-1
        while i <= last:
            if (people[i]+people[last]) <= limit:
                last -= 1
            count +=1
            i+=1
        return count

        

                
        