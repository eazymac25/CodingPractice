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
    
    def dfs(self, node, maxleft, maxright):
        if not node:
            return True
        if maxleft is not None and node.val >= maxleft:
            return False
        if maxright is not None and node.val <= maxright:
            return False
        return self.dfs(node.left, node.val, maxright) and \
    self.dfs(node.right, maxleft, node.val)