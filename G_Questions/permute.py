""" /** 
* Given any uppercase string. Report the starting index at which any valid permutation of 
* ABCDEF starts. If not found, then report -1. 
* Possible permutations of ABCDEF are ABCDFE, BCDAFE, FEDCAB etc (a total of 6! = 720 permutations) 
"""
import sys
import copy

def get_permutations(s):
	return recur(s, "", results=[])

def recur(s, curr, results=[]):
	if len(s) == 0:
		results.append(curr)
		return
	for i in xrange(len(s)):
		n_curr = curr + s[i]
		recur(s[0:i]+s[i+1:], n_curr, results=results)
	return results


################### solution to problem ##################

# asumption: the target string does not have any repeat characters
# The solution is a type of backtracking
# create a hashset for the target string
# for every character found in the hashset move the index forward
# remove that character from the hashset
# if the next character isn't in the hashset, backtrack the index
# add back the removed characters and continue forward

def find_in_str(s, target):
	"""
	a wrapper that turns the target string into a hashset<char>
	"""
	ts = set()
	for ch in target:
		ts.add(ch)
	return find_start(s, ts)

def find_start(s, ts):
	"""
	find start loops through each index of s 
	and checks the target set for the current character
	Args
		s (str): a string to search for any permutation of chars in ts
		ts (set<char>): a set of the target characters
	Returns
		int: the index where the permutation begins
		else -1
	"""
	if not s or not ts:
		return -1
	offset = len(ts)
	i = 0
	removed = []
	while i < len(s):
		if s[i] in ts:
			removed.append(s[i])
			ts.remove(s[i])
		else:
			r_l = len(removed)
			i -= r_l
			for ch in removed:
				ts.add(ch)
			removed = []
		if len(ts) == 0:
			return i - offset + 1
		i += 1
	return -1


if __name__ == '__main__':
	# arg1 is string to search
	# arg2 is target
	arg1, arg2 = str(sys.argv[1]), str(sys.argv[2])
	print find_in_str(arg1, arg2)
