#복습
def floyd_warshall(n, graph):
    # 그래프 초기화: i에서 j로 가는 직접적인 경로가 있으면 1, 없으면 0
    for k in range(n):
        for i in range(n):
            for j in range(n):
                # i에서 k를 거쳐 j로 가는 경로가 있는지 확인
                if graph[i][k] and graph[k][j]:
                    graph[i][j] = 1

    return graph

# 정점의 개수 N 입력 받기
N = int(input())

# 인접 행렬 입력 받기
graph = [list(map(int, input().split())) for _ in range(N)]

# 플로이드-워셜 알고리즘 수행
result = floyd_warshall(N, graph)

# 결과 출력
for row in result:
    print(' '.join(map(str, row)))
