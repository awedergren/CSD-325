# Amanda Wedergren
# April 17, 2025
# Module 8.2 Assignment

import json

# Define the Student class.
class Student:
    def __init__(self, L_Name, F_Name, Student_ID, Email):
        self.F_Name = F_Name
        self.L_Name = L_Name
        self.Student_ID = Student_ID
        self.Email = Email

    def __repr__(self):
        return f'{self.L_Name}, {self.F_Name}: ID = {self.Student_ID}, Email = {self.Email})'

# Function to load students from a JSON file.
def load_students_from_json(file_path):
    with open(file_path, 'r') as file:
        data = json.load(file)
        return [Student(**student) for student in data]

# Function to print the student list.
def print_student_list(students, message):
    print(message)
    for student in students:
        print(student)

# Function to print successful append message.
def print_success_message(message):
    print(message)

# Function to save students to a JSON file.
def save_students_to_json(file_path, students):
    with open(file_path, 'w') as file:
        json.dump([student.__dict__ for student in students], file, indent=4)

# Main program.
if __name__ == "__main__":
    # Load the original student list from JSON file.
    file_path = 'student.json'
    students = load_students_from_json(file_path)

    # Print the original student list.
    print_student_list(students, "This is the original student list:")

    # Add a new student to the list.
    new_student = Student(L_Name="Wedergren", F_Name="Amanda", Student_ID="24528", Email="awedergren@example.com")
    students.append(new_student)

    # Print the updated student list.
    print_student_list(students, "This is the updated student list:")

    # Save the updated student list back to the JSON file.
    save_students_to_json(file_path, students)

    # Print the updated student list.
    print_success_message("File has been appended successfully.")