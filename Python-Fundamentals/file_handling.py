#======================================== File Handling ===================================#
print('_________________________ This is File Handling Topic ______________________________')

#--------------------------------- Question No. 1 -----------------------------------------#
file = open('document.txt', 'r')
data = file.read()
print(data)
file.close()

#--------------------------------- Question No. 2 -----------------------------------------#
file = open('document.txt', 'r')
students = 0
for line in file:
    students += 1

print(f'The Total Number of Students in The file  Are: {students + 1}')
file.close()

#--------------------------------- Question No. 3 -----------------------------------------#
file = open('marks.txt', 'r') 
for line in file:
    print(line)

#--------------------------------- Question No. 4 -----------------------------------------#
file = open('marks.txt', 'r') 
line = file.readlines()
for i in range(len(line)):
    print(f'{i+1}. {line[i]}', end=' ')
file.close()
#--------------------------------- Question No. 5 -----------------------------------------#
file = open("message.txt", "w")
file.write("Welcome to Python File Handling!")
file.close()

#--------------------------------- Question No. 6 -----------------------------------------#
file = open("names.txt", "a")
name = ""
for i in range(3):
    name = input("\n Enter Name: ")
    file.write(f" {name} \n")
file.close()

#--------------------------------- Question No. 7 -----------------------------------------#
file = open("profile.txt", "a")
name = input("Enter Name: ")
file.write(f"Name: {name}")
age = str(input("Enter Your Age: "))
file.write(f"Age: {age}")
city = input("Enter Your City: ")
file.write(f"City: {city}")
file.close()

#--------------------------------- Question No. 8 -----------------------------------------#
with open("languages.txt", "a") as file:
    print("Enter Any Five Programming Languages.\n")
    for i in range(5):
        lang = input(f"{i+1}. Enter Language: ")
        file.write(f"{str(i)}. {lang} \n")



#--------------------------------- Question No. 9 -----------------------------------------#
with open("students.txt", "a") as student_record:
    for i in range(5):
        name = input("Enter Student Name: ")
        roll_number = input("Roll Number: ")
        marks = str(input("Marks: "))
        student_record.write(f"{str(i+1)}. Name: {name} - Roll_Number: {roll_number} - Marks: {marks}. \n")



#--------------------------------- Question No. 10 -----------------------------------------#
with open("numbers.txt", "w") as numbers_file:
    for i in range(1, 21):
        numbers_file.write(f"{str(i)} \n")

#--------------------------------- Question No. 10 -----------------------------------------#


with open("notes.txt", "a") as notes_file:

    print("======= Daily Notes App =======")
    print("1. Add Note")
    print("2. Exit")

    choice = int(input("Enter Choice: "))

    if choice == 1:
        note = input("Enter Note: ")
        notes_file.write(note + "\n")
        print("Note saved successfully.")

    elif choice == 2:
        print("Goodbye!")

    else:
        print("Invalid Choice")



employee_file = open("employee.txt", "w")
team = ["Ali - Manager", "Ahmed - Developer", "Ayesha - Designer"]
for i in range(len(team)):
    employee_file.write(f"{team[i]} \n")
employee_file.close()

read_emp = open("employee.txt", "r")
line = read_emp.readlines()
for i in range(len(line)):
    if line[i].startswith("Ahmed"):
        line[i] = "Ahmed - Senior Developer \n"
read_emp.close()

update_emp = open("employee.txt", "w")
update_emp.writelines(line)


# ========================= Delete Student Record =========================

# Step 1: Create the file (Only for testing)
with open("students.txt", "w") as students_info:
    students = [
        "Ali - 85",
        "Ahmed - 90",
        "Ayesha - 88",
        "Bilal - 95",
        "Fatima - 92"
    ]

    for student in students:
        students_info.write(student + "\n")


# Step 2: Read all student records
with open("students.txt", "r") as student_records:
    records = student_records.readlines()


# Step 3: Ask the user which student to delete
student_to_delete = input("Enter the student name to delete: ")

new_records = []
found = False


# Step 4: Remove the selected student
for record in records:
    if record.startswith(student_to_delete):
        found = True
    else:
        new_records.append(record)


# Step 5: Save the updated records
with open("students.txt", "w") as student_records:
    student_records.writelines(new_records)


# Step 6: Display the result
if found:
    print("Student deleted successfully.")
else:
    print("Student not found.")

