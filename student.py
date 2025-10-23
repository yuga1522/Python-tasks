# Student Marks Organizer

students = []

def add_student():
    name = input("Enter student name: ")
    raw_subjects = input("Enter subjects separated by commas: ").split(',')
    subjects = []

    for subject in raw_subjects:
        subject = subject.strip()
        if subject.isdigit():
            print(f"Invalid subject name '{subject}': Cannot be a number.")
            return
        subjects.append(subject)

    subjects = tuple(subjects)
    marks = {}
    for subject in subjects:
        score = float(input(f"Enter marks for {subject}: "))
        marks[subject] = score

    student = {'name': name, 'subjects': subjects, 'marks': marks}
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
            print()
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

def edit_subject_name():
    search_name = input("Enter student name to edit subject: ")
    for student in students:
        if student['name'].lower() == search_name.lower():
            print(f"Subjects for {student['name']}: {student['subjects']}")
            old_subject = input("Enter the subject name to edit: ").strip()
            if old_subject not in student['subjects']:
                print("Subject not found.\n")
                return
            new_subject = input("Enter new subject name: ").strip()
            if new_subject.isdigit():
                print("Invalid subject name: Cannot be a number.\n")
                return

            # Update subjects tuple
            subjects_list = list(student['subjects'])
            index = subjects_list.index(old_subject)
            subjects_list[index] = new_subject
            student['subjects'] = tuple(subjects_list)

            # Update marks dictionary
            student['marks'][new_subject] = student['marks'].pop(old_subject)

            print("Subject name updated successfully!\n")
            return
    print("Student not found.\n")

def edit_marks():
    search_name = input("Enter student name to edit marks: ")
    for student in students:
        if student['name'].lower() == search_name.lower():
            print(f"Subjects for {student['name']}: {student['subjects']}")
            subject = input("Enter the subject name to update marks: ").strip()
            if subject not in student['marks']:
                print("Subject not found.\n")
                return
            new_score = float(input(f"Enter new marks for {subject}: "))
            student['marks'][subject] = new_score
            print("Marks updated successfully!\n")
            return
    print("Student not found.\n")

def main():
    while True:
        print("=== Student Marks Organizer ===")
        print("1. Add Student")
        print("2. View Students")
        print("3. Search Student")
        print("4. Unique Subjects")
        print("5. Average Marks")
        print("6. Edit Subject Name")
        print("7. Edit Marks")
        print("8. Exit")
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
            edit_subject_name()
        elif choice == '7':
            edit_marks()
        elif choice == '8':
            print("Exiting the program. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.\n")

if __name__ == "__main__":
    main()
