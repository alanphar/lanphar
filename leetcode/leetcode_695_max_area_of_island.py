class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        """Main loop should find a 1 and start DFS."""
        max_area = 0

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                area = 1
                if grid[i][j]:
                    area = dfs(i, j, grid)
                    max_area = max(max_area, area)
        return max_area
    
def dfs(row, column, grid):
    """Count the current cell and check adjacents."""
    if row < 0 or row >= len(grid) or column < 0 or column >= len(grid[0]) or not grid[row][column]:
        return 0
    
    # sink the island :) 
    grid[row][column] = 0

    return 1 + dfs(row + 1, column, grid) + dfs(row - 1, column, grid) + dfs(row, column - 1, grid) + dfs(row, column + 1, grid)
