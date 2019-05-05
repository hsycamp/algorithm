'''
약수의 합
문제 설명
자연수 n을 입력받아 n의 약수를 모두 더한 값을 리턴하는 함수, solution을 완성해주세요.
'''


def solution1(n):
    sum = 0
    for i in range(1, n+1):
        if n % i == 0:
            sum += i
    return sum


def solution2(n):
    sum = 0
    for i in range(1, n//2+1):
        if n % i == 0:
            sum += i
    return sum+n
