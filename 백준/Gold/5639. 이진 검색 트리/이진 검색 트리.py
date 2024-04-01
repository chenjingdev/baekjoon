import sys
sys.setrecursionlimit(10**6)

def postorder(start, end):
    if start > end:
        return
    root = pre[start]
    idx = start + 1
    
    while idx <= end:
        if pre[idx] > root:
            break
        idx += 1
    
    postorder(start + 1, idx - 1)
    postorder(idx, end)
    print(root)

pre = []
while True:
    try:
        pre.append(int(input()))
    except:
        break

postorder(0, len(pre) - 1)
