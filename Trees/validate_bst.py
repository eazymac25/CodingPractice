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
        """
        It's good to note the idea behind this solution
        ----
        At any level in a BST you can compare the largest right value seen
        and the smallest left value seen to the current node to identify 
        if the tree is valid or not

                    5
                 /     \
                1        7
              /    \
             0      6

        Review execution:
        | iteration | Node Value | maxleft | maxright |
           iter 1:        5         None       None
           iter 2:        1           5        None
           iter 3:        0           1        None
           iter 4:        6           5          1

        -> return False

        at node 6 the maxleft = 5 
        and maxright = 1
        6 is greater than 5 so this evaluates to False
        """
        if not node:
            return True
        if maxleft is not None and node.val >= maxleft:
            return False
        if maxright is not None and node.val <= maxright:
            return False
        return self.dfs(node.left, node.val, maxright) and \
    self.dfs(node.right, maxleft, node.val)
