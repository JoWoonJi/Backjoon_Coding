# 간결하게
import sys
input = sys.stdin.readline

n = int(input())
m = [int(input()) for _ in range(n)]

stk, op, cnt, TF = [], [], 1, True

for i in m:
    while cnt <= i:
        stk += [cnt]
        op += '+'
        cnt += 1
    if stk.pop() != i:
        TF = False
        break
    op += '-'
print('\n'.join(op) if TF else 'NO')

# import sys
# input = sys.stdin.readline

# n = int(input()) 
# seq = [int(input()) for _ in range(n)] 

# stk, op, cnt = [], [], 1
# psbl = True

# for num in seq:
#     while cnt <= num:  # 현재 숫자까지 스택에 push
#         stk.append(cnt)
#         op.append('+')
#         cnt += 1
#     if stk[-1] == num:  # 스택의 top이 현재 숫자와 같으면 pop
#         stk.pop()
#         op.append('-')
#     else:
#         psbl = False
#         break

# if psbl:
#     for i in op:
#         print(i)
# else:
#     print('NO')
