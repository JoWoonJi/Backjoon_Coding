# 비트마스크 방법
import sys
input = sys.stdin.readline

m = int(input())
s = 0

for _ in range(m):
    cmd = input().split()
    c = cmd[0]
    if len(cmd) > 1:
        x = int(cmd[1]) - 1
        
    if c == 'add':
        s |= (1 << x)
    elif c == 'remove':
        s &= ~(1 << x)
    elif c == 'check':
        print(1 if s & (1 << x) else 0)
    elif c == 'toggle':
        s ^= (1 << x)
    elif c == 'all':
        s = (1 << 20) - 1
    elif c == 'empty':
        s = 0

# # 집합(set) 방법
# import sys
# input = sys.stdin.readline

# m = int(input())
# s = set()

# for _ in range(m):
#     cmd = input().split()
#     c = cmd[0]
#     if len(cmd) > 1:
#         x = int(cmd[1])
    
#     if c == 'add':
#         s.add(x)
#     elif c == 'remove':
#         s.discard(x)
#     elif c == 'check':
#         print(1 if x in s else 0)
#     elif c == 'toggle':
#         if x in s:
#             s.discard(x)
#         else:
#             s.add(x)
#     elif c == 'all':
#         s = set(range(1, 21))
#     elif c == 'empty':
#         s.clear()