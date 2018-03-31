
import heapq

def build_tower(circus):
	tower = []
	h = []
	#circus = sorted(circus, key=lambda x: x[0])

	for performer in circus:
		heapq.heappush(h, performer)

	while h:
		n = heapq.heappop(h)
		if len(tower) == 0 or (n[0] > tower[-1][0] and n[1] > tower[-1][0]):
			tower.append(n)
	return len(tower), tower

c = [
	(65, 100),
	(70, 150),
	(56, 90),
	(75, 190),
	(60, 95),
	(68, 110)
]

r = build_tower(c)

print r[0]
print r[1]