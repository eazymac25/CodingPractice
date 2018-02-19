"""
For a undirected graph with tree characteristics, we can choose any node as the root. The result graph is then a rooted tree. Among all possible rooted trees, those with minimum height are called minimum height trees (MHTs). Given such a graph, write a function to find all the MHTs and return a list of their root labels.

Format
The graph contains n nodes which are labeled from 0 to n - 1. You will be given the number n and a list of undirected edges (each edge is a pair of labels).

You can assume that no duplicate edges will appear in edges. Since all edges are undirected, [0, 1] is the same as [1, 0] and thus will not appear together in edges.

Example 1:

Given n = 4, edges = [[1, 0], [1, 2], [1, 3]]

        0
        |
        1
       / \
      2   3
return [1]

Example 2:

Given n = 6, edges = [[0, 3], [1, 3], [2, 3], [4, 3], [5, 4]]

     0  1  2
      \ | /
        3
        |
        4
        |
        5
return [3, 4]

Note:

(1) According to the definition of tree on Wikipedia: “a tree is an undirected graph in which any two vertices are connected by exactly one path. In other words, any connected graph without simple cycles is a tree.”

(2) The height of a rooted tree is the number of edges on the longest downward path between the root and a leaf.


---
Solutions:

firstTry (Time Limit Exception) :(
	This involved looping through every node in the graph
	and running a DFS which kept track of the maximum height
	for that starting node

	Once all DFS's had run, min heights were collected from
	the root node to max height

	Obviously, this is a brute force approach and runs in O(N^2) time

Accepted Solution:
	The accepted solution involves a similar approach to a topological sort via BFS

	The solution involves a few key insights about a minimum height tree in a graph

	1) A leaf is a vertex that has only 1 connection
	2) A minimum height tree will be rooted at the midpoint of the longest path
		A good example of this point:
			Imagine a table cloth or any 2 dimensional sheet (doily for those interior designers)
			If you were to pick this cloth up from one point so that the cloth doesn't hit the floor, 
			(as to minimize the drooping height) where would you pick up the cloth?
			Well, I can tell you that you would avoid picking it up from the ends (leaves)
			You would immediately look to grab from a center point. So the question isn't where is the root 
			of the minimum height tree, but where is the midpoint. 
	3) The midpoint can either be 1 or 2 nodes, never more
		(since this is a discrete structure rather than continuous like a cloth you can have more than one midpoint)

	To find the midpoint, collect all of the leaves (aka vertices with degree of one)
	Then BFS inward and generate the next round of leaves, working towards the center
	until the number of nodes left is less than or equal to 2

	Imagine that cloth again... just keep drawing circles of decreasing diameter until
	you reach a point... okay that's a Zeno's paradox for continuous structures, but you get the point ;)
"""

class Solution(object):
	def firstTry(self, n, edges):
        """
        :type n: int
        :type edges: List[List[int]]
        :rtype: List[int]
        """
        if n == 0:
            return []
        if n == 1:
            return [0]
        graph = [[] for _ in range(n)]
        
        for n1, n2 in edges:
            graph[n1].append(n2)
            graph[n2].append(n1)
        height_list = [0]*n
        overall_min = None
        for i in range(n):
            stack = [(i, 0)]
            visited = []
            m_height = 0
            while stack:
                node, height = stack.pop()
                if node in visited:
                    continue
                visited.append(node)
                if height > m_height:
                    m_height = height
                for adj in graph[node]:
                    stack.append((adj, height+1))
            if not overall_min or m_height < overall_min:
                overall_min = m_height
            height_list[i] = m_height
        results = []
        for i in xrange(n):
            if height_list[i] == overall_min:
                results.append(i)
        return results


    def findMinHeightTrees(self, n, edges):
        """
        :type n: int
        :type edges: List[List[int]]
        :rtype: List[int]
        """
        if n == 1: return [0]
        
        degrees = [0 for _ in xrange(n)]
        graph = [[] for _ in xrange(n)]

        for v1, v2 in edges:
        	graph[v1].append(v2)
        	graph[v2].append(v1)

        	degrees[v1] += 1
        	degrees[v2] += 1

        leaves = [i for i in xrange(n) if degrees[i] == 1]
        
        while n > 2:
            n -= len(leaves)
            new_leaves = []
            for leaf in leaves:
                v = graph[leaf].pop()
                graph[v] = [idx for idx in graph[v] if idx != leaf]
                degrees[v] -= 1
                if degrees[v] == 1:
                    new_leaves.append(v)
            leaves = new_leaves
        return leaves
