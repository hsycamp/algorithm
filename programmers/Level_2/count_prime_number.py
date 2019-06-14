'''
프로그래머스
소수 찾기
https://programmers.co.kr/learn/courses/30/lessons/42839

문제 설명
한자리 숫자가 적힌 종이 조각이 흩어져있습니다. 흩어진 종이 조각을 붙여 소수를 몇 개 만들 수 있는지 알아내려 합니다.

각 종이 조각에 적힌 숫자가 적힌 문자열 numbers가 주어졌을 때, 종이 조각으로 만들 수 있는 소수가 몇 개인지 return 하도록 solution 함수를 완성해주세요.

제한사항
numbers는 길이 1 이상 7 이하인 문자열입니다.
numbers는 0~9까지 숫자만으로 이루어져 있습니다.
013은 0, 1, 3 숫자가 적힌 종이 조각이 흩어져있다는 의미입니다.
입출력 예
numbers	return
17	3
011	2
'''


from itertools import permutations


def makeNumbers(numbers):
    numbers = list(numbers)
    resultA = []
    for i in range(1, len(numbers)+1):
        resultA.append(set(permutations(numbers, i)))
    resultB = [y for x in resultA for y in x]
    answer = [str(int(''.join(j))) for j in resultB]
    return answer


def countPrimeNumber(numberlist):
    answer = 0
    for i in set(numberlist):
        t = int(i)
        result = 0
        for j in range(2, t):
            if t % j == 0:
                result += 1
                break
        if result == 0 and t != 1 and t != 0:
            answer += 1
    return answer


def solution(numbers):
    numberlist = makeNumbers(numbers)
    answer = countPrimeNumber(numberlist)
    return answer
