"""
* Input is an integer array A 
* Return an array B such that B[i] = product of all elements of A except A[i] 
"""


def prod_arr(a):
	"""
	The idea is pretty simple
	There are 3 potential cases
	case 1: no zeros in the array so just find the product
			for every instance and then loop through and divide out
			the current index value
	case 2: 1 zero -> set the index of that zero
			to the product of all other indexes
			meanwhile everythign else is zero
	case 3: 2 or more -> everything is zero
	"""
	# init b as the case of 2 or more zeros
	b = [0 for _ in xrange(len(a))]
	zeros = []
	prod = 1
	for i in xrange(len(a))
		if a[i] == 0:
			zeros.append(i)
	if len(zeros) == 0: # no zeros
		for num in a:
			prod *= num
		for i in xrange(len(a)):
			b[i] = prod/a[i]
	elif len(zeros) == 1: # only one zero
		zidx = zeros[0]
		for i in xrange(len(a)):
			if i != zidx:
				prod *= a[i]
		b[zidx] = prod
	return b
