"""
Given a singly linked list where elements are sorted in ascending order, convert it to a height balanced BST.

For this problem, a height-balanced binary tree is defined as a binary tree in which the depth of the two subtrees of every node never differ by more than 1.


Example:

Given the sorted linked list: [-10,-3,0,5,9],

One possible answer is: [0,-3,9,-10,null,5], which represents the following height balanced BST:

      0
     / \
   -3   9
   /   /
 -10  5

"""

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    
    def sortedListToBST(self, head):
        if head is None:
            return
        l = []
        while head:
            l.append(head.val)
            head = head.next
        if len(l) == 1:
            return TreeNode(l[0])
        return self.recur_tree(l)
        
    def recur_tree(self, l):
        if not l:
            return None
        if len(l) == 1:
            return TreeNode(l[0])
        root = TreeNode(l[len(l)/2])
        root.left = self.recur_tree(l[:len(l)/2])
        root.right = self.recur_tree(l[len(l)/2+1:])
        return root
    
    def sortedListToBST_V1(self, head):
        """
        :type head: ListNode
        :rtype: TreeNode
        """
        if head is None:
            return
        if head.next is None:
            return TreeNode(head.val)
        
        mid, fast = head, head.next.next
        while fast and fast.next:
            mid, fast = mid.next, fast.next.next
        temp = mid.next
        mid.next = None
        root = TreeNode(temp.val)
        root.right = self.sortedListToBST(temp.next)
        root.left = self.sortedListToBST(head)
        return root
