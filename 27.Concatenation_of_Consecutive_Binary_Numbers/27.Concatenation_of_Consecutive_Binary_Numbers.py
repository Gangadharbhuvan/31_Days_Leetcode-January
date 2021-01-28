'''
    Given an integer n, return the decimal value of the binary string formed by concatenating the binary representations of 1 to n in order, modulo 109 + 7.

 

Example 1:

Input: n = 1
Output: 1
Explanation: "1" in binary corresponds to the decimal value 1. 
Example 2:

Input: n = 3
Output: 27
Explanation: In binary, 1, 2, and 3 corresponds to "1", "10", and "11".
After concatenating them, we have "11011", which corresponds to the decimal value 27.
Example 3:

Input: n = 12
Output: 505379714
Explanation: The concatenation results in "1101110010111011110001001101010111100".
The decimal value of that is 118505380540.
After modulo 109 + 7, the result is 505379714.
 

Constraints:

1 <= n <= 105
   Hide Hint #1  
Express the nth number value in a recursion formula and think about how we can do a fast evaluation.

'''

class Solution:
    def concatenatedBinary(self, n):
        def bin_pow(num): return [1<<i for i, b in enumerate(bin(num)[:1:-1]) if b == "1"]
        ans, MOD, q = 0, 10**9 + 7, len(bin(n)) - 3

        B = bin_pow((1<<q) - 1) + bin_pow(n - (1<<q) + 1)[::-1]
        C = list(range(1, q+1)) + [q+1]*(len(B) - q)
        D = list(accumulate(i*j for i,j in zip(B[::-1], C[::-1])))[::-1][1:] + [0]
        
        for a, b, c, d in zip(accumulate(B), B, C, D):
            t1 = pow(2, b*c, MOD) - 1
            t2 = pow(pow(2, c, MOD)-1, MOD - 2, MOD)
            ans += t2*((a-b+1+t2)*t1-b)*pow(2, d, MOD)

        return ans % MOD