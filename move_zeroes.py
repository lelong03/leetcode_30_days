# Given an array nums, write a function to move all 0's to the end of it while maintaining the relative order of the non-zero elements.
#
# Example:
#
# Input: [0,1,0,3,12]
# Output: [1,3,12,0,0]
#
# Input: [5,1,0,3,12,0,8]
# Output: [5,1,3,12,8,0,0]
#
# Note:
#
# You must do this in-place without making a copy of the array.
# Minimize the total number of operations.


class Solution(object):

    # Solution : Moving non-zero numbers to the front then fulfill zeros after that.
    # - Using 2 pointer i and j
    # - i keeps moving until finish array while j tries to mark the last non-zero index
    def moveZeroes(self, nums):
        i = 0
        j = 0

        while i < len(nums):
            if nums[i] != 0:
                nums[j] = nums[i]
                j += 1
            i += 1

        while j < len(nums):
            nums[j] = 0
            j += 1

        return nums


s = Solution()
print s.moveZeroes([5,1,0,3,12,0,0,8])




