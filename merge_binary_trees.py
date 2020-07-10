"""
For this problem, I am asked to merge two binary trees. If two nodes are in the same position in Tree 1 and Tree 2, add the values together. If only one tree has a node in that position, use the value from that tree.

This can be achieved by using recursion, as most binary tree problems can be solved this way. We can traverse the trees in preorder, adding the values together unless t1 or t2 is null.
In that case, we return the non null value.

The runtime complexity of this problem should be O(n) where n is the number of nodes in the two given trees.

The space complexity would also be O(n) as a worst case, where n is the number of nodes in both trees. 
"""

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def mergeTrees(self, t1: TreeNode, t2: TreeNode) -> TreeNode:
        if not t1:
            return t2
        if not t2:
            return t1
        
        if t1 and t2:
            t1.val = t1.val + t2.val
        
        t1.left = self.mergeTrees(t1.left, t2.left)
        t1.right = self.mergeTrees(t1.right, t2.right)
          
        return t1