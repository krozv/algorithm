# 진기의 최고급 붕어빵
"""
N명의 사람
M초의 시간을 들이면 K개의 붕어빵
모든 손님들에게 기다리는 시간 없이 붕어빵을 제공할 수 있는지?
"""
def bread():
    b = 0
    i = 0
    for j in range(len(arr)):
        while True:
            if i and i % M == 0:
                b += K
            if i == arr[j]:
                if b > 0:
                    b -= 1
                    break
                else:
                    return 'Impossible'
            i += 1
        if j < len(arr)-1 and arr[j] != arr[j+1]:
            i += 1
    else:
        return 'Possible'


import sys
sys.stdin = open('input.txt', 'r')
T = int(input())
for t in range(1, T+1):

    N, M, K = map(int, input().split())
    arr = list(map(int, input().split()))
    arr.sort()
    # print(M, K, arr)
    print(f'#{t} {bread()}')