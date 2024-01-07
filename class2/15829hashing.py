l = int(input())
alpha = input()
hash = 0
for i in range(l):
    hash += (ord(alpha[i])-96) * (31**i)
print(hash % 1234567891)