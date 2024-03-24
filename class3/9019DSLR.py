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