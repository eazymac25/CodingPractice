"""
We want to create a simple implementation of Dijkstra's Algorithm
to find minimum paths in a graph

Awesome algo and a must node. I need a refresher, so this will be a good exploratory
attempt
"""
import sys
import json
from collections import deque

class Graph(object):

	def __init__(self, vertex_count):
		self.vertex_count = vertex_count
		self.conn = [
			[ 0 for _ in xrange(self.vertex_count)]
				for _ in xrange(self.vertex_count)
		]

	def implicit_paths(self, prev):
		paths = []
		for u in xrange(self.vertex_count):
			v = u
			stack = deque()
			while prev[v] > -1:
				stack.appendleft(prev[v])
				v = prev[v]
			stack.append(u) # put the target at the end
			paths.append(list(stack))
		return paths

	def min_dist(self, q, dist):
		m = sys.maxint
		min_v = 0
		for v in q:
			if dist[v] < m:
				m = dist[v]
				min_v = v
		return min_v

	def path_finder(self, start):

		prev = [-1] * self.vertex_count
		dist = {}
		dist[start] = 0

		q = deque()
		q.append(start)

		# init the dists
		for vertex in xrange(self.vertex_count):
			if vertex != start:
				dist[vertex] = sys.maxint
				q.append(vertex)

		while q:
			u = self.min_dist(q, dist)
			q.remove(u)

			for n in xrange(self.vertex_count):
				if n != u  and self.conn[u][n] > 0:
					new_dist = dist[u] + self.conn[u][n]
					if new_dist < dist[n]:
						dist[n] = new_dist
						prev[n] = u

		return dist, prev

if __name__ == '__main__':
	g = Graph(9)
	g.conn = [
		[0, 4, 0, 0, 0, 0, 0, 8, 0],
		[4, 0, 8, 0, 0, 0, 0, 11, 0],
		[0, 8, 0, 7, 0, 4, 0, 0, 2],
		[0, 0, 7, 0, 9, 14, 0, 0, 0],
		[0, 0, 0, 9, 0, 10, 0, 0, 0],
		[0, 0, 4, 14, 10, 0, 2, 0, 0],
		[0, 0, 0, 0, 0, 2, 0, 1, 6],
		[8, 11, 0, 0, 0, 0, 1, 0, 7],
		[0, 0, 2, 0, 0, 0, 6, 7, 0]
	]
	dist, prev = g.path_finder(0)
	paths = g.implicit_paths(prev)
	print paths
	print json.dumps(dist, indent=4)

