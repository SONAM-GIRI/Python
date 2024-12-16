import random
import string
from tabulate import tabulate  # For displaying data in table format

class StudentManagementSystem:
    def __init__(self):
        self.students = []
        self.programs = ["B.Tech", "BBA", "MCA"]
        self.streams = {
            "B.Tech": ["Computer Science", "Mechanical", "Electrical", "Civil"],
            "BBA": ["Finance", "Marketing", "HR"],
            "MCA": ["Regular"]
        }
        self.courses = {
            "B.Tech": ["Mathematics", "Physics", "Programming", "Data Structures"],
            "BBA": ["Accounting", "Economics", "Business Law"],
            "MCA": ["Advanced Programming", "Database", "Networking"]
        }

    def generate_unique_id(self):
        while True:
            student_id = random.randint(1000, 9999)
            if not any(student['id'] == student_id for student in self.students):
                return student_id

    def generate_enrollment_number(self):
        while True:
            enrollment = ''.join(random.choices(string.ascii_uppercase + string.digits, k=8))
            if not any(student['enrollment'] == enrollment for student in self.students):
                return enrollment

    def validate_email(self, email):
        return '@' in email and '.' in email and not any(student['email'] == email for student in self.students)

    def validate_phone(self, phone):
        return len(phone) == 10 and phone.isdigit()

    def add_student(self):
        print("\nAdding New Student")
        print("-" * 20)

        # Get student details with validation
        name = input("Enter student name: ").strip()
        if not name:
            print("Error: Name is required!")
            return

        email = input("Enter student email: ").strip()
        if not email:
            print("Error: Email is required!")
            return
        if not self.validate_email(email):
            print("Error: Invalid or duplicate email!")
            return

        phone = input("Enter student phone: ").strip()
        if not self.validate_phone(phone):
            print("Error: Invalid phone number!")
            return

        address = input("Enter student address: ").strip()
        if not address:
            print("Error: Address is required!")
            return

        # Program selection
        print("\nAvailable Programs:")
        for idx, prog in enumerate(self.programs, 1):
            print(f"{idx}. {prog}")
        
        try:
            prog_choice = int(input("Select program (enter number): "))
            if prog_choice < 1 or prog_choice > len(self.programs):
                print("Invalid program selection!")
                return
            program = self.programs[prog_choice-1]
        except ValueError:
            print("Invalid input!")
            return

        # Stream selection
        print("\nAvailable Streams for", program)
        streams = self.streams[program]
        for idx, stream in enumerate(streams, 1):
            print(f"{idx}. {stream}")
        
        try:
            stream_choice = int(input("Select stream (enter number): "))
            if stream_choice < 1 or stream_choice > len(streams):
                print("Invalid stream selection!")
                return
            stream = streams[stream_choice-1]
        except ValueError:
            print("Invalid input!")
            return

        # Create student record
        student = {
            'id': self.generate_unique_id(),
            'enrollment': self.generate_enrollment_number(),
            'name': name,
            'email': email,
            'phone': phone,
            'address': address,
            'program': program,
            'stream': stream,
            'courses': []
        }

        self.students.append(student)
        print(f"\nStudent added successfully! ID: {student['id']}")

    def update_student(self):
        student_id = input("Enter student ID to update: ")
        try:
            student_id = int(student_id)
            student = next((s for s in self.students if s['id'] == student_id), None)
            
            if student:
                print("\nCurrent Details:")
                self.display_student(student)
                
                # Update fields
                name = input("Enter new name (press enter to skip): ").strip()
                if name:
                    student['name'] = name

                email = input("Enter new email (press enter to skip): ").strip()
                if email:
                    if self.validate_email(email):
                        student['email'] = email
                    else:
                        print("Invalid or duplicate email!")
                        return

                phone = input("Enter new phone (press enter to skip): ").strip()
                if phone:
                    if self.validate_phone(phone):
                        student['phone'] = phone
                    else:
                        print("Invalid phone number!")
                        return

                print("Student updated successfully!")
            else:
                print("Student not found!")
        except ValueError:
            print("Invalid ID format!")

    def delete_student(self):
        student_id = input("Enter student ID to delete: ")
        try:
            student_id = int(student_id)
            student = next((s for s in self.students if s['id'] == student_id), None)
            
            if student:
                self.students.remove(student)
                print("Student deleted successfully!")
            else:
                print("Student not found!")
        except ValueError:
            print("Invalid ID format!")

    def assign_courses(self):
        student_id = input("Enter student ID: ")
        try:
            student_id = int(student_id)
            student = next((s for s in self.students if s['id'] == student_id), None)
            
            if student:
                available_courses = self.courses[student['program']]
                print("\nAvailable Courses:")
                for idx, course in enumerate(available_courses, 1):
                    print(f"{idx}. {course}")
                
                while True:
                    try:
                        choice = int(input("\nSelect course number (0 to finish): "))
                        if choice == 0:
                            break
                        if 1 <= choice <= len(available_courses):
                            course = available_courses[choice-1]
                            if course not in student['courses']:
                                student['courses'].append(course)
                                print(f"Course '{course}' added!")
                            else:
                                print("Course already assigned!")
                        else:
                            print("Invalid course number!")
                    except ValueError:
                        print("Invalid input!")
            else:
                print("Student not found!")
        except ValueError:
            print("Invalid ID format!")

    def display_student(self, student):
        headers = ['Field', 'Value']
        data = [
            ['ID', student['id']],
            ['Enrollment', student['enrollment']],
            ['Name', student['name']],
            ['Email', student['email']],
            ['Phone', student['phone']],
            ['Address', student['address']],
            ['Program', student['program']],
            ['Stream', student['stream']],
            ['Courses', ', '.join(student['courses']) if student['courses'] else 'None']
        ]
        print(tabulate(data, headers=headers, tablefmt='grid'))

    def display_all_students(self):
        if not self.students:
            print("No students found!")
            return
        
        headers = ['ID', 'Enrollment', 'Name', 'Email', 'Program', 'Stream']
        data = [[s['id'], s['enrollment'], s['name'], s['email'], s['program'], s['stream']] 
                for s in self.students]
        print(tabulate(data, headers=headers, tablefmt='grid'))

    def display_student_by_id(self):
        student_id = input("Enter student ID: ")
        try:
            student_id = int(student_id)
            student = next((s for s in self.students if s['id'] == student_id), None)
            
            if student:
                self.display_student(student)
            else:
                print("Student not found!")
        except ValueError:
            print("Invalid ID format!")

def main():
    sms = StudentManagementSystem()
    
    while True:
        print("\nStudent Management System")
        print("1. Add Student")
        print("2. Update Student")
        print("3. Delete Student")
        print("4. Display All Students")
        print("5. Display Student by ID")
        print("6. Assign Courses")
        print("7. Exit")
        
        choice = input("\nEnter your choice: ")
        
        if choice == '1':
            sms.add_student()
        elif choice == '2':
            sms.update_student()
        elif choice == '3':
            sms.delete_student()
        elif choice == '4':
            sms.display_all_students()
        elif choice == '5':
            sms.display_student_by_id()
        elif choice == '6':
            sms.assign_courses()
        elif choice == '7':
            print("Thank you for using Student Management System!")
            break
        else:
            print("Invalid choice! Please try again.")

if __name__ == "__main__":
    main()
