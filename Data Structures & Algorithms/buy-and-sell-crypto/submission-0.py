class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        l =0
        r=1
        max_profit =0 
        while r < n:
            if prices[r] > prices[l]:
                profit = prices[r] - prices[l]
                max_profit = max(max_profit,profit)
            else:
                l = r
            r += 1
        return max_profit


        

        