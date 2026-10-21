
# class Student:
#     def __init__(self, name, age, course):
#         self.name = name
#         self.age = age
#         self.course = course

#     def display_details(self):
#         print("Name:", self.name)
#         print("Age:", self.age)
#         print("Course:", self.course)


# class StudentManagementSystem:
#     def __init__(self):
#         self.students = []

#     def add_student(self):
#         name = input("Enter student name: ")
#         age = int(input("Enter student age: "))
#         course = input("Enter student course: ")

#         student = Student(name, age, course)
#         self.students.append(student)

#         print("Student added successfully!")

#     def display_students(self):
#         if not self.students:
#             print("No students found.")
#             return

#         for student in self.students:
#             print("--------------------")
#             student.display_details()

#     def run(self):
#         while True:
#             print("\n--- Student Management System ---")
#             print("1. Add Student")
#             print("2. Display Students")
#             print("3. Exit")

#             choice = input("Choose an option: ")

#             if choice == "1":
#                 self.add_student()
#             elif choice == "2":
#                 self.display_students()
#             elif choice == "3":
#                 print("Thank you for using the system!")
#                 break
#             else:
#                 print("Invalid choice. Try again.")


# app = StudentManagementSystem()
# app.run()
