n = int(input()) # input값
t = 0 # 첫번째 덧셈 인자
s = 0 # 두번째 덧셈 인자
sum = 0 # t + s
count = 1 # 연산횟수

if n < 10:
    s = n
else:
    t = int(str(n)[0])
    s = int(str(n)[1])

sum = t + s

def calculate(n, t, s, sum):
    global count

    if n == int(str(s) + str(sum)[(len(str(sum))-1)]):
        return
    
    t = s
    if sum < 10:
        s = sum
    else:
        s = int(str(sum)[1])

    sum = t + s
    count += 1
    calculate(n, t, s, sum)

calculate(n, t, s, sum)
print(count)