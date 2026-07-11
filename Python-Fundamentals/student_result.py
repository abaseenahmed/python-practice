#============================== Student Result Calculator ==============================
def student_result_calculator():
    # Get student details
    name = input("Enter student's name: ")
    roll_number = input("Enter roll number: ")
    
    # Get marks for subjects
    subjects = ['Mathematics', 'Science', 'English', 'History', 'Geography']
    marks = {}
    
    for subject in subjects:
        while True:
            try:
                mark = float(input(f"Enter marks obtained in {subject} (out of 100): "))
                if 0 <= mark <= 100:
                    marks[subject] = mark
                    break
                else:
                    print("Please enter a valid mark between 0 and 100.")
            except ValueError:
                print("Invalid input. Please enter a numeric value.")
    
    # Calculate total and percentage
    total_marks = sum(marks.values())
    percentage = (total_marks / (len(subjects) * 100)) * 100
    
    # Determine grade
    if percentage >= 90:
        grade = 'A+'
    elif percentage >= 80:
        grade = 'A'
    elif percentage >= 70:
        grade = 'B+'
    elif percentage >= 60:
        grade = 'B'
    elif percentage >= 50:
        grade = 'C'
    else:
        grade = 'F'
    
    # Display result
    print("\n============================== Student Result ==============================")
    print(f"Name: {name}")
    print(f"Roll Number: {roll_number}")
    print(f"Total Marks: {total_marks} / {len(subjects) * 100}")
    print(f"Percentage: {percentage:.2f}%")
    print(f"Grade: {grade}")
    print('--------------------------------------------------------')
    print("Subject-wise Marks:")
    for subject, mark in marks.items():
        print(f"{subject}: {mark} / 100")
    print("===========================================================================")

student_result_calculator()
