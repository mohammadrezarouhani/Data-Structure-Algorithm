import pprint


def longest_common_subsequence(string1, string2):
    grid = [[0 for s2 in string2] for s1 in string1]

    for i, s1 in enumerate(string1):
        for j, s2 in enumerate(string2):
            if s1 == s2:
                if i > 0 and j > 0:
                    grid[i][j] = grid[i - 1][j - 1] + 1
                else:
                    grid[i][j] += 1
            else:
                if i > 0 and j > 0:
                    grid[i][j] = max(grid[i - 1][j], grid[i][j - 1])
                elif i > 0:
                    grid[i][j] = grid[i - 1][j]
                elif j > 0:
                    grid[i][j] = grid[i][j - 1]

    print(pprint.pformat(grid, width=20))
    return grid[-1][-1]


print(longest_common_subsequence("fish", "fosh"))
