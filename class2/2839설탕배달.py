n = int(input())
bags = 0

while n >= 0:
    if n % 5 == 0:
        bags += n // 5
        print(bags)
        break
    n -= 3 # 3을 빼주고 다시 반복문. 
    bags += 1
else:
    print(-1)