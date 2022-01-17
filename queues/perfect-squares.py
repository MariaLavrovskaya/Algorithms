# 279. Perfect Squares
# Given an integer n, return the least number of perfect square numbers that sum to n.

# A perfect square is an integer that is the square of an integer; in other words, it is the product of some integer with itself. 
# For example, 1, 4, 9, and 16 are perfect squares while 3 and 11 are not.



from collections import deque

class Solution:
    def numSquares(self, n: int) -> int:
        square_nums = [i**2 for i in range(0, int(math.sqrt(n))+1)]
        queue = deque()
        level = 0
        queue.append((n, level))
        def get_leaf(value):
            nonlocal square_nums
            for number in square_nums:
                if value - number < 0:
                    continue
                else:
                    yield value - number
        
        while queue: 
            level+= 1
            for _ in range(len(queue)):
                current, elevation = queue.popleft()
                
                for element in get_leaf(current):
                    if element == 0: return level
                    else: 
                        queue.append((element,level))
        return -1