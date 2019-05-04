'''
# PermCheck
Check whether array A is a permutation.
'''


def solution(A):
    if sum(A) != sum(range(len(A)+1)):
        return 0
    if len(A) != len(set(A)):
        return 0
    return 1
