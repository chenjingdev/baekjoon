n = int(input()) # 수열의 크기
arr = list(map(int, input().split())) # 수열
dp = [1] * n

for i in range(n):
    for j in range(i):
        if arr[i] > arr[j]:
            dp[i] = max(dp[i], dp[j] + 1)

print(max(dp))
