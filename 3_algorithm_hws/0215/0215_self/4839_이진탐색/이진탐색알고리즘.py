def bynarySearch(a, n, key):
    start = 0
    end = n - 1 #인덱스니까 전체 길이 - 1
    while start <= end: #시작부터 끝까지
        middle = (start + end) // 2 #중앙값을 기준으로 찾아보고
        if a[middle] == key: #중앙값이 내가 원하는 값이면 끝남
            return True
        elif a[middle] > key: #원하는 값이 아니고, 원하는 값이 중앙값 보다 앞에 위치
            end = middle - 1

        else: #원하는 값이 중앙값 보다 뒤에 위치
            start = middle + 1

    return False #검색 실패
