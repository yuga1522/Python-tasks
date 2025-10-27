# Data structure to store student records
students = []

def add_student():
    name = input("Enter student name: ")
    subjects = input("Enter subjects separated by commas: ").split(',')
    marks = {}
    for subject in subjects:
        score = float(input(f"Enter marks for {subject.strip()}: "))
        marks[subject.strip()] = score
    student = {
        'name': name,
        'subjects': tuple(subjects),
        'marks': marks
    }
    students.append(student)
    print("Student added successfully!\n")

def view_students():
    if not students:
        print("No student records found.\n")
    else:
        print("\n=== Student Records ===")
        for student in students:
            print(f"Name: {student['name']}")
            for subject in student['subjects']:
                print(f"  {subject}: {student['marks'][subject]}")
            print()

def search_student():
    search_name = input("Enter student name to search: ")
    found = False
    for student in students:
        if student['name'].lower() == search_name.lower():
            print(f"\nStudent found: {student['name']}")
            for subject in student['subjects']:
                print(f"{subject}: {student['marks'][subject]}")
            found = True
            break
    if not found:
        print("Student not found.\n")

def unique_subjects():
    subject_set = set()
    for student in students:
        subject_set.update(student['subjects'])
    print(f"\nUnique subjects across all students: {subject_set}\n")

def average_marks():
    for student in students:
        total = sum(student['marks'].values())
        avg = total / len(student['marks'])
        print(f"{student['name']}'s average marks: {avg:.2f}")
    print()

def main():
    while True:
        print("=== Student Marks Organizer ===")
        print("1. Add Student")
        print("2. View Students")
        print("3. Search Student")
        print("4. Unique Subjects")
        print("5. Average Marks")
        print("6. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            add_student()
        elif choice == '2':
            view_students()
        elif choice == '3':
            search_student()
        elif choice == '4':
            unique_subjects()
        elif choice == '5':
            average_marks()
        elif choice == '6':
            print("Exiting the program. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.\n")

if __name__ == "__main__":
    main()
