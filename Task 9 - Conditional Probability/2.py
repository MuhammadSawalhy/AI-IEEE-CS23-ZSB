# Submission: https://leetcode.com/problems/valid-palindrome/submissions/915926217/
class Solution:
    def isPalindrome(self, s: str) -> bool:
        new_s = list(filter(lambda c: c.isalnum(), s.lower()))
        return new_s[:len(new_s)//2] == new_s[:(len(new_s) - 1)//2:-1]

