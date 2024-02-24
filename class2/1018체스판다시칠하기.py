#함수 없이
n, m = map(int, input().split())
board = [input() for _ in range(n)]

min_repaints = min(
    sum((board[i + row][j + col] == color) ^ ((i + j) % 2 == 0) for i in range(8) for j in range(8))
    for row in range(n - 7) for col in range(m - 7) for color in 'BW'
)

print(min_repaints)

# //

# #함수
# def count_mismatches(board, row, col, color):
#     return sum((board[row + i][col + j] == color) ^ ((i + j) % 2 == 0) for i in range(8) for j in range(8)) # ^는 xor 이므로 값이 다를때 true(1)을 반환하고 그값이 더해진다. 다른 개수의 count를 올리는것과 같다.

# def find_min_repaints(board, n, m):
#     return min(min(count_mismatches(board, i, j, c) for i in range(n - 7) for j in range(m - 7)) for c in 'BW')

# n, m = map(int, input().split())
# board = [input() for _ in range(n)]

# print(find_min_repaints(board, n, m))

# 비트 연산자
# & : 비트 AND. 예: a & b
# | : 비트 OR. 예: a | b
# ^ : 비트 XOR (배타적 논리합). 예: a ^ b
# ~ : 비트 NOT (1의 보수). 예: ~a
# << : 비트 왼쪽 시프트. 예: a << b
# >> : 비트 오른쪽 시프트. 예: a >> b

# //

# def count_mismatches(board, start_row, start_col, color):
#     count = 0
#     for i in range(8):
#         for j in range(8):
#             if (i + j) % 2 == 0:
#                 if board[start_row + i][start_col + j] != color:
#                     count += 1
#             else:
#                 if board[start_row + i][start_col + j] == color:
#                     count += 1
#     return count

# def find_min_repaints(board, n, m):
#     min_repaints = float('inf')
#     for i in range(n - 7):
#         for j in range(m - 7):
            
#             min_repaints = min(min_repaints, 
#                                count_mismatches(board, i, j, 'W'), 
#                                count_mismatches(board, i, j, 'B'))
#     return min_repaints

# n, m = map(int, input().split())
# board = [input() for i in range(n)]

# min_repaints = find_min_repaints(board, n, m)

# print(min_repaints)