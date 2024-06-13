
def unique(lst):
    result = []
    for item in lst:
        if item not in result:
            result.append(item)
    return result
original_list = [1, 2, 2, 3, 4, 4, 5]
unique_list = unique(original_list)
print(unique_list)
