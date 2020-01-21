'''
LeetCode
283. Move Zeroes
https://leetcode.com/problems/move-zeroes/
Description:
Given an array nums, write a function to move all 0's to the end of it while maintaining the relative order of the non-zero elements.

Example:

Input: [0,1,0,3,12]
Output: [1,3,12,0,0]
Note:

You must do this in-place without making a copy of the array.
Minimize the total number of operations.
'''


class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        idx = 0
        for i in range(len(nums)):
            if nums[idx] == 0:
                target = nums.pop(idx)
                nums.append(target)
            else:
                idx += 1
