from typing import List
import pdb


class Solution:
    def onesMinusZeros(self, grid: List[List[int]]) -> List[List[int]]:
        row, col = len(grid), len(grid[0])

        ones_row = [0]*row
        ones_col = [0]*col

        for i in range(row):
            for j in range(col):
                ones_row[i] += grid[i][j]
                ones_col[j] += grid[i][j]

        for i in range(row):
            for j in range(col):
                grid[i][j] = 2*(ones_row[i]+ones_col[j]) - col-row

        return grid


s = Solution()

res = s.onesMinusZeros(
    [
        [0, 1, 1],
        [1, 0, 1],
        [0, 0, 1]
    ]
)

dic = {
    'id': 1,
    'name': 'ali',
    'age': 15
}


arr = [
    [0, 1, 1],
    [1, 0, 1],
    [0, 0, 1]
]


for i in zip(*arr):
    print(i)