#간결하게
import sys
i=sys.stdin.readline
N,M=map(int,i().split())
g=[[] for _ in range(N+1)]
v=[False]*(N+1)
for _ in range(M):
    u,f=map(int,i().split()); g[u].append(f); g[f].append(u)
c=0
for j in range(1,N+1):
    if not v[j]:
        k=[j]
        while k:
            p=k.pop()
            if not v[p]: v[p]=True; [k.append(w) for w in g[p] if not v[w]]
        c+=1
print(c)

#시간초과, pypy3로하면 됨
# def dfs(graph, v, visited):
#     visited[v] = True
#     for i in graph[v]:
#         if not visited[i]:
#             dfs(graph, i, visited)

# N, M = map(int, input().split())
# graph = [[] for _ in range(N + 1)]
# visited = [False] * (N + 1)

# for _ in range(M):
#     u, v = map(int, input().split())
#     graph[u].append(v)
#     graph[v].append(u)

# count = 0
# for i in range(1, N + 1):
#     if not visited[i]:
#         dfs(graph, i, visited)
#         count += 1

# print(count)
