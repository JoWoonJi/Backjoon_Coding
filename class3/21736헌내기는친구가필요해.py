#다시
from collections import deque

n, m = map(int, input().split())

campus = [input() for _ in range(n)]

for i in range(n):
    for j in range(m):
        if campus[i][j] == 'I':
            start = (i, j)
            break

queue = deque([start])
visited = [[False] * m for _ in range(n)]
visited[start[0]][start[1]] = True
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

count = 0

while queue:
    x, y = queue.popleft()
    for i in range(4):
        nx, ny = x + dx[i], y + dy[i]
        if 0 <= nx < n and 0 <= ny < m and not visited[nx][ny]:
            if campus[nx][ny] == 'O' or campus[nx][ny] == 'P':
                if campus[nx][ny] == 'P':
                    count += 1
                queue.append((nx, ny))
                visited[nx][ny] = True

print(count if count > 0 else 'TT')
