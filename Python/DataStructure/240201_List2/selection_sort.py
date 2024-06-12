# selection sort
def selection_sort(a:[], n:int):
    for i in range(n-1):
        min_index = i
        for j in range(i+1, n):
            # 최솟값이랑 비교
            if a[min_index] > a[j]:
                min_index = j
        a[i], a[min_index] = a[min_index], a[i]


a = [1, 45, 48, 4, 4]
selection_sort(a, 5)
print(a)