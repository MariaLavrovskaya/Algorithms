# Given a stream of integers and a window size, calculate the moving average of all integers in the sliding window.

# Implement the MovingAverage class:

# MovingAverage(int size) Initializes the object with the size of the window size.
# double next(int val) Returns the moving average of the last size values of the stream.

class MovingAverage:

    def __init__(self, size: int):
        self.queue = [0]*size
        self.size = size
        self.head = 0
        self.count = 0

    def next(self, val: int) -> float:
#         If the count of the array is equal to the allowed size of the queue, we need to dequeue one element and then add one element in the end
        if self.count == self.size:
            self.head = (self.head + 1) % self.size
            self.count -=1
#         This is the adding step in the end of the queue 
        self.queue[(self.head + self.count) % self.size] = val
#          We increment the count because we have just added the element
        self.count += 1

        return sum(self.queue) / self.count 