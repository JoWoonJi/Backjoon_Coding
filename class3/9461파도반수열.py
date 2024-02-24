#간결하게
def w(n):
    p=[0,1,1,1,2,2]
    for i in range(6,n+1):
        p.append(p[i-1]+p[i-5])
    return p[n]
t=int(input())
for _ in range(t):
    n=int(input())
    print(w(n))

# def wave_sequence(N):
#     P = [0, 1, 1, 1, 2, 2] 

#     for i in range(6, N + 1):
#         P.append(P[i - 1] + P[i - 5])

#     return P[N]

# T = int(input())

# for _ in range(T):
#     N = int(input())  
#     print(wave_sequence(N)) 
