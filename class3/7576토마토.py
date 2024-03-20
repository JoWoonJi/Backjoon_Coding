# 복습
from collections import deque

def bfs(tomatoes, m, n):
    queue = deque([(i, j) for i in range(n) for j in range(m) if tomatoes[i][j] == 1])
    directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
    days = -1
    while queue:
        days += 1
        for _ in range(len(queue)):
            x, y = queue.popleft()
            for dx, dy in directions:
                nx, ny = x + dx, y + dy
                if 0 <= nx < n and 0 <= ny < m and tomatoes[nx][ny] == 0:
                    tomatoes[nx][ny] = 1
                    queue.append((nx, ny))
    return days if all(0 not in row for row in tomatoes) else -1

m, n = map(int, input().split())
tomatoes = [list(map(int, input().split())) for _ in range(n)]

print(bfs(tomatoes, m, n))