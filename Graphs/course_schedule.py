"""
Course Schedule
https://leetcode.com/problems/course-schedule/description/

There are a total of n courses you have to take, labeled from 0 to n - 1.

Some courses may have prerequisites, 
for example to take course 0 you have to first take course 1, which is expressed as a pair: [0,1]

Given the total number of courses and a list of prerequisite pairs, 
is it possible for you to finish all courses?

For example:

2, [[1,0]]
There are a total of 2 courses to take. 
To take course 1 you should have finished course 0. So it is possible.

2, [[1,0],[0,1]]
There are a total of 2 courses to take. 
To take course 1 you should have finished course 0, 
and to take course 0 you should also have finished course 1. 
So it is impossible.

---

The idea is to create a topological sort. The classes and dependences represent 
a Directed Acyclic Graph (DAG). If there is a cycle (aka two classes require each other as recs)
then it is impossible to take all the classes

The topological sort algo does the following:

int[][] graph = new int[numCourses][]
int[] visited = new int[numCourses]

for each i in prerequisits.length
	idx = prerequisites[i][0]
	req = prerequisites[i][1]
	graph[idx].add(req)

public bool dfs_cycle(node n)
	if temporary mark
		return false
	if permanent mark
		return true
	visited[n] = -1 // temp mark
	for each adj in n
		if dfs_cycle(adj) is false
			return false
	visited[n] = 1 // permanent mark

for each node in graph
	if dfs_cycle(node) is false
		return false
return true

In words, the sort goes visits each node. If the node was visited permanently, then go to the next node.
If the node was visited temporarily, a cycle exists
"""

class Solution(object):

	def canFinish(self, numCourses, prerequisites):
		"""
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: bool
        """
        # init the graph
        graph = [[] for _ in xrange(numCourses)]
        visited = [0]*numCourses

        # list is alwasys [class, prereq] so we can unpack nicely
        for cl, req in prerequisites:
        	graph[cl].append(req)

        def dfs_cycle(node):
        	# temp visited case
        	if visited[node] == -1:
        		return False
        	# permanent case
        	if visited[node] == 1:
        		return True
        	visited[node] = -1 # temp visit
        	for adj in graph[node]:
        		if not dfs_cycle(adj):
        			return False
        	visited[node] = 1 # perm
        	return True
        for cl in xrange(numCourses):
        	if not dfs_cycle[cl]:
        		return False
        return True
