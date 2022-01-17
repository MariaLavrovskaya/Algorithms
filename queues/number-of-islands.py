# 200. Number of Islands

# Given an m x n 2D binary grid grid which represents a map of '1's (land) and '0's (water), return the number of islands.

# An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically. 
# You may assume all four edges of the grid are all surrounded by water.


from collections import deque

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid: return 0
        number_rows = len(grid)
        number_cols = len(grid[0])
        result = 0
        queue = deque()
        directions = [(-1,0), (0,-1), (0,1), (1,0)]
        

        
        
        
        for row in range(number_rows):
            for col in range(number_cols):
                if grid[row][col] == '1':
                    queue.append((row, col))
                    grid[row][col] = '0'
                    while queue: 
                        current_row, current_col = queue.popleft()
                        for dx, dy in directions:
                            xx, yy = current_row+dx, current_col+dy
                            if 0 <= xx < number_rows and 0 <= yy < number_cols and grid[xx][yy] == '1':
                                queue.append((xx, yy))
                                grid[xx][yy] = '0'
                    result += 1
        return result

