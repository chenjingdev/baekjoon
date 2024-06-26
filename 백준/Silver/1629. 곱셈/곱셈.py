def power(a, b, c):
    if b == 0:
        return 1
    half = power(a, b // 2, c)
    if b % 2 == 0:
        return (half * half) % c
    else:
        return (half * half * a) % c

a, b, c = map(int, input().split())
print(power(a, b, c))
