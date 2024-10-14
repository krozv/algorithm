# 돌 게임
'''
탁자 위에 돌 N개
상근이 창영이 턴 번갈아가면서 돌 1 or 3
마지막 돌 가져가면 이김
이기는 사람을 구하는 프로그램
게임은 상근이가 먼저 시작
상근 SK
창영 CY
2의 배수, 4의 배수?
'''
import sys
sys.stdin = open('input.txt', 'r')
input = sys.stdin.readline

N = int(input())
# 홀수
if N%2:
    print('SK')
# 짝수
else:
    print('CY')