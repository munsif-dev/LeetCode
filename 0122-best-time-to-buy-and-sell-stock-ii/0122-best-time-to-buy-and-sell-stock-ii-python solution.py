class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        n = len(prices)
        profit = 0
        buy = prices[0]

        for i in range(1,n):
            if prices[i] > buy:
                profit += prices[i] - buy
                buy = prices[i]
            else:
                buy = prices[i]
        return profit
        