#복습
from collections import deque

n, m = map(int, input().split())

#땅, 거리 설정
land = [list(map(int, input().split())) for _ in range(n)]
dis = [[0] * m for _ in range(n)]

dx, dy = [1, -1, 0, 0], [0, 0, 1, -1]

#bfs 세팅            
def bfs(i, j):
    q = deque()
    q.append((i, j))
    
    while q:
        x, y = q.popleft()
        
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            
            if 0 <= nx < n and 0 <= ny < m and dis[nx][ny] == 0 and land[nx][ny] == 1:
                dis[nx][ny] = dis[x][y] + 1
                q.append((nx, ny))

#시작 위치 찾기                
for i in range(n):
    for j in range(m):
        if land[i][j] == 2:
            bfs(i, j)

#도달하지 못한 땅 처리            
for i in range(n):
    for j in range(m):
        if land[i][j] == 1 and dis[i][j] == 0:
            dis[i][j] = -1

#출력 형식 맞추기
for i in range(n):
    for j in range(m):
        print(dis[i][j], end = ' ')
    print()