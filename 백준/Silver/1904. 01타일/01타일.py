n = int(input())

_dic = [0] * 1000005

_dic[1] = 1
_dic[2] = 2

for i in range(3, n+1):
    _dic[i] = (_dic[i - 1] + _dic[i - 2]) % 15746

print(_dic[n])