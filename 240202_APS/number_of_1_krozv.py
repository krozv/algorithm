# 연속한 1의 개수
'''
N개의 0과 1로 이루어진 수열에서 연속한 1의 개수 중 최대값 출력
T 테스트 케이스 1<=T<=10
N 수열의 길이 10<=N<1000
'''
import sys
sys.stdin = open('input_numberof1.txt', 'r')
T = int(input())
for t in range(1, T+1):
    N = int(input())
    num_list = list(map(int, input()))
    cnt = 0 # 1 개수 담을 그릇
    max_cnt = 0 # 최댓값 그릇
    for i in range(N):
        if num_list[i] == 0:
            cnt = 0
        else:
            cnt += 1

        if max_cnt < cnt:
            max_cnt = cnt
    print(f'#{t} {max_cnt}')