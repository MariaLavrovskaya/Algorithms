# Given an array of integers temperatures represents the daily temperatures, return an array answer such that answer[i] is the number of days you have to wait after the ith day to get a warmer temperature. If there is no future day for which this is possible, keep answer[i] == 0 instead.

#Here the approach is to fill in the result array as we go along. The approach is implemented using the decreasing monotonic stack, where the elements are always in sorted order. We can use a monotonic decreasing stack to hold temperatures. Monotonic decreasing means that the stack will always be sorted in descending order. 
# We calculate the days it took to get warmer as we go along. The stack maintains the index of the temperature, not the temperature itself. Once we enocunter the element that is greater than the last element in the stack, we pop the element and calculate days from indices. Otherwise, we append the value to the stack.

# On each day, there are two possibilities. If the current day's temperature is not warmer than the temperature on the top of the stack, we can just push the current day onto the stack - since it is not as warm (equal or smaller), this will maintain the sorted property.

# If the current day's temperature is warmer than the temperature on top of the stack, this is significant. It means that the current day is the first day with a warmer temperature than the day associated with the temperature on top of the stack. When we find a warmer temperature, the number of days is the difference between the current index and the index on the top of the stack. We can declare an answer array before iterating through the input and populate answer as we go along.

# When we find a warmer temperature, we can't stop after checking only one element at the top. Using the example temperatures = [75, 71, 69, 72], once we arrive at the last day our stack looks like stack = [0, 1, 2]. For clarity, here's what the stack looks like with each temperature associated with the day: stack = [(0, 75), (1, 71), (2, 69)]. 72 (the current temperature) is greater than 69, but it is also greater than 71. To make sure we don't miss any days, we should pop from the stack until the top of the stack is no longer colder than the current temperature. Once that is the case, we can push the current day onto the stack.




# class Solution:
    # """Naive implementation"""

#     def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        # def get_warmer_days(count, value, stack):
#             count=count
#             if count == len(temperatures):
#                 return 0
#             if temperatures[count] > value:
#                 print(temperatures[count], count)
#                 return count
#             else:
#                 print(value)
#                 count +=1
#                 count = get_warmer_days(count, value, stack)
            
            
class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        n = len(temperatures)
        answer = [0]*n
        stack = []
        for curr_day, curr_temp in enumerate(temperatures):
            while stack and temperatures[stack[-1]] < curr_temp:
                prev_day = stack.pop()
                answer[prev_day] = curr_day - prev_day

            stack.append(curr_day)
        
        return answer

        