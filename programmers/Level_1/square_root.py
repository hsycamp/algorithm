'''
프로그래머스
정수 제곱근 판별
https://programmers.co.kr/learn/courses/30/lessons/12934

문제 설명
임의의 정수 n에 대해, n이 어떤 정수 x의 제곱인지 아닌지 판단하려 합니다.
n이 정수 x의 제곱이라면 x+1의 제곱을 리턴하고, n이 정수 x의 제곱이 아니라면 -1을 리턴하는 함수를 완성하세요.

제한 사항
n은 1이상, 50000000000000 이하인 정수입니다.

입출력 예
n	return
121	144
3	-1
'''

import math


def solution1(n):
    if math.ceil((math.sqrt(n))) == math.sqrt(n):
        return math.pow((math.sqrt(n)+1), 2)
    return -1


def solution2(n):
    sqrt = n ** (1/2)
    if sqrt % 1 == 0:
        return (sqrt + 1) ** 2
    return -1
