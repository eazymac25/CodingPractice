"""
LRU Cache implementation

My first thought is a hash stack (not sure if that's a thing)


Turns out we can do better

We could do this instead wit a LinkedList.
We could map the key to a Node object
The node would have the key and value 

We then can easy move, insert and find things in this doubly linked list ... more to come
"""

class LRUCache(object):

	def __init__(size=100):
		self.size = 100
		self.stack = [] # keep the keys
		self.hash = {} # the key to value


	def insert(key, val):
		self.hash[key] = val
		if len(stack) == self.size:
			self.stack = self.stack[1:]
		if key in self.stack:
			self._remove(key)
		self.stack.append(key)

	def get(key):
		return self.hash.get(key, None)

	def _remove(key):
		for i, obj in enumerate(stack):
			if obj == key:
				self.stack = self.stack[:i] + self.stack[i+1:]
