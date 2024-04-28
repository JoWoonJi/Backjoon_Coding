n=int(input())
x=list(map(int,input()))
s=0
for i in x:
    s+=i
print(s)

#간결하게
# input()
# print(sum(map(int,input())))