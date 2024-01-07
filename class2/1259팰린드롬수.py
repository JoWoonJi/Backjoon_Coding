while True:
    palindrome = input()
    if palindrome == "0":
        break
    if palindrome == ''.join(reversed(palindrome)):
        print("yes")
    else:
        print("no")
    