def binary_search(array, target, start, end):
    while start <= end:
        mid = (start + end) // 2
        if array[mid] == target:
            return 1  # 타겟을 찾은 경우
        elif array[mid] > target:
            end = mid - 1
        else:
            start = mid + 1
    return 0  # 타겟을 찾지 못한 경우

n = int(input())
a = list(map(int, input().split()))
a.sort()  # 이분 탐색을 위해 배열을 먼저 정렬
m = int(input())
targets = list(map(int, input().split()))

for target in targets:
    print(binary_search(a, target, 0, n-1))
