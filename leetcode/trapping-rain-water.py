# https://leetcode.com/problems/trapping-rain-water/submissions/
class Solution(object):
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """

        length = len(height)

        max_l = [0] * length
        max_r = [0] * length

        max_l[0] = height[0]
        for i in range(1, length):
            max_l[i] = max(max_l[i - 1], height[i])

        max_r[length - 1] = height[length - 1]
        for i in range(length - 2, 0, -1):
            max_r[i] = max(max_r[i + 1], height[i])

        ret = [ min(max_l[i],  max_r[i]) - height[i] for i in range(1, length - 1) ]
        return sum(ret)

height = [0,1,0,2,1,0,1,3,2,1,2,1]
solution = Solution()
print(solution.trap(height))
