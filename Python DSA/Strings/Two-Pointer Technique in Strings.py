def is_valid_palindrome(s):
    left = 0
    right = len(s) - 1

    while left < right:
        if not s[left].isalnum():
            left += 1
            continue
        if not s[right].isalnum():
            right -= 1
            continue

        if s[left].lower() != s[right].lower():
            return False

        left += 1
        right -= 1

    return True


phrase = "A man, a plan, a canal: Panama"
print("Is valid palindrome:", is_valid_palindrome(phrase))

not_palindrome = "This is not one"
print("Is valid palindrome:", is_valid_palindrome(not_palindrome))