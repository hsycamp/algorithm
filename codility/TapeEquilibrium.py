'''
# TapeEquilibrium
Minimize the value |(A[0] + ... + A[P-1]) - (A[P] + ... + A[N-1])|.
'''


# 시간초과
def solution1(A):
    result = []
    for i in range(1, len(A)):
        diff = abs(sum(A[:i])-sum(A[i:]))
        result.append(diff)
    return min(result)


def solution2(A):
    lst = []
    sumOfFirstPart = 0
    sumOfSecondPart = sum(A)
    for i in range(len(A)-1):
        sumOfFirstPart += A[i]
        sumOfSecondPart -= A[i]
        lst.append(abs(sumOfFirstPart-sumOfSecondPart))
    return min(lst)
