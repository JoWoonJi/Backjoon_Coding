#간결하게
t = int(input())

for _ in range(t):
    n = int(input()) 
    z, o = 1, 0 

    for _ in range(n):
        z, o = o, z + o 

    print(z, o)

#함수
# t = int(input())

# def fibonacci(n):
#     if n == 0:
#         return (1, 0)
#     elif n == 1:
#         return (0, 1)

#     z = [0] * (n + 1)
#     o = [0] * (n + 1)
#     z[0], o[1] = 1, 1

#     for i in range(2, n + 1):
#         z[i] = z[i-1] + z[i-2]
#         o[i] = o[i-1] + o[i-2]

#     return (z[n], o[n])

# for _ in range(t):
#     n = int(input())
#     z, o = fibonacci(n)
#     print(z, o)