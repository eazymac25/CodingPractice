"""
Given an array of non-negative integers, you are initially positioned at the first index of the array.

Each element in the array represents your maximum jump length at that position.

Determine if you are able to reach the last index.

For example:
A = [2,3,1,1,4], return true.

A = [3,2,1,0,4], return false.
"""
class Solution(object):
    def canJump(self, nums):
        """
        GREEDY Approach
        :type nums: List[int]
        :rtype: bool
        """
        m = 0
        for i in xrange(len(nums)):
            if i > m:
                return False
            m = max(m, i + nums[i])
        return True
    def canJumpFirstTry(self, nums):
        """
        DFS stack approach
        :type nums: List[int]
        :rtype: bool
        """
        def recur(i, arr):
            if i >= len(arr) - 1:
                return True
            for j in range(1, arr[i]+1):
                n = i + j
                if recur(n, arr):
                    return True
            return False
        return recur(0, nums)