n = int(input())
point = n
array = []
for i in range(n):
    array.append(list(map(int, input().split())))

white = 0
blue = 0

def paper(x, y, n, p):
    global white
    global blue
    global depth

    if n / 2 < 0.5: return

    jSum = 0

    for i in range(n):
        for j in range(n):
            # print(array, 'array')
            # print(x, "x")
            # print(y, "y")
            # print(i, "i")
            # print(j, "j")
            a = array[i + x][j + y]
            jSum += a

    # print(jSum,"jSum")
    if jSum == n**2:
        blue += 1
        return
    if jSum == 0:
        white += 1
        return
    
    n = int(n / 2)
    
    # print(x, "xx")
    # print(y, 'yy')
    # print(n, 'nn')
    # print(p, 'print')
    paper(x, y, n, "1사분면")
    paper(int(n + x), y, n, "2사분면")
    paper(x, int(n + y), n, "3사분면")
    paper(int(n + x), int(n + y), n, "4사분면")


paper(0, 0, n, "큰사각형")
print(white)
print(blue)