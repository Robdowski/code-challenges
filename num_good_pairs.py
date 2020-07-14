"""
TASK:
Given an array of integers nums.

A pair (i,j) is called good if nums[i] == nums[j] and i < j.

Return the number of good pairs.

Example 1:

Input: nums = [1,2,3,1,1,3]
Output: 4
Explanation: There are 4 good pairs (0,3), (0,4), (3,4), (2,5) 0-indexed.

Example 2:

Input: nums = [1,1,1,1]
Output: 6
Explanation: Each pair in the array are good.

Example 3:

Input: nums = [1,2,3]
Output: 0

Constraints:

    1 <= nums.length <= 100
    1 <= nums[i] <= 100

"""

"""
SOLUTION:
Runtime: O(2n)
Space: O(n)

Process:
1. Create a lookup table to add items to in the form of ITEM: [INDICES], create a counter variable which starts at 0 to return
2. Loop through array, adding items to lookup table in form above
3. Loop through values of lookup table and determine number of possible combinations based upon length of array
4. Add number of possible combinations to the value which will be returned from the list
5. math.factorial casts our integers to floats, so before we return, we need to go back to integer ex. 4.0 -> 4


Runtime: 48 ms, faster than 66.67% of Python3 online submissions for Number of Good Pairs.
Memory Usage: 13.9 MB, less than 100.00% of Python3 online submissions for Number of Good Pairs.
"""

import math
class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        lookup_table = {}
        rtn_value = 0
        
        for index, item in enumerate(nums):
            if f"{item}" in lookup_table:
                lookup_table[f"{item}"].append(index)
            else:
                lookup_table[f"{item}"] = [index]
        
        for item in lookup_table.values():
            n = len(item)
            if n > 1:
                num_to_add = math.factorial(n)/(2* (math.factorial(n-2)))
                rtn_value += num_to_add
        
        return int(rtn_value)