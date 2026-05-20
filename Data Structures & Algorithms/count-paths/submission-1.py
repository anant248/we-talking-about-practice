class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
         # going to fill out the grid from bottom right to top left
         # return the value in top left
         # the way to reach bottom right from a cell is
            # of ways to its right + # of ways to its bottom

        # make a 2d grid of ones
        grid = [[1 for _ in range(n)] for _ in range(m)]

        # fill starting from m - 2, n - 2
        for row in range(m - 2, -1, -1):
            for col in range(n - 2, -1, -1):
                grid[row][col] = grid[row + 1][col] + grid[row][col + 1]
        
        return grid[0][0]