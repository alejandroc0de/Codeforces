n,m = map(int, input().split())
cats = list(map(int, input().split()))

graph = [[] for _ in range (n+1)]
print(graph)

for _ in range(n-1):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)

print(graph)

ans = 0

def dfs(node,parent,consecutive):
    global ans
    