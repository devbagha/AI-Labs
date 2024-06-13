
import numpy as np

def replace_with_inverse_recursive(arr, row=0, col=0):
    if row == arr.shape[0]:
        return arr
    elif col == arr.shape[1]:
        return replace_with_inverse_recursive(arr, row + 1, 0)
    else:
        arr[row, col] = 1 / arr[row, col]
        return replace_with_inverse_recursive(arr, row, col + 1)

def replace_matrix_elements_with_inverse(matrix):
    modified_matrix = matrix.copy()
    return replace_with_inverse_recursive(modified_matrix)

original_matrix = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]], dtype=float)
print("Original Matrix:")
print(original_matrix)

modified_matrix = replace_matrix_elements_with_inverse(original_matrix)
print("\nModified Matrix (with elements replaced by their multiplicative inverses):")
print(modified_matrix)
