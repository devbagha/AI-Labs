
def is_palindrome(input_str):
    input_str = input_str.lower()  # Convert to lowercase for case-insensitive comparison
    if len(input_str) <= 1:
        return True
    elif input_str[0] == input_str[-1]:
        return is_palindrome(input_str[1:-1])
    else:
        return False

# Example usage
result1 = is_palindrome('racecar')
print(result1)  

result2 = is_palindrome('hello')
print(result2)  	

