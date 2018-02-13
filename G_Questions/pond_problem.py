"""
The pond problem
Calculate the sizes for all ponds on a plot of land

Land is represented like this:

	0 1 2 3 0
	0 4 5 0 6
	7 8 9 0 1
	0 2 3 0 4

What is 0 (lowest point) and land is everything else

A body of water can be connected by any adjacent cells

(Think horizontal, diagonal, and vertical)
"""
import pprint

def pond_sizes(land):
	sizes = []
	for i in xrange(len(land)):
		for j in xrange(len(land[i])):
			if land[i][j] == 0:
				size = calc_pond_sizes(i, j, land)
				print land
				sizes.append(size)
	return sizes

def calc_pond_sizes(i, j, land):
	if i < 0 or j < 0 or i >= len(land) or j >= len(land[i]) or land[i][j] != 0:
		return 0
	size = 1
	land[i][j] = -1 # mark visited
	for row in xrange(-1,2):
		for col in xrange(-1,2):
			size += calc_pond_sizes(i+row, j+col, land)
	return size

if __name__ == '__main__':

	land = [
		[0, 1, 2, 3, 0],
		[0, 4, 5, 0, 6],
		[7, 8, 9, 0, 1],
		[0, 2, 3, 0, 4]
	]

	print pond_sizes(land)




