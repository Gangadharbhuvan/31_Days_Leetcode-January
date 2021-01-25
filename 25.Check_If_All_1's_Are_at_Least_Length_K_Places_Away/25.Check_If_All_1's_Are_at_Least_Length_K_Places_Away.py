'''
	Given an array nums of 0s and 1s and an integer k, return True if all 1's are at least k places away from each other, otherwise return False.

 

Example 1:



Input: nums = [1,0,0,0,1,0,0,1], k = 2
Output: true
Explanation: Each of the 1s are at least 2 places away from each other.
Example 2:



Input: nums = [1,0,0,1,0,1], k = 2
Output: false
Explanation: The second 1 and third 1 are only one apart from each other.
Example 3:

Input: nums = [1,1,1,1,1], k = 0
Output: true
Example 4:

Input: nums = [0,1,0,1], k = 1
Output: true
 

Constraints:

1 <= nums.length <= 105
0 <= k <= nums.length
nums[i] is 0 or 1
   Hide Hint #1  
Each time you find a number 1, check whether or not it is K or more places away from the next one. If it's not, return false.

'''

class Solution:
    def kLengthApart(self, nums, k):
        dist = k
        
        for num in nums:
            if num == 0: dist += 1
            elif num == 1 and dist >= k: dist = 0
            else: return False
                
        return True