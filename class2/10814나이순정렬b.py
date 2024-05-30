import sys
input = sys.stdin.read
data = input().strip().split('\n')
N = int(data[0])
members = [(int(age), name) for age, name in (line.split() for line in data[1:N+1])]
members.sort(key=lambda x: x[0])
for age, name in members:
    print(age, name)