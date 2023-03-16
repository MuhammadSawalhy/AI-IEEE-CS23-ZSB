# Submission: https://leetcode.com/problems/replace-elements-with-greatest-element-on-right-side/submissions/916419730/
class Solution:
    def replaceElements(self, arr: list[int]) -> list[int]:
        ans = [0] * len(arr)
        ans[-1] = -1
        for i in range(len(arr) - 2, -1, -1):
            ans[i] = max(ans[i + 1], arr[i + 1])
        return ans
