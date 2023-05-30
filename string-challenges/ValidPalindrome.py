def isPalindrome(s):
    # Convert to lowercase and remove non-alphanumeric characters
    s = ''.join(ch.lower() for ch in s if ch.isalnum())
    
    # Check if the modified string is equal to its reverse
    return s == s[::-1]
    
# Test the function
s = "A man, a plan, a canal: Panama"
print(isPalindrome(s))  # Output: True
