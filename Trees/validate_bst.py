# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        return self.dfs(root, None, None)
    
    def dfs(self, node, minleft, maxright):
        """
        It's good to note the idea behind this solution
        ----
        At any level in a BST you can compare the largest right value seen
        and the smallest left value seen to the current node to identify 
        if the tree is valid or not

                    5
            1           7
                6

        at node 6 the maxright = 5 
        and minleft = 1
        6 is greater than 5 so this evaluates to False
        """
        if not node:
            return True
        if maxleft is not None and node.val >= minleft:
            return False
        if maxright is not None and node.val <= maxright:
            return False
        return self.dfs(node.left, node.val, maxright) and \
    self.dfs(node.right, minleft, node.val)