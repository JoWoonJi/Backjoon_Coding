#복습
from collections import deque

N, K = map(int, input().split())

max_position = 100000
visited = [0] * (max_position + 1)
queue = deque([N])

while queue:
    current_position = queue.popleft()

    if current_position == K:
        print(visited[current_position])
        break

    for next_position in (current_position - 1, current_position + 1, current_position * 2):
        if 0 <= next_position <= max_position and not visited[next_position]:
            visited[next_position] = visited[current_position] + 1 
            queue.append(next_position)
