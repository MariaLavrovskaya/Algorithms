# Given an array of intervals where intervals[i] = [starti, endi], merge all overlapping intervals, 
# and return an array of the non-overlapping intervals that cover all the intervals in the input.



class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
#         sort the list by the first index
        intervals.sort(key=lambda x:x[0])
        merged = []
#         for every interval in our list
        for interval in intervals:
#         if merged list is empty or the the start value of the interval does not overlap 
            if not merged or merged[-1][1] < interval[0]:
                merged.append(interval)
#            if interval[0] overlaps with the previous interval or the start of a new interval is the finish of an old interval
            else:
                merged[-1][1] = max(merged[-1][1], interval[1])
        return merged