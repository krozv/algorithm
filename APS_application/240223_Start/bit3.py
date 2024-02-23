# 비트연산 문제 풀어보기
N, M = map(int, input().split())
print(str(bin(M)))
for i in range(N):
    if not 1 & M >> i:
        break
else:
    print('ON')