'''
LeetCode
242. Valid Anagram
https://leetcode.com/problems/valid-anagram/

Description:
Given two strings s and t , write a function to determine if t is an anagram of s.

Example 1:

Input: s = "anagram", t = "nagaram"
Output: true

Example 2:

Input: s = "rat", t = "car"
Output: false

Note:
You may assume the string contains only lowercase alphabets.
'''


class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        dic = {}
        if len(s) != len(t):
            return False
        for i in s:
            if i in dic.keys():
                dic[i] += 1
            else:
                dic[i] = 1
        for j in t:
            if j in dic.keys() and dic[j] != 0:
                dic[j] -= 1
            else:
                return False
        return True
