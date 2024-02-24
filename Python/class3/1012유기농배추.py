#다시 공부하기
import sys

def count_earthworms(test_cases):
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    def dfs_iterative(x, y, grid):
        stack = [(x, y)]
        while stack:
            x, y = stack.pop()
            if grid[x][y] == 1:
                grid[x][y] = 0
                for dx, dy in directions:
                    nx, ny = x + dx, y + dy
                    if 0 <= nx < len(grid) and 0 <= ny < len(grid[0]) and grid[nx][ny] == 1:
                        stack.append((nx, ny))
    
    results = []
    for M, N, K, positions in test_cases:
        grid = [[0] * N for _ in range(M)]
        for x, y in positions:
            grid[x][y] = 1
        
        earthworms_count = 0
        for x in range(M):
            for y in range(N):
                if grid[x][y] == 1:
                    dfs_iterative(x, y, grid)
                    earthworms_count += 1
        results.append(earthworms_count)
    return results

sys.setrecursionlimit(10000)

T = int(input().strip())
test_cases = []
for _ in range(T):
    M, N, K = map(int, input().strip().split())
    positions = [tuple(map(int, input().strip().split())) for _ in range(K)]
    test_cases.append((M, N, K, positions))

results = count_earthworms(test_cases)
for result in results:
    print(result)

#유니온 파인드 알고리즘 사용
# def root(a,j):
# 	while a[j]!=-1:
# 		j=a[j]
# 	return j
# for i in range(int(input())):
# 	M,N,K=map(int,input().split())
# 	b=[list(map(int, input().split())) for x in range(K)]
# 	a=K*[-1]
# 	for j in range(len(b)):
# 		for k in range(j+1,len(b)):
# 			x=b[j][0]-b[k][0]
# 			y=b[j][1]-b[k][1]
# 			if (abs(x)==1 and y==0 or abs(y)==1 and x==0):
# 				if a[k]<0:a[k]=j
# 				elif root(a,j)!=root(a,k): a[root(a,j)]=k
# 	print(a.count(-1))