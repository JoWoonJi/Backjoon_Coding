n = list(map(int,input().split()))
check_n = 0
for i in range(len(n)):
    check_n += n[i]*n[i]

print(check_n % 10)