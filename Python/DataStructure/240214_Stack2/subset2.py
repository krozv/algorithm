# subset1
def f(i, k, s, t): # k개의 원소를 가진 배열 A에서, 부분집합의 합이 t인 경우
    global cnt
    cnt += 1
    if s == t:  # 모든 원소에 대해 결정하면
        for j in range(k):
            if bit[j]:
                print(A[j], end= ' ')
        print()
    elif i==k:  # 모든 원소를 고려했으나 s != t
        return
    elif s > t:
        return
    else:
        bit[i]= 1
        f(i+1, k, s+A[i], t)
        bit[i] = 0
        f(i + 1, k, s, t)


N = 10
A = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
bit = [0] * N   # bit[i]는 A[i]의 부분집합 포함여부를 알려줌
cnt = 0
f(0, N, 0, 55)

print('cnt:', cnt)
