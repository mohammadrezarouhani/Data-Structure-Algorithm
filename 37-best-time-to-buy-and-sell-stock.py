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
import pprint


def sell_and_buy_method1(report: list):
    report_mapper = [(index, price) for index, price in enumerate(report)]
    report_sorted_mapper = sorted(report_mapper, key=lambda key: key[1])
    result = None
    max_profit = 0

    for i, r1 in report_sorted_mapper:
        for j, r2 in report_sorted_mapper[::-1]:
            if r2 - r1 > max_profit and j > i:
                max_profit = r2 - r1
                result = (i, j)

    return result


def sell_buy_method2(report: list):
    temp = report.copy()
    max_profit = 0
    result = None

    for i, price in enumerate(report):
        temp.pop(i)
        max_value = max(temp)
        new_calculate = max_value - price

        if new_calculate > max_profit:
            max_profit = new_calculate
            result = i, report.index(max_value)

    return result


def sell_and_buy_dynamic_programming(report: list):
    grid = [[r2 for r2 in report] for r1 in report]
    max_profit = 0
    result = None

    for i, r1 in enumerate(report):
        for j, r2 in enumerate(report):
            grid[i][j] = r2 - r1
            if grid[i][j] > max_profit and j > i:
                max_profit = grid[i][j]
                result = (i + 1, j + 1)

    print(pprint.pformat(grid, width=40))
    return result


print(sell_and_buy_dynamic_programming([10, 9, 8, 5, 7, 10, 6, 8]))
