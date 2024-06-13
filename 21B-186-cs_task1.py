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

