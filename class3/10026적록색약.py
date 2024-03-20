#복습
from queue import Queue

def bfs(start, grid, visited, n, is_color_blind):
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]  # 상, 하, 좌, 우 방향
    q = Queue()
    q.put(start)
    visited[start[0]][start[1]] = True
    while not q.empty():
        x, y = q.get()
        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            if 0 <= nx < n and 0 <= ny < n and not visited[nx][ny]:
                if is_color_blind:
                    if (grid[x][y] in ['R', 'G'] and grid[nx][ny] in ['R', 'G']) or grid[x][y] == grid[nx][ny]:
                        visited[nx][ny] = True
                        q.put((nx, ny))
                else:
                    if grid[x][y] == grid[nx][ny]:
                        visited[nx][ny] = True
                        q.put((nx, ny))

def count_regions(grid, n, is_color_blind):
    visited = [[False] * n for _ in range(n)]
    count = 0
    for i in range(n):
        for j in range(n):
            if not visited[i][j]:
                bfs((i, j), grid, visited, n, is_color_blind)
                count += 1
    return count

# 사용자 입력 받기
n = int(input())
grid = []
for i in range(n):
    grid.append(input().strip())

# 적록색약이 아닌 사람과 적록색약인 사람의 구역 수 계산
normal_count = count_regions(grid, n, False)
color_blind_count = count_regions(grid, n, True)

print(normal_count,color_blind_count)