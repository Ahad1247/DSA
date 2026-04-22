n , m = map(int,input().split())
graph = {i:[] for i in range(1,n+1)}

for _ in range(m):
    u , v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)
for vertex in graph:
    print(vertex, ":", graph[vertex])