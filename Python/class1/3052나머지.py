list = []
for i in range(10):
    n = int(input())
    rest = n % 42
    list.append(rest)

print(len(set((list))))