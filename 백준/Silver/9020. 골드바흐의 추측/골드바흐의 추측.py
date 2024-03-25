def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def goldbach(n, primes):
    for i in range(n//2, 1, -1):
        if i in primes and (n-i) in primes:
            return i, n-i
    return None, None

# 에라토스테네스의 체를 이용하여 10000까지의 소수를 찾는다.
primes = {i for i in range(2, 10001) if is_prime(i)}

T = int(input())
for _ in range(T):
    n = int(input())
    a, b = goldbach(n, primes)
    print(a, b)
