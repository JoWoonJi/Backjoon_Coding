n=input()
s=n.split('-')
m=sum(map(int,s[0].split('+')))
for i in s[1:]:
    m-=sum(map(int,i.split('+')))
print(m)
# expression = input()

# parts = expression.split('-')

# min_value = sum(map(int, parts[0].split('+')))

# for part in parts[1:]:
#     min_value -= sum(map(int, part.split('+')))

# print(min_value)
