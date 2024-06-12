# bubble sort
'''
a 배열
N 배열의 원소 개수
'''
# 오름차순
def bubble_sort(a:[int], n:int):
    for i in range(n-1):
        for j in range(i+1, n):
            if a[i] > a[j]:
                a[i], a[j] = a[j], a[i]
    return a

arr = [3, 4, 55, 298, 93, 34, 54]
n = 7
print(bubble_sort(arr, n))