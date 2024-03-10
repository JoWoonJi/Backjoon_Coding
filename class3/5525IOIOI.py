#복습
def count_houses(matrix, x, y, N):
    if x < 0 or x >= N or y < 0 or y >= N or matrix[y][x] == 0:
        return 0

    matrix[y][x] = 0
    count = 1

    count += count_houses(matrix, x+1, y, N)
    count += count_houses(matrix, x-1, y, N)
    count += count_houses(matrix, x, y+1, N)
    count += count_houses(matrix, x, y-1, N)

    return count

def solve(matrix, N):
    complexes = []

    for y in range(N):
        for x in range(N):
            if matrix[y][x] == 1:
                house_count = count_houses(matrix, x, y, N)
                complexes.append(house_count)

    complexes.sort()
    return len(complexes), complexes

N = int(input().strip())
matrix = [list(map(int, list(input().strip()))) for _ in range(N)]

complex_count, complexes = solve(matrix, N)

print(complex_count)
for count in complexes:
    print(count)
