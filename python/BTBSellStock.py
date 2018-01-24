# -*- coding:utf-8 -*-

# @Author zpf
"""
Say you have an array for which the ith element is the price of a given stock on day i.

If you were only permitted to complete at most one transaction (ie, buy one and sell one share of the stock), design an algorithm to find the maximum profit.

Example 1:
Input: [7, 1, 5, 3, 6, 4]
Output: 5

max. difference = 6-1 = 5 (not 7-1 = 6, as selling price needs to be larger than buying price)
Example 2:
Input: [7, 6, 4, 3, 1]
Output: 0

In this case, no transaction is done, i.e. max profit = 0.
"""


class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        max_profit = 0
        if len(prices) < 2:
            pass
        elif len(prices) == 2:
            max_profit = prices[1] - prices[0] if prices[1] > prices[0] else 0
        elif len(prices) > 2:
            flag = 0
            i = 0
            j = i + 1
            while j != len(prices):
                if prices[i] >= prices[j]:
                    i = j
                    j = i + 1
                elif prices[i] < prices[j]:
                    temp = prices[j] - prices[i]
                    if temp > max_profit:
                        max_profit = temp
                    j += 1
        return max_profit

if __name__ == "__main__":
    sample = Solution()
    print(sample.maxProfit([1, 2, 4]))
