n = int(input())
bulks = []
for _ in range(n):
    x, y = map(int,input().split())
    bulks.append((x, y))

ranks = [1] * n
for i in range(n):
    for j in range(n):
        if bulks[i][0] < bulks[j][0] and bulks[i][1] < bulks[j][1]:#0은 첫번째인자:몸무게, 1은 두번째인자:키 // 즉 키와 몸무게 둘다 작을때 1 올려준다
            ranks[i] += 1
print(' '.join(map(str,ranks)))

# //

#함수로 깰끔하게 연습
# def bulk(n):
#     bulks = []
#     for _ in range(n):
#         x, y = map(int,input().split())
#         bulks.append((x, y))
#     ranks = [1] * n
#     for i in range(n):
#         for j in range(n):
#             if bulks[i][0] < bulks[j][0] and bulks[i][1] < bulks[j][1]:
#                 ranks[i] += 1
#     return ' '.join(map(str,ranks))
    
# n = int(input())
# print(bulk(n))

# //

# sorted사용해서. 더 쉬워질줄 알았는데 복잡.
# def bulk_rank_sorted():
#     n = int(input())
#     bulk_data = []
#     for i in range(n):
#         weight, height = map(int, input().split())
#         bulk_data.append((weight, height, i)) 

#     sorted_data = sorted(bulk_data, key=lambda x: (-x[0], x[1]))

#     ranks = [0] * n
#     for i in range(n):
#         rank = 1
#         for j in range(i):
#             if bulk_data[sorted_data[j][2]][1] > bulk_data[sorted_data[i][2]][1]:
#                 rank += 1
#         ranks[sorted_data[i][2]] = rank 

#     return ' '.join(map(str, ranks))

# print(bulk_rank_sorted())

