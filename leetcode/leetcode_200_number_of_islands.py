"""Given an m x n 2D binary grid grid which represents a map of '1's (land) and '0's (water), return the number of islands.

An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically. You may assume all four edges of the grid are all surrounded by water.

Example 1:

Input: grid = [
  ["1","1","1","1","0"],
  ["1","1","0","1","0"],
  ["1","1","0","0","0"],
  ["0","0","0","0","0"]
]
Output: 1

Example 2:

Input: grid = [
  ["1","1","0","0","0"],
  ["1","1","0","0","0"],
  ["0","0","1","0","0"],
  ["0","0","0","1","1"]
]
Output: 3

My solution
Runtime 232ms Beats 86.58% 
Memory 21.51MB Beats72.61%
"""
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        num_islands = 0
        for row in range(len(grid)):
            for column in range(len(grid[0])):
                if grid[row][column] == "1":
                    num_islands += 1
                    sink_the_island(grid, row, column)
        return num_islands


def sink_the_island(grid, row, column):
    if row < 0 or column < 0 or row >= len(grid) or column >= len(grid[0]) or grid[row][column] != "1":
        return
    grid[row][column] = "0"
    sink_the_island(grid, row + 1, column)
    sink_the_island(grid, row - 1, column)
    sink_the_island(grid, row, column + 1)
    sink_the_island(grid, row, column - 1)
