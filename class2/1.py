n = int(input())
n_list = map(int,input().split())
count = 0
for i in n_list:
    for j in range(2,i):
        if i % j == 0:
            break
    else:
        if i > 1:
            count += 1
print(count)
    