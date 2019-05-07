'''
# MaxCounters
Calculate the values of counters after applying all alternating operations: increase counter by 1; set value of all counters to current maximum.
'''


# 시간초과
def solution(N, A):
    lst = [0] * N
    for i in range(len(A)):
        for j in range(N):
            if A[i] == j+1:
                lst[j] += 1
            if A[i] == N+1:
                lst = [max(lst)] * N
    return lst
