# 84. Largest Rectangle in Histogram

# Given an array of integers heights representing the histogram's bar height 
# where the width of each bar is 1, return the area of the largest rectangle in the histogram.

class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        
        """ The trick of this problem that has not been stated in the problem description is to consider all possible triangles of a given heights.
        The idea is to use the current element as the height and consider all possible widths for this height. The trisk is to realise how should we                calculate the width. We use idx-1 for the right boundary and stack[-1] as the left boundary, because we are ensured that stack[-1] is definitely smaller than the element that we popped out but we do not know whether the bar is actually smaller than stack[-1], so we would need to check this condition. 
        
        """
        if len(heights) == 1:
            return heights[0]
        heights = heights + [0]
        stack = [-1]
        greatest_value = 0
        for idx, bar in enumerate(heights):
            while bar < heights[stack[-1]]:
                candidate = stack.pop() 
                print(heights[candidate], idx, idx-1 - stack[-1], stack[-1])
                greatest_value = max(greatest_value, heights[candidate]*(idx-1 - stack[-1]))

            if heights[stack[-1]]*2 >= greatest_value:
                greatest_value = heights[stack[-1]]*2
            stack.append(idx)
        # if heights[stack[-1]] > greatest_value:
        #     return heights[stack[-1]]
        return greatest_value
                
