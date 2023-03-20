# Submission: https://leetcode.com/problems/trapping-rain-water/submissions/918509509/
class Solution:
    def max_left(self, height: List[int]) -> List[int]:
        mx = [0] * len(height)
        for i in range(1, len(height)):
            mx[i] = max(mx[i-1], height[i-1])
        return mx

    def trap(self, height: List[int]) -> int:
        left = self.max_left(height)
        left.reverse()
        height.reverse()
        right = self.max_left(height)
        water = 0
        for i in range(len(height)):
            water += max(height[i], min(left[i], right[i])) - height[i]
        return water

