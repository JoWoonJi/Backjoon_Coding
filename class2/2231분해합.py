
#간결하게
n = int(input())
for i in range(1, n):
    if i + sum(map(int, str(i))) == n:
        print(i)
        break
else:
    print("0")



# n = input() 

# for i in range(1, int(n)):
#     sum_each_n = sum(int(digit) for digit in str(i))
#     disassemble_sum = i + sum_each_n
#     if disassemble_sum == int(n):
#         print(i)
#         break
# else:
#     print("0")