# Problem: Best Time to Buy and Sell Stock
#
# You are given an array 'report' where each element represents the price of a good on that day.
# The goal is to find the best day to buy and the best day to sell such that the profit is maximized.
#
# Key Concept:
# 1. You can only buy before you sell, i.e., the buy day must come before the sell day.
# 2. We need to maximize the difference between the sell price and the buy price.
#
# Approach:
# - We first sort the prices to identify possible buy and sell days.
# - We create a dictionary `report_dict` where the keys are the prices and values are their respective indices in the original array.
# - We iterate through all possible price pairs where the price on the "buy day" is less than the price on the "sell day".
# - For each valid pair, we calculate the profit (sell price - buy price) and track the maximum profit.
# - The result will be the day indices (1-based) of the best buy and sell days.
#
# Edge Case:
# - If no profit can be made (prices are in decreasing order), return None.


# solution greedy algorithm
def sell_and_buy(report: list):
    report_sorted = sorted(report)
    report_dict = {price: index for index, price in enumerate(report)}
    result = None
    max_profit = 0

    for i in report_sorted:
        for j in report_sorted[::-1]:
            if report_dict[i] < report_dict[j] and j - i > max_profit:
                max_profit = j - i
                result = report_dict[i] + 1, report_dict[j] + 1

    return result


print(sell_and_buy([10, 9, 8, 5, 7, 10, 6, 8]))
