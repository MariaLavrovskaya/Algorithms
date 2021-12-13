# You are given an m x n grid where each cell can have one of three values:

# 0 representing an empty cell,
# 1 representing a fresh orange, or
# 2 representing a rotten orange.
# Every minute, any fresh orange that is 4-directionally adjacent to a rotten orange becomes rotten.




from collections import deque 
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        
#     Strategy to solve this question. We first need to find all the locations of the rotten oranges of the matrix and the number of fresh oranges in the matrix. Then we should start a loop of rottening. 
        fresh_oranges = 0
        locations_of_rotten = []
        visited = set()
        queue = deque()
        minutes = 0
        max_row = len(grid)
        max_col = len(grid[0])
        
        
        for row in range(len(grid)): 
            for cell in range(len(grid[row])): 
                if grid[row][cell] == 1:
                    fresh_oranges +=1
                if grid[row][cell] == 2:
                    queue.append((row,cell))
        if fresh_oranges == 0:
            return fresh_oranges
                
        directions = [(-1,0), (0,-1), (0,1), (1,0)]
        def get_neighbours(row,col):
            nonlocal directions, fresh_oranges
            for row_difference, col_difference in directions:
                new_row = row + row_difference
                new_col = col + col_difference
                if not (0 <= new_row < max_row and 0 <= new_col < max_col):
                    continue
                if grid[new_row][new_col] == 0:
                    continue
                if grid[new_row][new_col] == 2:
                    continue
                # fresh_oranges -= 1
                yield (new_row, new_col)
        
        while queue: 
            minutes +=1
            print(minutes)
            print('Length', len(queue))
            number_of_nodes = len(queue)
            for _ in range(len(queue)):
                row, col = queue.popleft()
                visited.add((row,col))
                for neighbour_row, neightbor_col in get_neighbours(row,col):
                    if (neighbour_row, neightbor_col) in visited:
                        print(visited)
                        continue
                    queue.append((neighbour_row, neightbor_col))
                    fresh_oranges -= 1
                    # visited.add((row,col))
        print(fresh_oranges)
        if fresh_oranges == 0:
            return minutes -1
        else:
            return -1
