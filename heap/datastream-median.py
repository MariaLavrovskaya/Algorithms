# The median is the middle value in an ordered integer list. If the size of the list is even, there is no middle value and the median is the mean of the two middle values.

# For example, for arr = [2,3,4], the median is 3.
# For example, for arr = [2,3], the median is (2 + 3) / 2 = 2.5.
# Implement the MedianFinder class:

# MedianFinder() initializes the MedianFinder object.
# void addNum(int num) adds the integer num from the data stream to the data structure.
# double findMedian() returns the median of all elements so far. Answers within 10-5 of the actual answer will be accepted.

# The following approach is different from the solutions that use sorting algorithms and then do the insertation step. The following approach relies 
# on maintaining two heaps (minheap and maxheap). 


from heapq import _siftdown_max

class MedianFinder:

    def __init__(self):
        self.hi = [] #containts all the larger numbers (min_heap)
        self.lo = [] #contains all the smaller numbers (max_heap)
        heapq.heapify(self.hi)
        heapq._heapify_max(self.lo)
        
        
    def addNum(self, num: int) -> None:
        def heappush_max(heap, item):
            """Push item onto heap, maintaining the heap invariant."""
            heap.append(item)
            _siftdown_max(heap, 0, len(heap) - 1)
        
        heappush_max(self.lo, num)
        heapq.heappush(self.hi, heapq._heappop_max(self.lo))
        if len(self.lo) < len(self.hi):
            heappush_max(self.lo, heapq.heappop(self.hi))                  

    def findMedian(self) -> float:
        return self.lo[0] if len(self.lo) > len(self.hi) else (self.lo[0] + self.hi[0]) / 2
