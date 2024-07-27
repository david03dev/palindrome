def is_palindrome(s):
    # Remove any whitespace and convert to lower case for uniformity
    s = s.strip().lower()
    
    # Check if the string is equal to its reverse
    if s == s[::-1]:
        return 1
    else:
        return 0

# Input from the user
s = input().strip()

# Print the result
print(is_palindrome(s))
