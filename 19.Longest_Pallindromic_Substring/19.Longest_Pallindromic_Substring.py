'''
	Given a string s, return the longest palindromic substring in s.

 

Example 1:

Input: s = "babad"
Output: "bab"
Note: "aba" is also a valid answer.
Example 2:

Input: s = "cbbd"
Output: "bb"
Example 3:

Input: s = "a"
Output: "a"
Example 4:

Input: s = "ac"
Output: "a"
 

Constraints:

1 <= s.length <= 1000
s consist of only digits and English letters (lower-case and/or upper-case),
   Hide Hint #1  
How can we reuse a previously computed palindrome to compute a larger palindrome?
   Hide Hint #2  
If “aba” is a palindrome, is “xabax” and palindrome? Similarly is “xabay” a palindrome?
   Hide Hint #3  
Complexity based hint:
If we use brute-force and check whether for every start and end position a substring is a palindrome we have O(n^2) start - end pairs and O(n) palindromic checks. Can we reduce the time for palindromic checks to O(1) by reusing some previous computation.

'''

class Solution:
    def longestPalindrome(self, s):
        n, ans = len(s), ""
        def helper(i, j):
            while i >= 0 and j < n and s[i] == s[j]:
                i, j = i - 1, j + 1
            return s[i + 1:j]
        
        for k in range(n):
            ans = max(helper(k, k), helper(k, k + 1), ans, key=len)
        return ans