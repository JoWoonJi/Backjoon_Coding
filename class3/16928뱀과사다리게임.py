#복습
N, M = map(int, input().split())  # 사다리의 수 N과 뱀의 수 M
ladders = {}  # 사다리 정보를 저장할 딕셔너리
snakes = {}  # 뱀 정보를 저장할 딕셔너리

for _ in range(N):
    x, y = map(int, input().split())
    ladders[x] = y

for _ in range(M):
    u, v = map(int, input().split())
    snakes[u] = v

# 너비 우선 탐색(BFS) 알고리즘 구현
from collections import deque

def bfs():
    visited = [False] * 101  # 방문 여부 확인을 위한 리스트
    queue = deque([(1, 0)])  # (현재 위치, 주사위 굴린 횟수)

    while queue:
        position, count = queue.popleft()  # 현재 위치와 주사위 굴린 횟수를 가져옴

        if position == 100:  # 100번 칸에 도착한 경우
            return count  # 현재까지의 이동 횟수를 반환

        for i in range(1, 7):  # 주사위를 1부터 6까지 굴림
            next_position = position + i
            if next_position > 100 or visited[next_position]:  # 보드판을 벗어나거나 이미 방문한 칸인 경우
                continue

            visited[next_position] = True  # 방문 표시

            if next_position in ladders:  # 사다리가 있는 경우
                next_position = ladders[next_position]
            elif next_position in snakes:  # 뱀이 있는 경우
                next_position = snakes[next_position]

            queue.append((next_position, count + 1))  # 큐에 다음 위치와 이동 횟수 추가

# 최소 이동 횟수 계산
min_moves = bfs()
print(min_moves)