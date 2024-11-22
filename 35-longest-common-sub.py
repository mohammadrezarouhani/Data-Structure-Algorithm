# solving with dynamic programing

import pprint


def longest_common_substring(string1, string2):
    grid = [[0 for s2 in string2] for s1 in string1]
    longest_string = 0

    for i, s1 in enumerate(string1):
        for j, s2 in enumerate(string2):
            if i > 0 and j > 0 and s1 == s2:
                grid[i][j] = grid[i - 1][j - 1] + 1

            elif s1 == s2:
                grid[i][j] += 1

            if grid[i][j] > longest_string:
                longest_string += 1

    print(pprint.pformat(grid, width=20))
    return longest_string


print(longest_common_substring("fish", "hish"))
