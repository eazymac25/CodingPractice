"""
Given an array S of n integers, are there elements a, b, c in S such that a + b + c = 0? Find all unique triplets in the array which gives the sum of zero.

Note: The solution set must not contain duplicate triplets.

For example, given array S = [-1, 0, 1, 2, -1, -4],

A solution set is:
[
  [-1, 0, 1],
  [-1, -1, 2]
]

"""


class Solution(object):
    def threeSumMyAttempt(self, nums):
        """
        This was my first iteration making use of a hashtable like the 2 sum
        problem however this was not fast enough. It did work though
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        hashed = {}
        result = []
        combos = {}
        # preprocess
        for i in range(len(nums)):
            if hashed.get(nums[i], None) is not None:
                hashed[nums[i]].append(i)
            else:
                hashed[nums[i]] = [i]
        
        for i in range(len(nums)):
            for j in range(i+1, len(nums)): 
                two_sum = nums[i] + nums[j]
                needed = 0 - two_sum
                if hashed.get(needed, None) is not None:
                    if len(hashed.get(needed))>2 or i not in hashed.get(needed) and j not in hashed.get(needed):
                        temp = sorted([nums[i], nums[j], needed])
                        if combos.get(tuple(temp), None) is None:
                            result.append(temp)
                        combos[tuple(temp)] = 1
        return result

    def threeSumAcceptet(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums.sort()
        results = []
        
        for i in xrange(len(nums)-2):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            l, r = i+1, len(nums)-1
            while l<r:
                s = nums[i] + nums[l] + nums[r]
                if s<0:
                    l+=1
                elif s>0:
                    r-=1
                else:
                    results.append([nums[i], nums[l], nums[r]])
                    while l<r and nums[l] == nums[l+1]:
                        l+=1
                    while l<r and nums[r] == nums[r-1]:
                        r+=-1
                    l+=1
                    r+=-1
        return results