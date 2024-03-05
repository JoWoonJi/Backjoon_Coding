n,r,c=map(int,input().split())
def s(n,r,c):
  if n==0:
    return 0
  return 2*(r%2)+(c%2)+4*s(n-1,int(r/2),int(c/2))
print(s(n, r, c))

# n, r, c = map(int, input().split())

# def sol(n, r, c):
#   if n == 0:
#     return 0
#   return 2*(r%2)+(c%2) + 4*sol(n-1, int(r/2), int(c/2))

# print(sol(n, r, c))

# def z(n, r, c):
#     if n == 0:
#         return 0
#     half = 2 ** (n - 1)
#     if r < half and c < half:
#         return z(n - 1, r, c)
#     if r < half and c >= half:
#         return half * half + z(n - 1, r, c - half)
#     if r >= half and c < half:
#         return 2 * half * half + z(n - 1, r - half, c)
#     return 3 * half * half + z(n - 1, r - half, c - half)

# N, r, c = map(int, input().split())

# print(z(N, r, c))