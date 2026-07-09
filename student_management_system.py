import json
import os
from datetime import datetime
import getpass
import hashlib

class StudentManagementSystem:
    DATA_FILE = "students.json"  # Class constant for file name
    
    def __init__(self):
        self.students = []
        self.student_id_counter = 1001
        self.current_user = None
        
        # Predefined credentials with hashed passwords
        self.users = {
            "admin": hashlib.sha256("admin123".encode()).hexdigest(),
            "teacher": hashlib.sha256("teacher123".encode()).hexdigest(),
            "student": hashlib.sha256("student123".encode()).hexdigest()
        }
    
    def print_header(self, title):
        """Helper function to print formatted headers"""
        print("\n" + "="*50)
        print(title.center(50))
        print("="*50)
    
    def validate_name(self, name, field_name="Name"):
        """Validate name input"""
        while True:
            name = input(f"Enter {field_name}: ").strip()
            
            if not name:
                print(f"❌ {field_name} cannot be empty")
                continue
            
            # Check if name contains only letters, spaces, dots, and hyphens
            if not all(c.isalpha() or c in " .'-" for c in name):
                print(f"❌ Enter a valid {field_name} (letters, spaces, dots, hyphens only)")
                continue
            
            return name
    
    def validate_age(self):
        """Validate age input"""
        while True:
            try:
                age = int(input("Enter Age: "))
                if 1 <= age <= 120:
                    return age
                else:
                    print("❌ Age must be between 1 and 120")
            except ValueError:
                print("❌ Invalid age! Please enter a number")
    
    def validate_roll_number(self):
        """Validate roll number input"""
        while True:
            try:
                roll = int(input("Enter Roll Number: "))
                if roll <= 0:
                    print("❌ Roll number must be positive")
                    continue
                # Check if roll number already exists
                if any(s['roll'] == roll for s in self.students):
                    print("❌ Roll number already exists! Please enter a unique roll number")
                    continue
                return roll
            except ValueError:
                print("❌ Invalid roll number! Please enter a number")
    
    def validate_semester(self):
        """Validate semester input"""
        while True:
            try:
                semester = int(input("Enter Semester (1-8): "))
                if 1 <= semester <= 8:
                    return semester
                else:
                    print("❌ Semester must be between 1 and 8")
            except ValueError:
                print("❌ Invalid semester! Please enter a number")
    
    def validate_mark(self, subject_num):
        """Validate individual mark input"""
        while True:
            try:
                mark = float(input(f"Subject {subject_num}: "))
                if 0 <= mark <= 100:
                    return mark
                else:
                    print("❌ Mark must be between 0 and 100")
            except ValueError:
                print("❌ Please enter a valid number")
    
    def validate_marks(self):
        """Get and validate all marks"""
        print("\nEnter Marks for 5 Subjects (0-100):")
        marks = []
        for i in range(1, 6):
            marks.append(self.validate_mark(i))
        return marks
    
    def hash_password(self, password):
        """Hash password for storage"""
        return hashlib.sha256(password.encode()).hexdigest()
    
    def login_system(self):
        """Bonus Challenge: Login System"""
        self.print_header("LOGIN SYSTEM")
        
        attempts = 3
        while attempts > 0:
            username = input("Username: ")
            password = getpass.getpass("Password: ")
            hashed_password = self.hash_password(password)
            
            if username in self.users and self.users[username] == hashed_password:
                self.current_user = username
                print(f"\n✅ Login Successful! Welcome {username}!")
                return True
            else:
                attempts -= 1
                print(f"❌ Invalid credentials! {attempts} attempts remaining")
        
        print("❌ Too many failed attempts. Exiting...")
        return False
    
    def generate_student_id(self):
        """Bonus Challenge: Generate Student ID automatically"""
        student_id = f"STU-{self.student_id_counter}"
        self.student_id_counter += 1
        return student_id
    
    def add_student(self):
        """Task 1: Add Student"""
        self.print_header("ADD STUDENT")
        
        try:
            student = {}
            
            # Generate student ID automatically
            student['student_id'] = self.generate_student_id()
            
            # Get validated student information
            student['name'] = self.validate_name("Name")
            student['roll'] = self.validate_roll_number()
            student['age'] = self.validate_age()
            student['department'] = self.validate_name("Department")
            student['semester'] = self.validate_semester()
            student['marks'] = self.validate_marks()
            
            # Add admission date and time
            now = datetime.now()
            student['admission_date'] = now.strftime("%Y-%m-%d")
            student['admission_time'] = now.strftime("%H:%M:%S")
            student['admission_datetime'] = now.strftime("%Y-%m-%d %H:%M:%S")
            
            # Add to students list and automatically save
            self.students.append(student)
            self.save_data()
            
            print(f"\n✅ Student added successfully! Student ID: {student['student_id']}")
            print(f"   Admission Date: {student['admission_date']}")
            print(f"   Admission Time: {student['admission_time']}")
            
        except Exception as e:
            print(f"❌ Error adding student: {e}")
    
    def display_student(self, student, index=None):
        """Display a single student's information"""
        if index is not None:
            self.print_header(f"Student #{index + 1}")
        
        print(f"Student ID  : {student.get('student_id', 'N/A')}")
        print(f"Roll No     : {student['roll']}")
        print(f"Name        : {student['name']}")
        print(f"Age         : {student['age']}")
        print(f"Department  : {student['department']}")
        print(f"Semester    : {student['semester']}")
        print(f"Admission   : {student.get('admission_datetime', 'N/A')}")
        
        print("Marks       : ", end="")
        marks = student['marks']
        for i, mark in enumerate(marks, 1):
            print(f"S{i}: {mark:.1f}", end="  " if i < len(marks) else "")
        print()
        
        # Calculate and display result
        result = self.calculate_student_result(student)
        print(f"Total Marks : {result['total']:.1f}")
        print(f"Percentage  : {result['percentage']:.1f}%")
        print(f"Grade       : {result['grade']}")
        print(f"Status      : {result['status']}")
        print("="*50)
    
    def view_students(self):
        """Task 2: View Students"""
        self.print_header("VIEW STUDENTS")
        
        if not self.students:
            print("❌ No students found!")
            return
        
        # Bonus Challenge: Sort by percentage (highest to lowest)
        sorted_students = sorted(
            self.students, 
            key=lambda s: self.calculate_student_result(s)['percentage'], 
            reverse=True
        )
        
        print(f"\nTotal Students: {len(sorted_students)}")
        print("Sorting by: Percentage (Highest to Lowest)\n")
        
        for i, student in enumerate(sorted_students):
            self.display_student(student, i)
    
    def search_student(self):
        """Task 3: Search Student with bonus search options"""
        self.print_header("SEARCH STUDENT")
        
        print("\nSearch by:")
        print("1. Roll Number")
        print("2. Name")
        print("3. Department")
        
        choice = input("Enter choice (1-3): ").strip()
        
        results = []
        
        try:
            if choice == '1':
                roll = int(input("Enter Roll Number: "))
                results = [s for s in self.students if s['roll'] == roll]
            elif choice == '2':
                name = input("Enter Name: ").strip().lower()
                results = [s for s in self.students if name in s['name'].lower()]
            elif choice == '3':
                dept = input("Enter Department: ").strip().lower()
                results = [s for s in self.students if dept in s['department'].lower()]
            else:
                print("❌ Invalid choice!")
                return
            
            if results:
                print(f"\nFound {len(results)} student(s):")
                for student in results:
                    self.display_student(student)
            else:
                print("❌ Student Not Found!")
                
        except ValueError:
            print("❌ Invalid input! Please enter a valid number")
        except Exception as e:
            print(f"❌ Error searching student: {e}")
    
    def get_confirm_input(self, message="Are you sure? (y/n): "):
        """Get confirmation input"""
        while True:
            confirm = input(message).strip().lower()
            if confirm in ("y", "n"):
                return confirm == "y"
            print("❌ Please enter 'y' or 'n'")
    
    def update_student(self):
        """Task 4: Update Student"""
        self.print_header("UPDATE STUDENT")
        
        try:
            roll = int(input("Enter Roll Number to update: "))
            
            # Find student by roll number
            for student in self.students:
                if student['roll'] == roll:
                    print(f"\nUpdating student: {student['name']}")
                    print("Leave blank to keep current value")
                    
                    # Update fields with validation
                    name = input(f"Name ({student['name']}): ").strip()
                    if name:
                        # Validate name
                        if not all(c.isalpha() or c in " .'-" for c in name):
                            print("❌ Invalid name format!")
                            return
                        student['name'] = name
                    
                    age = input(f"Age ({student['age']}): ").strip()
                    if age:
                        try:
                            age_val = int(age)
                            if not (1 <= age_val <= 120):
                                print("❌ Age must be between 1 and 120")
                                return
                            student['age'] = age_val
                        except ValueError:
                            print("❌ Invalid age! Please enter a number")
                            return
                    
                    dept = input(f"Department ({student['department']}): ").strip()
                    if dept:
                        if not all(c.isalpha() or c in " .'-" for c in dept):
                            print("❌ Invalid department format!")
                            return
                        student['department'] = dept
                    
                    semester = input(f"Semester ({student['semester']}): ").strip()
                    if semester:
                        try:
                            semester_val = int(semester)
                            if not (1 <= semester_val <= 8):
                                print("❌ Semester must be between 1 and 8")
                                return
                            student['semester'] = semester_val
                        except ValueError:
                            print("❌ Invalid semester! Please enter a number")
                            return
                    
                    update_marks = input("Update marks? (y/n): ").strip().lower()
                    if update_marks == 'y':
                        print("Enter new marks for 5 subjects (0-100):")
                        new_marks = []
                        for i in range(1, 6):
                            new_marks.append(self.validate_mark(i))
                        student['marks'] = new_marks
                    
                    # Automatically save after update
                    self.save_data()
                    
                    print("\n✅ Student updated successfully!")
                    self.display_student(student)
                    return
            
            print("❌ Student Not Found!")
            
        except ValueError:
            print("❌ Invalid roll number! Please enter a number")
        except Exception as e:
            print(f"❌ Error updating student: {e}")
    
    def delete_student(self):
        """Task 5: Delete Student"""
        self.print_header("DELETE STUDENT")
        
        try:
            roll = int(input("Enter Roll Number to delete: "))
            
            # Find student by roll number
            for i, student in enumerate(self.students):
                if student['roll'] == roll:
                    print(f"\nStudent to delete: {student['name']}")
                    
                    if self.get_confirm_input():
                        del self.students[i]
                        # Automatically save after deletion
                        self.save_data()
                        print("✅ Student Deleted Successfully!")
                    else:
                        print("❌ Deletion cancelled!")
                    return
            
            print("❌ Student Not Found!")
            
        except ValueError:
            print("❌ Invalid roll number! Please enter a number")
        except Exception as e:
            print(f"❌ Error deleting student: {e}")
    
    def calculate_student_result(self, student):
        """Helper function to calculate result for a student"""
        try:
            total = sum(student['marks'])
            percentage = (total / 500) * 100
            
            # Determine grade
            if percentage >= 90:
                grade = "A+"
                status = "Excellent"
            elif percentage >= 80:
                grade = "A"
                status = "Very Good"
            elif percentage >= 70:
                grade = "B"
                status = "Good"
            elif percentage >= 60:
                grade = "C"
                status = "Satisfactory"
            elif percentage >= 50:
                grade = "D"
                status = "Pass"
            else:
                grade = "F"
                status = "Fail"
            
            return {
                'total': total,
                'percentage': percentage,
                'grade': grade,
                'status': status
            }
        except (TypeError, ZeroDivisionError):
            return {
                'total': 0,
                'percentage': 0,
                'grade': 'N/A',
                'status': 'Error'
            }
    
    def calculate_result(self):
        """Task 6: Calculate Result"""
        self.print_header("CALCULATE RESULT")
        
        if not self.students:
            print("❌ No students found!")
            return
        
        try:
            roll = int(input("Enter Roll Number: "))
            
            # Find student by roll number
            for student in self.students:
                if student['roll'] == roll:
                    result = self.calculate_student_result(student)
                    
                    self.print_header(f"Result for: {student['name']} (ID: {student.get('student_id', 'N/A')})")
                    print(f"Roll Number   : {student['roll']}")
                    print(f"Department    : {student['department']}")
                    print(f"Semester      : {student['semester']}")
                    print(f"Total Marks   : {result['total']:.1f}/500")
                    print(f"Percentage    : {result['percentage']:.1f}%")
                    print(f"Grade         : {result['grade']}")
                    print(f"Status        : {result['status']}")
                    print("="*50)
                    return
            
            print("❌ Student Not Found!")
            
        except ValueError:
            print("❌ Invalid roll number! Please enter a number")
        except Exception as e:
            print(f"❌ Error calculating result: {e}")
    
    def save_data(self):
        """Task 7: Save Data to JSON"""
        try:
            with open(self.DATA_FILE, 'w', encoding='utf-8') as file:
                json.dump(
                    self.students, 
                    file, 
                    indent=4, 
                    ensure_ascii=False  # Allows Unicode characters like Arabic
                )
            # Don't print success message here to avoid spam during auto-save
        except (IOError, PermissionError) as e:
            print(f"❌ Error saving data: {e}")
        except Exception as e:
            print(f"❌ Unexpected error while saving: {e}")
    
    def load_data(self):
        """Task 8: Load Data from JSON"""
        try:
            if not os.path.exists(self.DATA_FILE):
                return
            
            with open(self.DATA_FILE, 'r', encoding='utf-8') as file:
                loaded_data = json.load(file)
            
            # Update student_id_counter if there are existing students
            if loaded_data:
                max_id = 1000  # Start from 1000
                for student in loaded_data:
                    if 'student_id' in student:
                        try:
                            id_num = int(student['student_id'].split('-')[1])
                            max_id = max(max_id, id_num)
                        except (ValueError, IndexError):
                            # Skip if student_id format is invalid
                            pass
                
                if max_id > 1000:
                    self.student_id_counter = max_id + 1
                
                self.students = loaded_data
                print(f"✅ Data loaded successfully from {self.DATA_FILE}!")
                print(f"   Total students loaded: {len(self.students)}")
            
        except FileNotFoundError:
            print(f"ℹ️ No data file found. Starting fresh.")
        except json.JSONDecodeError:
            print(f"❌ Error: Invalid JSON format in {self.DATA_FILE}")
        except (IOError, PermissionError) as e:
            print(f"❌ Error accessing file: {e}")
        except Exception as e:
            print(f"❌ Unexpected error while loading: {e}")
    
    def display_menu(self):
        """Display main menu"""
        self.print_header("STUDENT MANAGEMENT SYSTEM")
        print("1. Add Student")
        print("2. View Students")
        print("3. Search Student")
        print("4. Update Student")
        print("5. Delete Student")
        print("6. Calculate Result")
        print("7. Save Data (Manual)")
        print("8. Load Data")
        print("9. Exit")
        print("="*50)
        print(f"Logged in as: {self.current_user}")
        print(f"Total Students: {len(self.students)}")
        print("="*50)
    
    def run(self):
        """Main program loop"""
        # Login system
        if not self.login_system():
            return
        
        # Load existing data if available
        self.load_data()
        
        while True:
            self.display_menu()
            
            try:
                choice = input("Enter Choice (1-9): ").strip()
                
                if choice == '1':
                    self.add_student()
                elif choice == '2':
                    self.view_students()
                elif choice == '3':
                    self.search_student()
                elif choice == '4':
                    self.update_student()
                elif choice == '5':
                    self.delete_student()
                elif choice == '6':
                    self.calculate_result()
                elif choice == '7':
                    self.save_data()
                    print(f"✅ Data saved successfully to {self.DATA_FILE}!")
                    print(f"   Total students saved: {len(self.students)}")
                elif choice == '8':
                    self.load_data()
                elif choice == '9':
                    self.print_header("Thank you for using the system!")
                    print("Goodbye!")
                    break
                else:
                    print("❌ Invalid choice! Please enter a number between 1 and 9")
                
                input("\nPress Enter to continue...")
                
            except KeyboardInterrupt:
                print("\n\nExiting program...")
                break
            except Exception as e:
                print(f"❌ Unexpected error: {e}")
                input("\nPress Enter to continue...")

# Main program
if __name__ == "__main__":
    system = StudentManagementSystem()
    system.run()