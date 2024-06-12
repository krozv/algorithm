# 이진수2
"""
십진수 N: 0<N<1 -> 이진수로 바꿈
0.625 -> 0.101
소수점 아래 12자리 이내인 이진수로 표시할 수 있으면 0.을 제외한 나머지 숫자 출력
13자리 이상 = overflow 출력
"""
T = int(input())
for t in range(1, T+1):
    N = float(input())
    b = ''
    for i in range(1, 14):
        if N == 0:
            print(f'#{t} {b}')
            break
        if i == 13:
            print(f'#{t} overflow')
            break
        if N >= 2**(-i):
            N -= 2 **(-i)
            b += '1'
        else:
            b += '0'