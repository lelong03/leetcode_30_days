# Given an integer array nums, find the contiguous subarray (containing at least one number) which has the largest sum and return its sum.
#
# Example:
#
# Input: [-2,1,-3,4,-1,2,1,-5,4],
# Output: 6
# Explanation: [4,-1,2,1] has the largest sum = 6.
# Follow up:
#
# If you have figured out the O(n) solution, try coding another solution using the divide and conquer approach, which is more subtle.

import sys

class Solution(object):

    # Kadane's algorithm
    def maxSubArray(self, nums):
        if len(nums) == 1:
            return nums[0]

        max_so_far = -sys.maxint - 1
        max_ending_here = 0

        for i in range(0, len(nums)):
            max_ending_here += nums[i]

            if max_ending_here < 0:
                max_ending_here = 0

            if max_ending_here > max_so_far:
                max_so_far = max_ending_here

        return max_so_far

    # Kadane's algorithm with index
    def maxSubArrayWithIndex(self, nums):
        max_so_far = -sys.maxint-1
        max_ending_here = 0
        start = 0
        end = 0

        for i in range(0, len(nums)):
            max_ending_here += nums[i]

            if max_ending_here < 0:
                max_ending_here = 0
                s = i+1

            if max_ending_here > max_so_far:
                max_so_far = max_ending_here
                start = s
                end = i

            # print "s=%s, start=%s, end=%s" % (s, start, end)

        return nums[start:end+1]

    # Solution for all negative numbers
    def maxSubArray2(self, nums):
        if len(nums) == 1:
            return nums[0]

        max_so_far = nums[0]
        max_ending_here = nums[0]

        for i in range(1, len(nums)):
            max_ending_here = max(nums[i], max_ending_here + nums[i])
            max_so_far = max(max_ending_here, max_so_far)

        return max_so_far


s = Solution()
print s.maxSubArray([-1, -2])
print s.maxSubArray2([-1, -2])





