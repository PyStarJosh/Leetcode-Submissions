class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        if len(people) == 1:
            return 1
            
        people.sort()
        boats = 0
        left, right = 0, len(people) - 1

        while left <= right:
            pair_weight = people[left] + people[right]
            boats += 1

            if pair_weight <= limit:
                left += 1
                right -= 1

            else:
                right -= 1
                    
        return boats
