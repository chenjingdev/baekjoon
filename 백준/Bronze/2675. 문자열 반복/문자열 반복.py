caseLength = int(input())
for i in range(caseLength):
    a, b = map(str, input().split())
    a = int(a)
    b = list(b)
    c = []
    for j in range(len(b)):
        c.append(b[j] * a)

    print("".join(c))