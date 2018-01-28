
def coin_sums(target):
	coins = [1, 2, 5, 10, 20, 50, 100, 200]
	ways = [1] + [0]*target

	for coin in coins:
	    for i in xrange(coin, target+1):
	        ways[i] += ways[i-coin]
	print ways
	return ways[target]


def multiples(high):
	s = 0
	stor = []
	for i in xrange(1, high):
		if i % 3 == 0 or i % 5 == 0:
			s += i
			stor.append(i)
	print stor
	return s

def fib(target):
	last = 0
	current = 1
	for i in xrange(target):
		last, current = current, current+last
	return last

if __name__ == '__main__':
	#print coin_sums(199)
	# print multiples(1000)
	print len(str(fib(4782)))
	c = 0
	while len(str(fib(c)))<1000:
		c += 1
	print c