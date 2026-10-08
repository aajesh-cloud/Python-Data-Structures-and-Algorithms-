def reverse_string(s):
    chars = list(s)
    left = 0
    right = len(chars) - 1

    while left < right:
        chars[left], chars[right] = chars[right], chars[left]
        left += 1
        right -= 1

    return "".join(chars)


def is_palindrome(s):
    left = 0
    right = len(s) - 1

    while left < right:
        if s[left] != s[right]:
            return False
        left += 1
        right -= 1

    return True


word = "madam"
print("Reversed:", reverse_string(word))

check1 = "racecar"
check2 = "hello"
print(f"{check1} is palindrome:", is_palindrome(check1))
print(f"{check2} is palindrome:", is_palindrome(check2))