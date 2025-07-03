class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        left = 0 #buying
        right = 0 #selling
        maxP = 0

        while right < len(prices):
            if prices[left] < prices[right]:
                profit = prices[right] - prices[left]
                maxP = max(maxP,profit)

            else:
                left = right
            right += 1

        return maxP


