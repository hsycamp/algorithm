'''
# MaxCounters
Calculate the values of counters after applying all alternating operations: increase counter by 1; set value of all counters to current maximum.
'''


# 시간초과
def solution1(N, A):
    lst = [0] * N
    for i in range(len(A)):
        for j in range(N):
            if A[i] == j+1:
                lst[j] += 1
            if A[i] == N+1:
                lst = [max(lst)] * N
    return lst


def solution2(N, A):
    lst = [0]*N
    count = 0
    maxCount = 0
    for i in range(len(A)):
        if A[i] == N+1:
            maxCount = count
        else:
            if lst[A[i]-1] < maxCount:
                lst[A[i]-1] = maxCount
            lst[A[i]-1] += 1
            if lst[A[i]-1] > count:
                count = lst[A[i]-1]
    bridge_the_gap(lst, maxCount)
    return lst


def bridge_the_gap(lst, maxCount):
    for i in range(len(lst)):
        if lst[i] < maxCount:
            lst[i] = maxCount
