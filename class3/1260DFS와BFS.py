#다시 공부하기
def dfs(graph, v, visited):
    visited[v] = True
    print(v, end=' ')
    for i in sorted(graph[v]):
        if not visited[i]:
            dfs(graph, i, visited)

def bfs(graph, start):
    visited = [False] * (len(graph) + 1)
    queue = [start]
    visited[start] = True
    while queue:
        v = queue.pop(0)
        print(v, end=' ')
        for i in sorted(graph[v]):
            if not visited[i]:
                queue.append(i)
                visited[i] = True

N, M, V = map(int, input().split())
graph = [[] for _ in range(N + 1)]

for _ in range(M):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

visited = [False] * (N + 1)
dfs(graph, V, visited)
print()
bfs(graph, V)