import sys

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l, w, profit, maxProfit = 0, 0, 0, 0
        r = 1
        sub = lambda a, b: b - a
        
        while r < len(prices):
            if prices[l] > prices[r]:
                l += 1
                continue
            profit = sub(prices[l], prices[r])
            maxProfit=max(maxProfit, profit)
            r += 1

        return maxProfit






