a,b,c,d,e=map(int,input().split())
print((a**2+b**2+c**2+d**2+e**2)%10)

#좀더 세련되게 
# n=list(map(int,input().split()))
# x=0
# for i in n:
#     x+=i**2
# print(x%10)