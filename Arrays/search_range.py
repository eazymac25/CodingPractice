"""
Given an array of integers sorted in ascending order, find the starting and ending position of a given target value.

Your algorithm's runtime complexity must be in the order of O(log n).

If the target is not found in the array, return [-1, -1].

For example,
Given [5, 7, 7, 8, 8, 10] and target value 8,
return [3, 4].

"""
class Solution(object):
    
    def searchRangeFaster(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        if len(nums)==0: return [-1,-1]
        length=len(nums);l=0;r=length-1;mid=0  
        res=[-1,-1]  
        while l<=r:  
            mid=(l+r)>>1;  
            if nums[mid]==target:break  
            elif nums[mid]>target:r=mid-1  
            else:l=mid+1  
        if l<=r:  
            l=mid-1  
            while l>=0 and nums[l]==nums[mid]:l-=1  
            r=mid+1  
            while r<length and nums[r]==nums[mid]:r+=1  
            res[0]=l+1;res[1]=r-1  
        return res 

    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        rng = [-1, -1]
        lset, rset = False, False
        l, r = 0, len(nums) - 1
        while l <= r:
            if nums[l] == target and not lset:
                rng[0] = l
                lset = True
            if nums[r] == target and not rset:
                rng[1] = r
                rset = True
            if nums[l] < target:
                l += 1
            if nums[r] > target:
                r+= -1
            if rset and lset:
                break
        return rng
