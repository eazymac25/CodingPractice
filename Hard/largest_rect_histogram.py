class Solution(object):
    def largestRectangleArea_my_attempt(self, heights):
        """
        :type heights: List[int]
        :rtype: int
        """
        max_area = 0
        
        for i in xrange(len(heights)):
            j = i + 1
            min_h = heights[i]
            max_area = max(min_h*(1), max_area)
            while j < len(heights):
                min_h = min(min_h, heights[j])
                max_area = max(min_h*(j-i+1), max_area)
                j+=1
        return max_area


    def largestRectangleArea(self, height):
        """
        This solution is elegant. No idea how someone would have come up
        with this idea in a ~30 minute interview
        """
        height.append(0)
        stack = [-1]
        ans = 0
        for i in xrange(len(height)):
            while height[i] < height[stack[-1]]:
                h = height[stack.pop()]
                w = i - stack[-1] - 1
                ans = max(ans, h * w)
            stack.append(i)
        height.pop()
        return ans