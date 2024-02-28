# 도전: 화장실 문제
arr = [15, 30, 50, 10]
arr.sort(reverse=True)
cnt = 0
for idx, t in enumerate(arr):
    cnt += idx * t
print(cnt)

# 강사님 코드
person = [15, 30, 50, 10]
n = len(person)
person.sort()
sum = 0
left_person = n -1  # 화장실을 아직 이용하지 못한 대기자의 수

for turn in range(n):
    time = person[turn]
    # 누적합 += 남은시간 * 시간
    sum += left_person * time
    left_person -= 1
print(sum)

