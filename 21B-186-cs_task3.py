
def minmax(data):
    if not data:
        return None  
    min_val = max_val = data[0]
    for num in data[1:]:
        if num < min_val:
            min_val = num
        elif num > max_val:
            max_val = num

    return min_val, max_val
sequence = [3, 7, 2, 9, 1, 5]
result = minmax(sequence)
print(result)
