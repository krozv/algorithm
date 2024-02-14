# subset1
def f(i, k, t): # k개의 원소를 가진 배열 A에서, 부분집합의 합이 t인 경우
    if i == k:  # 모든 원소에 대해 결정하면
        ss = 0  # 부분집합의 합
        for j in range(k):
            if bit[j]:     # A[j]가 포함된 경우
                ss += A[j]
        if ss==t:
            for j in range(k):
                if bit[j]:
                    print(A[j], end = ' ')
            print()
    else:
        for j in range(1, -1, -1):
            bit[i] = j
            f(i+1, k, t)


N = 10
A = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
bit = [0] * N   # bit[i]는 A[i]의 부분집합 포함여부를 알려줌
f(0, N, 10)

# 박주연 화이팅 <3
