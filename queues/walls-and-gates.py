# 286. Walls and Gates

# You are given an m x n grid rooms initialized with these three possible values.

# -1 A wall or an obstacle.
# 0 A gate.
# INF Infinity means an empty room. We use the value 231 - 1 = 2147483647 
# to represent INF as you may assume that the distance to a gate is less than 2147483647.
# Fill each empty room with the distance to its nearest gate. 
# If it is impossible to reach a gate, it should be filled with INF.


from collections import deque 

class Solution:
    def wallsAndGates(self, rooms: List[List[int]]) -> None:
        """
        Do not return anything, modify rooms in-place instead.
        """
        #We first need to identify locations of the gates
        queue = deque()
        max_row = len(rooms)
        max_col = len(rooms[0])
        visited = set()
        directions = [(-1,0), (0,-1), (0,1), (1,0)]
        iteration = 0
        def get_neighbours(row,col):
            nonlocal directions
            for row_difference, col_difference in directions:
                new_row = row + row_difference
                new_col = col + col_difference
                if not (0 <= new_row < max_row and 0 <= new_col < max_col):
                    continue
                # if grid[new_row][new_col] == 0:
                #     continue
                if rooms[new_row][new_col] == -1:
                    continue
                if rooms[new_row][new_col] == 2147483647:
                    yield (new_row, new_col)
        
        for row in range(len(rooms)):
            for cell in range(len(rooms[row])):
                if rooms[row][cell] == 0:
                    queue.append((row, cell))
                    visited.add((row, cell))
                else: 
                    continue 
        while queue: 
            iteration += 1
            for _ in range(len(queue)):
                current_row, current_col = queue.popleft()
                for neightbor_row, neightbor_col in get_neighbours(current_row, current_col):
                    if (neightbor_row, neightbor_col) in visited:
                        continue
                    queue.append((neightbor_row, neightbor_col))
                    rooms[neightbor_row][neightbor_col] = iteration
        return rooms
                
            

        