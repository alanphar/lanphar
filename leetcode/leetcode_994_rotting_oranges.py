from collections import deque

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        self.queue = deque()
        min_time = self.fresh_count = 0

        for row in range(len(grid)):
            for column in range(len(grid[0])):
                if grid[row][column] == 1:
                    self.fresh_count += 1
                elif grid[row][column] == 2:
                    self.queue.append((row, column))
        
        while self.queue and self.fresh_count > 0:
            rotten_count = len(self.queue)
            for _ in range(rotten_count):
                rotten_row, rotten_col = self.queue.popleft()
                if rotten_row > 0 and grid[rotten_row - 1][rotten_col] == 1:
                    self.rot_it(grid, rotten_row - 1, rotten_col)
                if rotten_row + 1 < len(grid) and grid[rotten_row + 1][rotten_col] == 1:
                    self.rot_it(grid, rotten_row + 1, rotten_col)
                if rotten_col + 1 < len(grid[0]) and grid[rotten_row][rotten_col + 1] == 1:
                    self.rot_it(grid, rotten_row, rotten_col + 1)
                if rotten_col > 0 and grid[rotten_row][rotten_col - 1] == 1:
                    self.rot_it(grid, rotten_row, rotten_col - 1)
            min_time += 1
        
        if self.fresh_count == 0:
            return min_time
        else:
            return -1
                
                    
    def rot_it(self, grid, row, col):
        grid[row][col] = 2
        self.fresh_count -= 1
        self.queue.append((row, col))
