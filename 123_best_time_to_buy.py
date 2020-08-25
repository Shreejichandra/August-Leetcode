'''Say you have an array for which the ith element is the price of a given stock on day i.

Design an algorithm to find the maximum profit. You may complete at most two transactions.

Note: You may not engage in multiple transactions at the same time (i.e., you must sell the stock before you buy again).'''

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        k = 2
        profit = [[0 for i in range(n + 1)]  
                 for j in range(k + 1)]  
  
    # Fill the table in bottom-up fashion  
        for i in range(1, k + 1):  
            prevDiff = float('-inf') 

            for j in range(1, n):  
                prevDiff = max(prevDiff, 
                               profit[i - 1][j - 1] - 
                               prices[j - 1])  
                profit[i][j] = max(profit[i][j - 1],  
                                   prices[j] + prevDiff)  

        return profit[k][n - 1]  
