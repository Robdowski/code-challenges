
## CAST INT TO STRING
## ACCESS STRING USING SLICE NOTATION
## USE TWO POINTERS POINTING AT OPPOSITE ENDS OF STRING
## INCREMENT AND DECREMENT EACH ITERATION
## IF THEY EVER DO NOT MATCH, NOT A PALINDROME

class Solution:
    def isPalindrome(self, x: int) -> bool:
        as_string = str(x)
        left = 0
        right = len(as_string)-1
        
        while left < right:
            if as_string[left] != as_string[right]:
                return False
            
            left += 1
            right -= 1
            
        return True
        