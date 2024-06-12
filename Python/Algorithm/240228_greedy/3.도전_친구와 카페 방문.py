# 도전: 친구와 카페 방문
arr = ['A', 'B', 'C', 'D', 'E']
n = len(arr)

def get_fr(tar):
    cnt = 0
    for i in range(n):
        # 1비트가 1인지 확인
        if tar & 0x1:
            cnt += 1
        # right shift 연산
        tar >>= 1
    return cnt


result = 0
for tar in range(1<<n):
    # get_fr(tar)의 리턴값이 2이상일 경우
    if get_fr(tar) >= 2:
        result += 1
print(result)

