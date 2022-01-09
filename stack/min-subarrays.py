class Solution:
    def sumSubarrayMins(self, arr: List[int]) -> int:
        stack = []
        start = 0
        
        for end in range(len(arr)+1):
            start = 0
            while start < end:
                stack.append(min(list(arr[start:end])))
                start += 1
        
        return sum(stack) % (10 **9 + 7)