'''
LeetCode
409. Longest Palindrome
https://leetcode.com/problems/longest-palindrome/
Description:
Given a string which consists of lowercase or uppercase letters, find the length of the longest palindromes that can be built with those letters.

This is case sensitive, for example "Aa" is not considered a palindrome here.

Note:
Assume the length of given string will not exceed 1,010.

Example:
Input:
"abccccdd"

Output:
7

Explanation:
One longest palindrome that can be built is "dccaccd", whose length is 7.
'''


class Solution:
    def longestPalindrome(self, s: str) -> int:
        dic = {}
        count = 0
        for i in s:
            if i in dic.keys():
                dic[i] += 1
            else:
                dic[i] = 1
        for j in dic.values():
            count += j//2*2
            if count % 2 == 0 and j % 2 != 0:
                count += 1
        return count
