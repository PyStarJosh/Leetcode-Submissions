class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        res = 0

        for idx in range(len(prices) - 1):
            diff = prices[idx + 1] - prices[idx]

            if diff > 0:
                res += diff
        
        return res
