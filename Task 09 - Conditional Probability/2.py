# Submission: https://leetcode.com/problems/valid-palindrome/submissions/916816572/
class Solution:
    def isPalindrome(self, s: str) -> bool:
        new_s = list(filter(lambda c: c.isalnum(), s.lower()))
        return new_s == new_s[::-1]
