#간결하게
n=int(input())
m=int(input())
c=[[] for _ in range(n+1)]
for _ in range(m):
    a,b=map(int,input().split())
    c[a].append(b)
    c[b].append(a)
x=[False]*(n+1)
def v(c,s,x):
    x[s]=True
    for i in c[s]:
        if not x[i]:
            v(c,i,x)
v(c,1,x)
print(sum(x)-1)

# n = int(input())  
# m = int(input()) 

# connect = [[] for _ in range(n + 1)]

# for _ in range(m):
#     a, b = map(int, input().split())
#     connect[a].append(b)
#     connect[b].append(a)

# infection = [False] * (n + 1)

# def virus(connect, start, infection):
#     infection[start] = True
#     for i in connect[start]:
#         if not infection[i]:
#             virus(connect, i, infection)

# virus(connect, 1, infection)

# print(sum(infection) - 1)

#함수정의없이
# n = int(input())
# m = int(input())

# connect = [[] for _ in range(n + 1)]

# for _ in range(m):
#     a, b = map(int, input().split())
#     connect[a].append(b)
#     connect[b].append(a)

# infection = [False] * (n + 1)

# queue = [1]  
# infection[1] = True 

# while queue:
#     current = queue.pop(0)  
#     for i in connect[current]:
#         if not infection[i]:
#             infection[i] = True
#             queue.append(i)

# print(sum(infection) - 1)