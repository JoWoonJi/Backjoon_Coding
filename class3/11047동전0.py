n, k = map(int, input().split())
c = reversed([int(input()) for _ in range(n)])

r = 0
for i in c:
    if k >= i:
        r += k // i
        k %= i
print(r)
