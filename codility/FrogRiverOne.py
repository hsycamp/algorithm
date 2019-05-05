'''
# FrogRiverOne
Find the earliest time when a frog can jump to the other side of a river.
'''


# 시간초과
def solution1(X, A):
    for i in range(len(A)):
        if len(set(A[:i+1])) == X:
            return i
    return -1
