# 8일차 - 이진탐색 (제출용)
'''
이진탐색트리에 저장하려고 한다

'''
def pre_order(T):
    if T:
        global cnt
        cnt += 1
        pre_order(left[T])
        pre_order(right[T])


T = int(input())
for t in range(1,T+1):
    E, N = map(int, input().split())
    arr = list(map(int, input().split()))
    left = [0] * (E+2)  # 왼쪽자식
    right = [0] * (E+2) # 오른쪽자식
    par = [0] * (E+2)   # 가운데부모
    for i in range(E):
        # print(arr)
        p, c = arr[i*2], arr[i*2+1]
        # print(i, p, c)
        if left[p] == 0:
            left[p] = c
        else:
            right[p] = c
        par[c] = p
    cnt = 0
    pre_order(N)
    print(f'#{t} {cnt}')
