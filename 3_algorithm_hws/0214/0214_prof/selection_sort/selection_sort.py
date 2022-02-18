def selectionSort(arr, N) :
    for i in range(N-1) :
        minIdx = i
        for j in range(i+1, N) :
           if arr[minIdx] > arr[j] :
                minIdx = j
        print(f'가장 작은 값 : {minIdx}')
        print(f'현재 가장 왼쪽 idx : {i}')
        arr[i], arr[minIdx] = arr[minIdx], arr[i]
        print('='*30)
        print()
        print(arr)

arr = [8, 10, 53, 2, 16, 9, 42, 22]
N = len(arr)
print(arr)
selectionSort(arr, N)
