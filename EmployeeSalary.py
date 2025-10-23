# Employee Salary Analyzer

employees = {}

# Add employee with validation
def add_employee():
    name = input("Enter employee name: ").strip()
    if name.isdigit():
        print("❌ Invalid name: Cannot be a number.\n")
        return

    salary_input = input("Enter monthly salary: ").strip()
    try:
        salary = float(salary_input)
        employees[name] = salary
        print("✅ Employee added successfully!\n")
    except ValueError:
        print("❌ Invalid salary: Please enter a numeric value.\n")

# View all employees
def display_employees():
    if not employees:
        print("⚠️ No employee data available.\n")
    else:
        print("\n=== 🗂️ Employee Salary List ===")
        for name, salary in employees.items():
            print(f"{name}: ₹{salary:.2f}")
        print()

# Calculate average salary
def calculate_average_salary():
    if not employees:
        print("⚠️ No employee data available.\n")
        return None
    total = sum(employees.values())
    average = total / len(employees)
    print(f"📊 Average salary: ₹{average:.2f}\n")
    return average

# Find highest-paid employee
def highest_paid_employee():
    if not employees:
        print("⚠️ No employee data available.\n")
        return
    highest = max(employees.items(), key=lambda x: x[1])
    print(f"💰 Highest-paid employee: {highest[0]} with ₹{highest[1]:.2f}\n")

# List employees earning above average
def above_average_employees():
    average = calculate_average_salary()
    if average is None:
        return
    print("📈 Employees earning above average:")
    found = False
    for name, salary in employees.items():
        if salary > average:
            print(f"- {name}: ₹{salary:.2f}")
            found = True
    if not found:
        print("No employees earn above the average.\n")
    else:
        print()

# Edit employee name
def edit_employee_name():
    old_name = input("Enter the current employee name: ").strip()
    if old_name not in employees:
        print("❌ Employee not found.\n")
        return

    new_name = input("Enter the new employee name: ").strip()
    if new_name.isdigit():
        print("❌ Invalid name: Cannot be a number.\n")
        return

    employees[new_name] = employees.pop(old_name)
    print("✅ Employee name updated successfully!\n")

# Edit employee salary
def edit_employee_salary():
    name = input("Enter employee name to update salary: ").strip()
    if name not in employees:
        print("❌ Employee not found.\n")
        return

    salary_input = input("Enter new salary: ").strip()
    try:
        salary = float(salary_input)
        employees[name] = salary
        print("✅ Salary updated successfully!\n")
    except ValueError:
        print("❌ Invalid salary: Please enter a numeric value.\n")

# Apply salary hike by percentage
def apply_salary_hike():
    name = input("Enter employee name for salary hike: ").strip()
    if name not in employees:
        print("❌ Employee not found.\n")
        return

    hike_input = input("Enter hike percentage (e.g., 10 for 10%): ").strip()
    try:
        hike_percent = float(hike_input)
        current_salary = employees[name]
        new_salary = current_salary + (current_salary * hike_percent / 100)
        employees[name] = new_salary
        print(f"✅ Salary updated: {name} now earns ₹{new_salary:.2f} after {hike_percent}% hike.\n")
    except ValueError:
        print("❌ Invalid percentage: Please enter a numeric value.\n")

# Main menu
def main():
    while True:
        print("=== 🧮 Employee Salary Analyzer ===")
        print("1. Add Employee")
        print("2. View All Employees")
        print("3. Calculate Average Salary")
        print("4. Highest-Paid Employee")
        print("5. Employees Above Average Salary")
        print("6. Edit Employee Name")
        print("7. Edit Employee Salary")
        print("8. Apply Salary Hike")
        print("9. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            add_employee()
        elif choice == '2':
            display_employees()
        elif choice == '3':
            calculate_average_salary()
        elif choice == '4':
            highest_paid_employee()
        elif choice == '5':
            above_average_employees()
        elif choice == '6':
            edit_employee_name()
        elif choice == '7':
            edit_employee_salary()
        elif choice == '8':
            apply_salary_hike()
        elif choice == '9':
            print("👋 Exiting the program. Goodbye!")
            break
        else:
            print("❌ Invalid choice. Please try again.\n")

# Run the program
if __name__ == "__main__":
    main()
