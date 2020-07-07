"""
This is my solution to a classic interview problem, removing the K-th linked list node in one pass.

We first start by setting a dummy, which points to the head. This will allow us to start at 0 instead of 1.  We then
advance pointer j by n times while keeping pointer i in place. Once we have advanced j n times, we can then begin advancing
both i and j until j reaches the end of the linked list. Once this has been achieved, i should be one spot from the node to delete.

We can do this by pointing i.next to i.next.next, which will effectively delete the current i.next from memory, since there is no longer
anything pointing to it.

One optimization could be made if the length of the linked list was given. We would no longer need to iterate k times to create a gap
between pointers i and j. We could simply take k = len(lst) - n and then iterate i by k amount of times to find the node to delete.
"""

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        dummy = ListNode(0)
        dummy.next = head
        
        i = dummy
        j = dummy
        k = 0
            
        while k < n+1:
            j = j.next
            k += 1
        
        while j is not None:
            j = j.next
            i = i.next
            
           
            
        i.next = i.next.next
        
        return dummy.next