def find(parent, x):
    if parent[x] != x:
        parent[x] = find(parent, parent[x])
    return parent[x]

def union(parent, a, b):
    a = find(parent, a)
    b = find(parent, b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b

def kruskal(graph, v):
    parent = [0] * (v + 1)
    edges = []
    result = 0
    
    for i in range(1, v + 1):
        parent[i] = i
    
    for i in graph:
        edges.append((i[2], i[0], i[1]))
    
    edges.sort()
    
    for edge in edges:
        cost, a, b = edge
        if find(parent, a) != find(parent, b):
            union(parent, a, b)
            result += cost
    
    return result

# 그래프 입력 예시
v, e = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(e)]

print(kruskal(graph, v))
