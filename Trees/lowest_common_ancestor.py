"""
Given a binary search tree (BST), find the lowest common ancestor (LCA) of two given nodes in the BST.

According to the definition of LCA on Wikipedia: “The lowest common ancestor is defined between two nodes v and w as the lowest node in T that has both v and w as descendants (where we allow a node to be a descendant of itself).”

        _______6______
       /              \
    ___2__          ___8__
   /      \        /      \
   0      _4       7       9
         /  \
         3   5
For example, the lowest common ancestor (LCA) of nodes 2 and 8 is 6. Another example is LCA of nodes 2 and 4 is 2, since a node can be a descendant of itself according to the LCA definition.
"""



# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        p_path = self.dfs(root, p, path=[])
        q_path = self.dfs(root, q, path=[])
        i = 0
        while i<len(p_path) and i<len(q_path):
            if p_path[i].val != q_path[i].val:
                break
            i+=1
        i-= 1
        if len(p_path) < len(q_path):
            return p_path[i]
        return q_path[i]
        
    
    def dfs(self, root, target, path=[]):
        if root is not None:
            path.append(root)
        if root is None or root.val == target.val:
            return path
        elif root.val < target.val:
            return self.dfs(root.right, target, path=path)
        return self.dfs(root.left, target, path=path)


    def simpler_lca(self, root, p, q):
        """
        This option is iterative and much simpler
        Just keep going through the nodes until 
        the vals of p and q are on opposite sides of the parent
        """
        while root:
            if max(p.val, q.val) < root.val:
                root = root.left
            elif min(p.val, q.val) > root.val:
                root = root.right
            else:
                return root
        return root
