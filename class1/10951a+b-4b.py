while True:
    try:
        a,b=map(int,input().split())
        print(a+b)
    except:
        break

#다른 간결한 방법
# import sys
# for x in sys.stdin:
#     a,b=map(int,x.split())
#     print(a+b)