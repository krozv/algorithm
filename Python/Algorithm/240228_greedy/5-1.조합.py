# 재귀 이용해서 조합 만들기
def nCr(n, r, s):
    """
    n: 전체 개수
    r: 앞으로 골라야 할 숫자 개수
    s: 현재 위치
    """
    if r == 0:
        print(*comb)
    else:
        for i in range(s, n-r+1):
            comb[r-1] = A[i]
            nCr(n, r-1, i+1)


A = [1, 2, 3, 4, 5]
N = 5
R = 3
comb = [0] * R
nCr(5, 3, 0)