#복습
import sys
from collections import deque

input = sys.stdin.readline
MOD = 10000

def D(n):
    return (n * 2) % MOD, 'D'

def S(n):
    return (n - 1) % MOD, 'S'

def L(n):
    return (10 * n + (n // 1000)) % MOD, 'L'

def R(n):
    return (n // 10 + (n % 10) * 1000) % MOD, 'R'

commands = [D, S, L, R]
    
def bfs(a, b):
    q = deque([(a, '')])
    visited = set()
    
    while q:
        x, command = q.popleft()
        
        if x == b:
            print(command)
            return
        
        for i in commands:
            j, c = i(x)
            if j not in visited:
                visited.add(j)
                q.append((j, command + c))

for _ in range(int(input())):
    N, K = map(int, input().split())
    bfs(N, K)

# import sys
# from collections import deque

# cmd = {0:'D', 1:'S', 2:'L', 3:'R'}

# def D(n):
#     return (n * 2) % 10000

# def S(n):
#     if n == 0: return 9999
#     return n - 1

# def L(n):
#     return (n % 1000) * 10 + n // 1000

# def R(n):
#     return (n % 10) * 1000 + n // 10

# def solve():
#     a, b = map(int, sys.stdin.readline().rstrip().split())
#     visited = [False for _ in range(10000)]
#     q = deque()
#     q.append([a, ''])
#     visited[a] = True

#     while q:
#         cn, path = q.popleft()

#         if cn == b:
#             print(path)
#             break

#         nns = [D(cn), S(cn), L(cn), R(cn)]

#         for i in range(4):
#             nn = nns[i]

#             if not visited[nn]:
#                 visited[nn] = True
#                 q.append([nn, path+cmd[i]])


# tc = int(sys.stdin.readline().rstrip())

# while tc:
#     solve()
#     tc -= 1