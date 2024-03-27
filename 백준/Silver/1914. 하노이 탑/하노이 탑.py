#하노이 함수
def hanoi_f(start, end, n):
    if n == 1:
        print(start,end)
        return

    hanoi_f(start, 6-start-end, n-1) #1단계 (1->2)
    print(start, end) #2단계 (마지막원반 1->3)
    hanoi_f(6-start-end, end, n-1) #3단계 (2->3)

#메인
n = int(input())
print(2**n-1)

if n <= 20:
    hanoi_f(1,3,n)

    