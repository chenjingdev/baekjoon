def hanoi(n, start, end, aux):
    if n == 1:
        print(start, end)
        return
    # n-1개를 aux로 이동
    hanoi(n-1, start, aux, end)
    print(start, end)
    # n-1개를 end로 이동
    hanoi(n-1, aux, end, start)

n = int(input())
print(2**n - 1)

if n <= 20:
    hanoi(n, 1, 3, 2)
