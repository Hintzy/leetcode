

# FIRST SOLUTION.  TOO SLOW
# def maxProfit(prices):
#     max_profit = 0
#     for i, price in enumerate(prices[:-1]):
#         profit = max(prices[i+1:]) - price
#         if profit > max_profit:
#             max_profit = profit
#     return max_profit
# print(maxProfit(rices))


#  SECOND ATTEMPT.  STILL TOO SLOW
# def maxProfit(prices):
#     max_profit = 0
#     min = prices[0]
#     maxi = max(prices[1:])
#     for i, price in enumerate(prices[:-1]):
#         if price < min:
#             min = price
#         if price == maxi:
#             maxi = max(prices[i+1:])
#         profit = maxi - min
#         if profit > max_profit:
#             max_profit = profit
#     return max_profit


# THIRD ATTEMPT
from math import ceil
# Sorting Method Attempt. Still in progress.
# def maxProfit(prices):
#     sorted_prices = []
#     max_profit = 0
#     for i, price in enumerate(prices):
#         sorted_prices.append((price, i))
#     sorted_prices = sorted(sorted_prices)
#     for i in range(len(sorted_prices)-1):
#         if sorted_prices[-i-1][1] > sorted_prices[i][1]:
#             max3 = sorted_prices[-i-1][0] - sorted_prices[i][0]
#             if max3 > 0:
#                 return max3
#         elif sorted_prices[-i-1][1] > sorted_prices[i+1][1]:
#             max1 = sorted_prices[-i - 1][0] - sorted_prices[i + 1][0]
#             if max1 > 0:
#                 return max1
#         elif sorted_prices[-i-2][1] > sorted_prices[i][1]:
#             max2 = sorted_prices[-i - 2][0] - sorted_prices[i][0]
#             if max2 > 0:
#                 return max2
#     return max_profit
#

from test_cases import tests, test_series

# def maxProfit(prices):
#     """
#     :type prices: List[int]
#     :rtype: Int
#     """
#     min_price = float('inf')
#     max_profit = 0
#     for price in prices:
#         if price < min_price:
#             min_price = price
#         else:
#             max_profit = max(max_profit, price - min_price)
#     return max_profit
#
# test_series(maxProfit, tests)

"""
Redoing problem from scratch for review:

Logic - Two pointers (low & high).  
Iterate though all elements in the list. Low is the running minimum of values in the list.  Max is the running max until
a new low is found, then the max is set equal to that current new low.
"""

def max_profit(prices: list[int]) -> int:
    low, high = prices[0], prices[0]
    max_profit = 0
    for price in prices:
        if price < low:
            low = price
        else:
            max_profit = max(max_profit, (price-low))
    return max_profit

test_1 = [1,7,19,6,4,3,1, 55]
print(max_profit(test_1))

