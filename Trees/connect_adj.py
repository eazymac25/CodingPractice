"""
This is a problem that I came across during an interview, but I later discovered
that it was in "Cracking the Coding Interview." I really should have prepped more...

Problem:
	Given a tree connect all the adjacent nodes
	For example the tree below:

				0
			/		\
		1				2
	  /   \          /     \	
	3	   4		5		6

	Becomes:

				0
			/		\
		1	 ----->    2
	  /   \          /   \	
	3 ---> 4  --->	5 ---> 6
"""

class TreeNode(object):
	def __init__(self, val, left=None, right=None, adj=None):
		self.val = val
		self.left = left
		self.right = right
		self.adj = adj

	def __str__(self):

		stor = []
		root = self
		stack = [root]
		while stack:
			node = stack.pop()
			if node:
				adj_val = '->'
				if node.adj:
					adj_val += str(node.adj.val)
				stor.append((node.val, adj_val))
				stack.append(node.right)
				stack.append(node.left)
		return str(stor)


def connect_adj(root):
	if not root:
		return
	if root.left:
		if root.right:
			root.left.adj = root.right
		connect_adj(root.left)
	if root.right:
		if root.adj and root.adj.left:
			root.right.adj = root.adj.left
		connect_adj(root.right)
	return root

r = TreeNode(0)

r.left = TreeNode(1)
r.right = TreeNode(2)

r.left.left = TreeNode(3)
r.left.right = TreeNode(4)

r.right.left = TreeNode(5)
r.right.right = TreeNode(6)

r.left.left.left = TreeNode(7)
r.left.left.right = TreeNode(8)
r.left.right.left = TreeNode(9)
r.left.right.right = TreeNode(10)

r.right.left.left = TreeNode(11)
r.right.left.right = TreeNode(12)
r.right.right.left = TreeNode(13)
r.right.right.right = TreeNode(14)

connect_adj(r)
print r
