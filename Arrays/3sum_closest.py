"""
Given an array S of n integers, find three integers in S such that the sum is closest to a given number, target. Return the sum of the three integers. You may assume that each input would have exactly one solution.

    For example, given array S = {-1 2 1 -4}, and target = 1.

    The sum that is closest to the target is 2. (-1 + 2 + 1 = 2).
"""

class Solution(object):
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int

        The idea behind this was eaxtly the same as 3 sum, but
        in this case, you don't have to store an array of solution sets.
        Instead, you just return the sum that is closest to the target.
        This means you can break the second loop early. O(n^2) solution
        """
        nums.sort()
        closest = None
        for i in xrange(len(nums)-2):
            if i>0 and nums[i] == nums[i-1]:
                continue
            l,r = i+1, len(nums)-1
            while l<r:
                s = nums[i] + nums[l] + nums[r]
                if closest is None:
                    closest = s
                closest = self.derive_closest(closest, s, target)
                if s < target:
                    l+=1
                elif s > target:
                    r+=-1
                else:
                    return closest
        return closest
    
    def derive_closest(self, curr_sum, new_sum, target):
        curr_sum_diff = abs(target-curr_sum)
        new_sum_diff = abs(target-new_sum)
        
        min_diff = min(abs(curr_sum_diff), abs(new_sum_diff))
        if min_diff == curr_sum_diff:
            return curr_sum
        return new_sum
        