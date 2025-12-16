def is_palindrome(s):
    if len(s) <= 1:
        return True
    else:
        return is_palindrome(s[1:-1]) and s[0] == s[-1]