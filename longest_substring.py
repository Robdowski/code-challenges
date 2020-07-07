"""
The purpose of this algorithm is to find the longest substring without repeating characters if given a string.

I utilized a "brute force" approach to this problem by iterating through i, j and using a dictionary to look up if we've visited that
character or not. This will run in n^3 time at it's worst. 

Another approach to this problem would be to use a "sliding window" with a hashtable or set. With a naive solution to this using a sliding window,
we can reduce the runtime complexity to O(2n)

The reason I chose to leave my brute force method as the solution to this problem is that this is what I would have done in an interview.
I would not have been able to research further methods for optimizing this algorithm, and this is currently the most accurate representation
of my skill level with this type of problem.
"""

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
          
        longest_count = 0
        
        for i in range(len(s)):
            count = 0
            seen = {}
            
            for j in range(i, len(s)):
                

                ##handle edge case since not able to add " " to a dict
                if s[j] == " ":
                    if 1 not in seen:
                        print('hit one')
                        seen[1] = 1
                        count += 1
                    elif 1 in seen:
                        break
                
                ## break if we've seen it
                elif s[j] in seen:
                    break


                ## if it's new, add to count and keep going    
                else:
                    count += 1
                    seen[s[j]] = 1
            
            if count > longest_count:
                longest_count = count
                    
        return longest_count