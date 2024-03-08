import sys
i=sys.stdin.readline
n=int(i())
m=[]
for _ in range(n):
    a,z=map(int,i().split())
    m.append((a,z))
m.sort(key=lambda x:(x[1],x[0]))
c=1
t=m[0][1]
for i in range(1,n):
    if m[i][0]>=t:
        c+=1
        t=m[i][1]
print(c)

# import sys
# input=sys.stdin.readline
# n = int(input())
# meetings = []

# for _ in range(n):
#     start, end = map(int, input().split())
#     meetings.append((start, end))

# meetings.sort(key=lambda x: (x[1], x[0]))

# count = 1
# end_time = meetings[0][1]

# for i in range(1, n):
#     if meetings[i][0] >= end_time:
#         count += 1
#         end_time = meetings[i][1]

# print(count)
