
def recursive_reverse(input_str):
    if len(input_str) <= 1:
        return input_str
    else:
        return recursive_reverse(input_str[1:]) + input_str[0]
result = recursive_reverse('example')
print(result)

