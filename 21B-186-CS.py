#!/usr/bin/env python
# coding: utf-8

# In[1]:


class StudentDatabase:
    def __init__(self):
        self.students = []

    def add_student(self, name, age, grade):
        student = {'name': name, 'age': age, 'grade': grade}
        self.students.append(student)

    def display_students(self):
        for student in self.students:
            print(f"Name: {student['name']}, Age: {student['age']}, Grade: {student['grade']}")

    def find_student(self, name):
        for student in self.students:
            if student['name'] == name:
                return student
        return None

    def remove_student(self, name):
        for student in self.students:
            if student['name'] == name:
                self.students.remove(student)
                print(f"{name} removed from the database.")
                return
        print(f"{name} not found in the database.")


# Usage of the StudentDatabase class
student_db = StudentDatabase()

# Adding some initial students
student_db.add_student("Ali", 11, 'A')
student_db.add_student("Khalid", 19, 'C')
student_db.add_student("Saad", 20, 'A+')

# Displaying all students
print("List of the students:")
student_db.display_students()

# Finding a student
print("\nFinding a student:")
student_to_find = student_db.find_student("Umair")
if student_to_find:
    print(f"Found {student_to_find['name']} in the database.")
else:
    print("The student doesnot exist in th.")

# Removing a student
print("\nRemoving a student:")
student_db.remove_student("Charlie")

# Displaying all students after removal
print("\nAll students after removal:")
student_db.display_students()


# In[2]:


def recursive_reverse(input_str):
    if len(input_str) <= 1:
        return input_str
    else:
        return recursive_reverse(input_str[1:]) + input_str[0]
result = recursive_reverse('example')
print(result)


# In[3]:


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


# In[6]:


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


# In[4]:


def unique(lst):
    result = []
    for item in lst:
        if item not in result:
            result.append(item)
    return result
original_list = [1, 2, 2, 3, 4, 4, 5]
unique_list = unique(original_list)
print(unique_list)


# In[5]:


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

