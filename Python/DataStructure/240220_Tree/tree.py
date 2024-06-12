# tree
'''
13
1 2 1 3 2 4 3 5 3 6 4 7 5 8 5 9 6 10 6 11 7 12 11 13
'''


def pre_order(T):
    print(T)
    if T:
        print(T, end=' ')
        pre_order(left[T])
        pre_order(right[T])


N = int(input())
E = N-1
arr = list(map(int, input().split()))
left = [0]*(N+1)    # 부모를 인덱스로 왼쪽자식번호 저장
right = [0]*(N+1)   # 부모를 인덱스로 오른쪽자식번호 저장
par = [0]*(N+1)     # 자식을 인덱스로 부모 저장
for i in range(E):
    p, c = arr[i*2], arr[i*2+1]
    # print(p, c)
    if left[p] == 0:    # 왼쪽 자식이 없으면
        left[p] = c
    else:
        right[p] = c
    par[c] = p

c = N
# root 찾는 과정. 마지막 번호 노드 가져와서 위까지 타고 올라가기
while par[c] != 0:  # 부모가 있으면
    c = par[c]      # 부모를 새로운 자식으로 두고
root = c            # 더이상 부모가 없으면
# print(root)
pre_order(root)