# 0b110이 주어지면, BC 출력하는 함수
arr = ['A', 'B', 'C']
n = len(arr)

def get_sub(tar):
    for i in range(n):
        if tar & 0x1:
            print(arr[i], end='')
        tar >>= 1   # 검사한 한 자리를 제거

for tar in range(1<<n):
    print('{', end='')
    get_sub(tar)
    print('}')