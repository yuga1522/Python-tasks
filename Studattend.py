# Step 1: Define the Student class
class Student:
    def __init__(self, name, roll_number):
        # Step 2: Initialize student with name, roll number, attendance list, and marks dictionary
        self.name = name
        self.roll_number = roll_number
        self.attendance = []
        self.marks = {}

    # Step 3: Mark attendance for a specific date
    def mark_attendance(self, date):
        self.attendance.append(date)

    # Step 4: Enter all 5 subjects and marks at once with validation
    def enter_multiple_subjects(self):
        print(f"\nEntering marks for {self.name} (Roll No: {self.roll_number})")
        subjects_entered = 0
        while subjects_entered < 5:
            subject = input(f"Enter subject {subjects_entered + 1} name: ").strip()
            # Validate subject name
            if subject.isdigit():
                print("Error: Subject name cannot be a number.")
                continue
            if subject in self.marks:
                print("Error: Subject already entered.")
                continue
            try:
                score = float(input(f"Enter marks for {subject} (0–100): "))
                if score < 0 or score > 100:
                    print("Error: Marks must be between 0 and 100.")
                    continue
                self.marks[subject] = score
                subjects_entered += 1
            except ValueError:
                print("Error: Marks must be a numeric value.")
        print("All 5 subjects and marks recorded successfully.")

    # Step 5: Calculate average marks
    def average_marks(self):
        if self.marks:
            return sum(self.marks.values()) / len(self.marks)
        return 0

    # Step 6: Calculate attendance percentage
    def attendance_percentage(self, total_days):
        if total_days == 0:
            return 0
        return (len(self.attendance) / total_days) * 100

    # Step 7: Determine grade based on average marks
    def grade(self):
        avg = self.average_marks()
        if avg >= 90:
            return "A"
        elif avg >= 75:
            return "B"
        elif avg >= 50:
            return "C"
        else:
            return "D"

    # Step 8: Display individual performance summary
    def performance_summary(self):
        print(f"\n===== Performance Summary for {self.name} (Roll No: {self.roll_number}) =====")
        print(f"Total Attendance Days: {len(self.attendance)}")
        print("Marks:")
        for subject, score in self.marks.items():
            print(f"  {subject}: {score}")
        print(f"Average Marks: {self.average_marks():.2f}")
        print("Grade:", self.grade())

# Step 9: Main application logic
def main():
    students = {}         # Dictionary to store students by roll number
    all_dates = set()     # Set to track all unique attendance dates

    while True:
        # Step 10: Display main menu
        print("\n===== Smart Student Attendance & Performance Tracker =====")
        print("1. Add New Student")
        print("2. Mark Attendance")
        print("3. Enter All 5 Subjects & Marks")
        print("4. View Attendance Report")
        print("5. Generate Individual Performance Summary")
        print("6. Generate Overall Class Summary")
        print("7. Exit")
        choice = input("Select an option (1–7): ")

        # Step 11: Add a new student
        if choice == '1':
            name = input("Enter student name: ").strip()
            roll = input("Enter roll number: ").strip()
            if roll in students:
                print("Student already exists.")
            else:
                students[roll] = Student(name, roll)
                print(f"Student {name} added successfully.")

        # Step 12: Mark attendance for multiple students
        elif choice == '2':
            date = input("Enter date (YYYY-MM-DD): ").strip()
            all_dates.add(date)
            print("Mark attendance for the following students:")
            for roll, student in students.items():
                response = input(f"Is {student.name} (Roll No: {roll}) present? (y/n): ").lower()
                if response == 'y':
                    student.mark_attendance(date)
            print("Attendance updated.")

        # Step 13: Enter all 5 subjects and marks
        elif choice == '3':
            name = input("Enter student name: ").strip()
            found = None
            for student in students.values():
                if student.name.lower() == name.lower():
                    found = student
                    break
            if found:
                if len(found.marks) >= 5:
                    print("This student already has 5 subjects recorded.")
                else:
                    found.enter_multiple_subjects()
            else:
                print("Student not found.")

        # Step 14: View attendance report
        elif choice == '4':
            roll = input("Enter roll number: ").strip()
            if roll in students:
                student = students[roll]
                print(f"\nAttendance Report for {student.name} (Roll No: {roll})")
                for date in student.attendance:
                    print(f"  - {date}")
                print(f"Total Days Present: {len(student.attendance)}")
            else:
                print("Student not found.")

        # Step 15: Generate individual performance summary
        elif choice == '5':
            roll = input("Enter roll number: ").strip()
            if roll in students:
                students[roll].performance_summary()
            else:
                print("Student not found.")

        # Step 16: Generate overall class summary
        elif choice == '6':
            total_days = len(all_dates)
            if not students:
                print("No students found.")
                continue

            print("\n----------------------------------------------------------")
            print(f"{'Name':<14}{'Roll No':<10}{'Attendance%':<14}{'Marks':<8}{'Grade'}")
            print("----------------------------------------------------------")

            total_attendance_percentages = 0
            for student in students.values():
                attendance_pct = student.attendance_percentage(total_days)
                avg_marks = student.average_marks()
                grade = student.grade()
                total_attendance_percentages += attendance_pct
                print(f"{student.name:<14}{student.roll_number:<10}{attendance_pct:>6.1f}%{'':<6}{avg_marks:>6.0f}{'':<3}{grade}")

            class_avg = total_attendance_percentages / len(students)
            print("----------------------------------------------------------")
            print(f"Class Average: {class_avg:.1f}%")

        # Step 17: Exit the program
        elif choice == '7':
            print("Exiting the tracker. Goodbye!")
            break

        # Step 18: Handle invalid input
        else:
            print("Invalid option. Please try again.")

# Step 19: Run the application
if __name__ == "__main__":
    main()