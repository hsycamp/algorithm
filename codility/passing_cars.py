'''
# PassingCars
Count the number of passing cars on the road.
'''


def solution(A):
    east = 0
    answer = 0
    for elem in A:
        if elem == 0:
            east += 1
        else:
            answer += east
            if answer > 10**9:
                return -1
    return answer
