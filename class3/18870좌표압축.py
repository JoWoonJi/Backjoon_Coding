n=int(input())
l=list(map(int,input().split()))
s=sorted(set(l))
d={}
for i in range(len(s)):
    d[s[i]]=i
for i in l:
    print(d[i],end=" ")

# def coordinate_compression(N, X):
#     unique_sorted_X = sorted(set(X)) 
#     compression_dict = {value: index for index, value in enumerate(unique_sorted_X)}
#     compressed_X = [compression_dict[x] for x in X]
#     return ' '.join(map(str, compressed_X))

# N = int(input()) 
# X = list(map(int, input().split()))

# print(coordinate_compression(N, X))
