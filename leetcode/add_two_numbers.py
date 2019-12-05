'''
LeetCode
2. Add Two Numbers
https://leetcode.com/problems/add-two-numbers/

Description:

You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order and each of their nodes contain a single digit. Add the two numbers and return it as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.

Example:

Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
Output: 7 -> 0 -> 8
Explanation: 342 + 465 = 807.
'''

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        first_number = self.make_number(l1)
        second_number = self.make_number(l2)

        sum_result = first_number + second_number
        reversed_str = str(sum_result)[::-1]

        answer = None
        current_node = None

        for elem in reversed_str:
            if not answer:
                answer = ListNode(int(elem))
                current_node = answer
            else:
                current_node.next = ListNode(int(elem))
                current_node = current_node.next

        return answer

    def make_number(self, lst: ListNode) -> int:
        result_number = 0
        current_node = lst
        num = 1
        while current_node:
            result_number += current_node.val*num
            current_node = current_node.next
            num *= 10
        return result_number
