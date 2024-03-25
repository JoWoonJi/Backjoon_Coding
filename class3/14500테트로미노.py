#복습
#pypy3
n, m = map(int, input().split())
board = []
visited = [[False] * m for _ in range(n)]

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

for i in range(n):
    board.append(list(map(int, input().split())))

answer = 0

def dfs(x, y, mysum, depth):
    global answer

    if depth == 3:
        answer = max(answer, mysum)
        return
    else:
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or nx >= n or ny < 0 or ny >= m or visited[nx][ny]:
                continue

            if depth == 1:  # ㅗ 모양은 DFS로 만들 수 없으므로 예외처리
                visited[nx][ny] = True
                dfs(x, y, mysum + board[nx][ny], depth + 1)
                visited[nx][ny] = False

            visited[nx][ny] = True
            dfs(nx, ny, mysum + board[nx][ny], depth + 1)
            visited[nx][ny] = False


for i in range(n):
    for j in range(m):
        visited[i][j] = True
        dfs(i, j, board[i][j], 0)
        visited[i][j] = False

print(answer)

#python3
# n, m = map(int, input().split())
# board = []
# for i in range(n):
#     board.append(list(map(int, input().split())))

# tetris = [
#     [(0, 0), (0, 1), (1, 0), (1, 1)], # ㅡ
#     [(0, 0), (0, 1), (0, 2), (0, 3)], # ㅣ
#     [(0, 0), (1, 0), (2, 0), (3, 0)], # ㅁ
#     [(0, 0), (1, 0), (1, 1), (2, 1)], # h
#     [(1, 0), (0, 1), (1, 1), (2, 0)], # h 회전
#     [(1, 0), (1, 1), (0, 1), (0, 2)], # ...
#     [(0, 0), (0, 1), (1, 1), (1, 2)],
#     [(0, 0), (1, 0), (2, 0), (2, 1)], # L
#     [(0, 1), (1, 1), (2, 0), (2, 1)], # ...
#     [(0, 0), (0, 1), (1, 0), (2, 0)],
#     [(0, 0), (0, 1), (1, 1), (2, 1)],
#     [(1, 0), (0, 1), (1, 1), (1, 2)],
#     [(0, 0), (0, 1), (0, 2), (1, 1)],
#     [(0, 0), (1, 0), (1, 1), (1, 2)],
#     [(1, 0), (1, 1), (1, 2), (0, 2)],
#     [(0, 0), (0, 1), (0, 2), (1, 0)],
#     [(0, 0), (0, 1), (0, 2), (1, 2)],
#     [(0, 0), (1, 0), (1, 1), (2, 0)],
#     [(1, 0), (0, 1), (1, 1), (2, 1)] # ㅓ
# ]

# def solution(x, y):
#     global answer
#     for i in range(19):
#         tmp = 0
#         for j in range(4):
#             nx = x + tetris[i][j][0]
#             ny = y + tetris[i][j][1]

#             if nx < 0 or nx >= n or ny < 0 or ny >= m:
#                 break

#             tmp += board[nx][ny]

#         answer = max(answer, tmp)

# answer = 0
# for i in range(n):
#     for j in range(m):
#         solution(i, j)

# print(answer)

#숏코딩
# import sys
# R=range
# T=int
# M=map
# X=max
# I=sys.stdin.readline
# n,m=M(T,I().split())
# g=[[*M(T,I().split())]for _ in R(n)]
# v=[[1]*m for _ in R(n)]
# x=[-1,0,1,0]
# y=[0,1,0,-1]
# t=0
# b=X(M(X,g))
# def D(i,j,c,s):
#     global t,b
#     if s+b*(4-c)<t:return
#     if c==4:t=X(t,s);return
#     for _ in R(4):
#         k=i+x[_];l=j+y[_]
#         if 0<=k<n and 0<=l<m and v[k][l]:
#             if c==2:v[k][l]=0;D(i,j,c+1,s+g[k][l]);v[k][l]=1
#             v[k][l]=0;D(k,l,c+1,s+g[k][l]);v[k][l]=1
# for r in R(n):
#    for c in R(m):
#        v[r][c]=0;D(r,c,1,g[r][c]);v[r][c]=1 
# print(t)