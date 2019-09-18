'''
프로그래머스
가장 긴 팰린드롬
https://programmers.co.kr/learn/courses/30/lessons/12904

문제 설명
앞뒤를 뒤집어도 똑같은 문자열을 팰린드롬(palindrome)이라고 합니다.
문자열 s가 주어질 때, s의 부분문자열(Substring)중 가장 긴 팰린드롬의 길이를 return 하는 solution 함수를 완성해 주세요.

예를들면, 문자열 s가 abcdcba이면 7을 return하고 abacde이면 3을 return합니다.

제한사항
문자열 s의 길이 : 2,500 이하의 자연수
문자열 s는 알파벳 소문자로만 구성
입출력 예
s	answer
abcdcba	7
abacde	3
'''


import heapq


def solution(s):
    for i in range(len(s), 0, -1):
        for j in range(len(s)):
            if i+j > len(s):
                break
            palindrome_length = get_palindrome_length(s[j:j+i])
            if palindrome_length:
                return palindrome_length


def get_palindrome_length(s):
    if s == s[::-1]:
        return len(s)
