while True:
    palindrome = input()
    if palindrome == "0":
        break
    if palindrome == ''.join(reversed(palindrome)):  # 또는 palindrome[::-1] // reversed라는 함수가 있길래 사용해 보았는데 쉬운 방법이 있었다.
        print("yes")
    else:
        print("no")
