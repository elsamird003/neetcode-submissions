class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # Start the minimum price as infinitely high so the first price becomes the new minimum
        min_price = float('inf') 
        # Start max profit at 0 (if we can't make a profit, we return 0)
        max_profit = 0
        
        # Notice we don't even need enumerate() here! 
        # We just need the actual prices.
        for price in prices:
            # 1. Is this the cheapest price we've seen so far?
            if price < min_price:
                min_price = price
                
            # 2. If it's not the cheapest day to buy, is it a good day to sell?
            # Check if selling today gives us a bigger profit than we've seen before.
            elif price - min_price > max_profit:
                max_profit = price - min_price
                
        # Return the actual profit amount, not the price itself!
        return max_profit