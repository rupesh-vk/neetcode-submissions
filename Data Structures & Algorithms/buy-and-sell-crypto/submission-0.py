class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        result = float("-inf")
        low = high = prices[0]
        for price in prices:
            if price < low:
                low = high = price
            if price > high:
                high = price
            result = max(result, high - low)
        return result
            
        