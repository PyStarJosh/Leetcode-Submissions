class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        left, right = 1, max(piles)

        while left <= right:
            k = left + (right - left) // 2
            total_time = 0
            
            for pile in piles:
                total_time += (pile + k - 1) // k

            if total_time <= h:
                ans = k
                right = k - 1
            else:
                left = k + 1
        
        return ans
