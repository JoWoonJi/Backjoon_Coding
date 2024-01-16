# 리스트 컴프리헨션 사용 
import sys

n = int(sys.stdin.readline().strip())
m_data = [sys.stdin.readline().strip().split() for _ in range(n)]
m_data = [(int(age), name) for age, name in m_data]

def sort_m(m_data):
    age_list = [[] for _ in range(201)]
    for age, name in m_data:
        age_list[age].append(name)
    return [(age,name) for age in range(201) for name in age_list[age]]
for i in sort_m(m_data):
    print(i[0], i[1])

# //

#리스트 컴프리헨션 사용하지 않고.
# import sys

# n = int(sys.stdin.readline().strip())
# m_data = []
# for _ in range(n):
#     age, name = sys.stdin.readline().strip().split()
#     m_data.append((int(age), name))

# def sort_m(m_data):
#     age_list = [[] for _ in range(201)]
#     for age, name in m_data:
#         age_list[age].append(name)

#     sorted_members = []
#     for age in range(201):
#         for name in age_list[age]:
#             sorted_members.append((age, name))
#     return sorted_members

# sorted_m = sort_m(m_data)

# for i in sorted_m:
#     print(i[0], i[1])

# //

# #시간 초과에 걸릴뻔 했기에 sys로 
# import sys

# def sort_members(n, member_data):
#     # 나이가 200살까지가 범위라서 배열을 미리 할당 
#     age_sorted = [[] for _ in range(201)]
#     for age, name in member_data:
#         age_sorted[age].append(name)
    
#     result = []
#     for age in range(201):
#         for name in age_sorted[age]:
#             result.append((age, name))
#     return result

# n = int(sys.stdin.readline().strip())
# member_data = []

# for _ in range(n):
#     age, name = sys.stdin.readline().strip().split()
#     member_data.append((int(age), name))

# sorted_members = sort_members(n, member_data)

# for member in sorted_members:
#     print(member[0], member[1])

# //

#시간초과가 되진 않았지만 위의 코드와 256ms 4024ms 정도로 속도차이가 난다.
#첫시도
# def sort_members(n, member_data):
    
#     member_data.sort(key=lambda x: x[0])
#     return member_data

# n = int(input())
# member_data = []

# for _ in range(n):
#     age, name = input().split()
#     member_data.append((int(age), name))

# sorted_members = sort_members(n, member_data)

# for member in sorted_members:
#     print(member[0], member[1])

# //

#첫 시도를 간결하게. 코드는 간단하지만 오래걸려서 문제에 부합하지 않는듯
# n = int(input())
# m_data = []
# for _ in range(n):
#     age, name = input().split()
#     m_data.append((int(age), name))
# m_data.sort(key=lambda x: x[0])
# for i in m_data:
#     print(i[0], i[1])
