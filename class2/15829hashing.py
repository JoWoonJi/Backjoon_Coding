l = int(input())
low_alpha = input()
hash = 0
for i in range(l):
    hash += ((ord(low_alpha[i]) - 96)) * (31**i)
print(hash % 1234567891)