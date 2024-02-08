import sys
input = sys.stdin.readline

n, m = map(int, input().split())
d = {}

for i in range(1, n+1):
    p = input().strip()
    d[p] = str(i)
    d[str(i)] = p
    
for _ in range(m):
    q = input().strip()
    print(d[q])