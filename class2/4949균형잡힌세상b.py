while True:
    s = input()
    if s == '.':
        break

    stack = []
    balanced = 'yes'
    for c in s:
        if c in '([':
            stack.append(c)
        elif c == ')':
            if not stack or stack[-1] != '(':
                balanced = 'no'
                break
            stack.pop()
        elif c == ']':
            if not stack or stack[-1] != '[':
                balanced = 'no'
                break
            stack.pop()

    if stack:
        balanced = 'no'

    print(balanced)