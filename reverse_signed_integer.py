"""
In this problem, I decided to take the route of turning the integer into a string to reverse it,
taking a programmatic in lieu of a mathematical approach (if a mathematical approach exists, I don't know how to implement it.)

I separated the actual functionality of turning the integer into a string and reversing it into a helper function,
and took care of most of the return logic in the main function.

To reverse the int, I first cast the int to an absolute value, not worrying about a sign at this time,
then cast that to a string, reverse it and add it to a new string. It is possible that you can do this problem without
declaring a new string variable, but I was getting some errors casting my reversed string back to an int and this seemed to fix the issue.

Finally, I took care of the edge cases in my main function, such as inputs of 0 and outside of the range of [-2^31, 2^31 - 1]

"""
class Solution:
    def reverse(self, x: int) -> int:
        answer = 0
        if x == 0:
            answer = 0
        
        elif x < 0:
            reversed_int = self.reverse_int(x)
            answer = -reversed_int
        
        elif x > 0:
            reversed_int = self.reverse_int(x)
            answer = reversed_int
        
        if answer in  range(-2**31, 2**31):
            return answer
        else:
            return 0
            
    def reverse_int(self, x: int) -> int:
        int_as_string = str(abs(x))
        new_str = ""
        for i in reversed(int_as_string):
            new_str += i
            
        return int(new_str)
        
