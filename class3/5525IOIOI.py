N = int(input())
M = int(input())
S = input()

def count_pn(N, S):
    target = 'I' + 'OI' * N 
    count = 0
    for i in range(len(S) - len(target) + 1):
        if S[i:i+len(target)] == target:
            count += 1
    return count

count = count_pn(N, S)
print(count)
