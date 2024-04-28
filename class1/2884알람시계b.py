h,m=map(int,input().split())
if m<45:
    if h==0:
        print(23,(m+15))
    else:
        print((h-1),(m+15))
else:
    print(h,m-45)

# h,m=map(int,input().split())
# if m<45:
#     if h==0:
#         h=23
#         m+=15
#     else:
#         h-=1
#         m+=15
# else:
#     m-=45
# print(h,m)

#더 수학적+파이써닉하게
# h,m=map(int,input().split())
# print((h-(m<45))%24,(m-45)%60)