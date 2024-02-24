n = int(input())
hive = 1
common_diff = 1
while n > hive:
    hive += 6 * common_diff
    common_diff += 1
print(common_diff)