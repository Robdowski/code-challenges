"""
This problem asks to keep a running total of the sum of a 1 dimensional array, and add that sum to each item in the array as we traverse.

To do this, we can simply declare a variable, running sum, and add it to each item in the array as we traverse. We need to add the sum to the item in the array, while storing the original value of the item in a temporary
variable to add to the running sum.

Example output [1, 2, 3, 4] --> [1, 3, 6, 10]

Runtime Complexity: O(n)
Space Complexity: O(1)
"""

class Solution:
    def runningSum(self, nums):
        running_sum = 0
        
        for i in range(len(nums)):
            temp = nums[i]
            nums[i] += running_sum
            running_sum += temp
        
        return nums