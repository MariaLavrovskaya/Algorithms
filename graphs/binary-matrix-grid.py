from collections import deque

# Given an n x n binary matrix grid, return the length of the shortest clear path in the matrix. If there is no clear path, return -1.

# A clear path in a binary matrix is a path from the top-left cell (i.e., (0, 0)) to the bottom-right cell (i.e., (n - 1, n - 1)) such that:

# All the visited cells of the path are 0.
# All the adjacent cells of the path are 8-directionally connected (i.e., they are different and they share an edge or a corner).
# The length of a clear path is the number of visited cells of this path.

# Approach 1: Using matrix and changing distance in place. BFS is performed on the matrix to find the shortest path. We recall, that the BGS works as follows: we first "process" the root node, then we add all neighbors width-wise to the queue. In this case, once the get_neighbors() this means that the node is processed. 

class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        max_row = len(grid)-1
        max_col = len(grid[0]) - 1
#         We first determine the directions where we can go on the grid
        directions = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)] 
    
#     We check whether the problem condition holds, otherwise we return -1
        if grid[0][0] != 0 or grid[len(grid)-1][len(grid[0])-1] !=0:
            return -1
    
    
        def get_neighbors(row, col):
            nonlocal grid, directions
            for row_difference, col_difference in directions:
                new_row = row + row_difference
                new_col = col + col_difference
                # print(neighbor_row, neighbor_col)
                if not (0 <= new_row <= max_row and 0 <= new_col <= max_col):
                    continue
                if grid[new_row][new_col] != 0:
                    continue 
                yield (new_row, new_col)


        
#         Set up the BFS to find the shortest path
        queue = deque()
        queue.append((0,0))
        grid[0][0] = 1
        
        while queue: 
            row, col = queue.popleft()
            distance = grid[row][col]
            if (row, col) == (max_row, max_col):
                return distance
#             That is the step to process the current node
            for neighbor_row, neighbor_col in get_neighbors(row, col):
                grid[neighbor_row][neighbor_col] = distance + 1
                queue.append((neighbor_row, neighbor_col))
        
        return -1
    
# Approach 2: If we do not want to replace the initial grid matrix. We use the visited to keep track of the values that we have already visited. 
class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        max_row = len(grid)-1
        max_col = len(grid[0]) - 1
#         We first determine the directions where we can go on the grid
        directions = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)] 
    
#     We check whether the problem condition holds, otherwise we return -1
        if grid[0][0] != 0 or grid[len(grid)-1][len(grid[0])-1] !=0:
            return -1
    
    
        def get_neighbors(row, col):
            nonlocal grid, directions
            for row_difference, col_difference in directions:
                new_row = row + row_difference
                new_col = col + col_difference
                # print(neighbor_row, neighbor_col)
                if not (0 <= new_row <= max_row and 0 <= new_col <= max_col):
                    continue
                if grid[new_row][new_col] != 0:
                    continue 
                yield (new_row, new_col)


        
#         Set up the BFS to find the shortest path
        queue = deque()
        visited = set() #to mitigate ambiguity, we create set using set(), not curly braces
        queue.append((0,0,1))
        visited.add((0,0))
        
        while queue: 
            row, col,distance = queue.popleft()
            if (row, col) == (max_row, max_col):
                return distance
            for neighbor_row, neighbor_col in get_neighbors(row, col):
                if (neighbor_row, neighbor_col) in visited:
                    continue
                visited.add((neighbor_row, neighbor_col))
                queue.append((neighbor_row, neighbor_col,distance+1))
        
        return -1