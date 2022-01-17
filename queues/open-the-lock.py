# 752. Open the Lock

# You have a lock in front of you with 4 circular wheels. Each wheel has 10 slots: '0', '1', '2', '3', '4', '5', '6', '7', '8', '9'. 
# The wheels can rotate freely and wrap around: for example we can turn '9' to be '0', or '0' to be '9'. Each move consists of turning one wheel one slot.
# The lock initially starts at '0000', a string representing the state of the 4 wheels.
# You are given a list of deadends dead ends, meaning if the lock displays any of these codes, 
# the wheels of the lock will stop turning and you will be unable to open it.
# Given a target representing the value of the wheels that will unlock the lock, 
# return the minimum total number of turns required to open the lock, or -1 if it is impossible.


from collections import deque

class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        #account for the cases if the starting value is in the deadends
        if '0000' in deadends:
            return -1
        #account for the case if the target value is the starting parameter
        if target == '0000':
            return 0
        visited = set()
        queue = deque()
        queue.append(('0000', 0))
        iteration = 0
        def get_possible_combinations(lock):
            for i in range(4):
                x = int(lock[i])
                for d in (-1,1):
                    y = (x+ d) % 10 #this is because each slot should be between 0 and 9
                    yield lock[:i] + str(y) + lock[i+1:] #generator
        
        while queue:
            iteration += 1
            for _ in range(len(queue)):
                lock, step = queue.popleft()
            
                for direction in get_possible_combinations(lock):
                    if direction in visited:
                        continue
                    if direction in deadends:
                        continue
                    elif direction == target: return iteration
                    else:
                        visited.add(direction)
                        queue.append((direction, iteration))
                # print(queue)
        return -1