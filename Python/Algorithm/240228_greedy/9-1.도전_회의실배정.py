# 회의실 배정
"""
시작시작과 종료시간이 정해져 있는 여러 회의가 있음
가능한 많은 회의가 열리기 위해서는 회의들을 어떻게 배정해야 할까?
가장 종료시간이 가장 빠른 회의를 먼저 선택
"""

'''
10
1 4 1 6 6 10 5 7 3 8 5 9 3 5 8 11 2 13 12 14
'''
N = int(input())    # 회의 개수
arr = list(map(int, input().split()))
meeting = []
for i in range(N):
    si, fi = arr[i*2], arr[i*2+1]
    meeting.append((si, fi))
# 종료 시간 기준으로 오름차순 정렬
meeting.sort(key=lambda x: x[1])
cnt = 0 # 배정한 회의 수
end = 0 # 선택한 회의의 종료시간
for s, f in meeting:
    if s >= end:
        cnt += 1
        end = f # 새 회의 종료시간으로 값 변경
print(cnt)