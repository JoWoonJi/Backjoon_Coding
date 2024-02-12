#숏코딩. 시간은 오래걸리는데 통과는 된다.
n,m=map(int,input().split())
f={}
for _ in range(n):
    s,p=input().split()
    f[s]=p
for _ in range(m):
    print(f[input()])

# import sys
# input = sys.stdin.readline

# n, m = map(int, input().split())
# sp = {}
# for _ in range(n):
#     s, p = input().split()
#     sp[s] = p

# for _ in range(m):
#     f = input()
#     print(sp[f])