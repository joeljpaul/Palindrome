def palindrome(str):
    # Write code here and return True if it is a palindrome
    reverse_str = reversed(str)
    if list(str) == list(reverse_str):
        return True
    return False

if palindrome("malayalam"):
    print("It is a palindrome")
else:
    print("It is not a palindrome")
