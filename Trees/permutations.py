"""
Given a collection of distinct numbers, return all possible permutations.

For example,
[1,2,3] have the following permutations:
[
  [1,2,3],
  [1,3,2],
  [2,1,3],
  [2,3,1],
  [3,1,2],
  [3,2,1]
]
"""

class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]

        Pretty much the same idea is the phone_number
        except the order doesn't matter hence permutation
        """
        if len(nums) == 0:
            return []
        
        return self.dfs(nums, curr=[], results=[])
    
    def dfs(self, nums, curr=[], results=[]):
        if len(nums) == 0:
            results.append(curr)
            return
        for i in xrange(len(nums)):
            n_nums = nums[0:i] + nums[i+1:]
            n_curr = curr + [nums[i]]
            self.dfs(n_nums, curr=n_curr, results=results)
        return results
