import sys
sys.stdin = open('input.txt', 'r')
input = sys.stdin.readline

N = int(input())
cards = list(map(int, input().split()))
dict = {}
for card in cards:
    if dict.get(card):
        dict[card] += 1
    else:
        dict[card] = 1
M = int(input())
arr = list(map(int, input().split()))
for i in arr:
    if dict.get(i):
        print(dict[i], end=' ')
    else:
        print(0, end=' ')