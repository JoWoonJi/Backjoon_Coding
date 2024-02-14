#동적 프로그래밍
n = int(input())
d = [0] * (n + 1)
for i in range(2, n + 1):
    d[i] = d[i - 1] + 1
    if i % 2 == 0:
        d[i] = min(d[i], d[i // 2] + 1)
    if i % 3 == 0:
        d[i] = min(d[i], d[i // 3] + 1)
print(d[n])

#너무 큰수가 들어오면 recursion error
# n = int(input())
# m = {}
# def a(n, m):
#     if n in m:
#         return m[n]
#     if n == 1:
#         return 0
#     r = 1 + a(n - 1, m)
#     if n % 2 == 0:
#         r = min(r, 1 + a(n // 2, m))
#     if n % 3 == 0:
#         r = min(r, 1 + a(n // 3, m))
#     m[n] = r
#     return r
# print(a(n, m))
