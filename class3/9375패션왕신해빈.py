#간결하게
t=int(input())
for _ in range(t):
    c=[input().split()[1] for _ in range(int(input()))]
    x=1
    for i in set(c):
        x*=c.count(i)+1
    print(x-1)

# test_cases = int(input().strip())
# for _ in range(test_cases):
#     clothes = [input().strip().split()[1] for _ in range(int(input().strip()))]
#     combinations = 1
#     for kind in set(clothes):
#         combinations *= clothes.count(kind) + 1
#     print(combinations - 1)

# #모듈없이
# def calculate_combinations(clothes):
#     clothes_counter = {}
#     for _, kind in clothes:
#         clothes_counter[kind] = clothes_counter.get(kind, 0) + 1

#     combinations = 1
#     for count in clothes_counter.values():
#         combinations *= (count + 1)
    
#     return combinations - 1

# test_cases = int(input().strip())
# results = []

# for _ in range(test_cases):
#     n = int(input().strip())
#     clothes = [input().strip().split() for _ in range(n)]
#     results.append(calculate_combinations(clothes))

# for result in results:
#     print(result)


#모듈사용
# def calculate_combinations(clothes):
#     from collections import Counter
#     from functools import reduce
#     clothes_counter = Counter([kind for _, kind in clothes])
 
#     combinations = reduce(lambda x, y: x * y, [count + 1 for count in clothes_counter.values()]) - 1
    
#     return combinations

# try:
#     test_cases = int(input().strip())
#     results = []

#     for _ in range(test_cases):
#         n = int(input().strip())
#         if n == 0:
#             results.append(0) 
#             continue
#         clothes = [input().strip().split() for _ in range(n)]
#         results.append(calculate_combinations(clothes))

#     for result in results:
#         print(result)
# except ValueError as e:
#     print(f"Invalid input: {e}")

