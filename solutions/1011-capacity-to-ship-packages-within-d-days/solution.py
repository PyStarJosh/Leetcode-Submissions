class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        left = max(weights)
        right = sum(weights)

        while left <= right:
            cap = left + (right - left) // 2
            curr_weight = 0
            time = 1
            
            for pck_weight in weights:
                curr_weight += pck_weight
                if curr_weight > cap:
                    time += 1
                    curr_weight = pck_weight
          
            if time <= days:
                ans = cap
                right = cap - 1
            else:
                left = cap + 1
        
        return ans
