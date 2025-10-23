import json
import os

# Step 1: Define the file name to store expense data
DATA_FILE = "expenses.json"

# Step 2: Load existing data from file or initialize empty list
def load_data():
    if os.path.exists(DATA_FILE):
        with open(DATA_FILE, "r") as file:
            return json.load(file)
    else:
        return []

# Step 3: Save updated data back to the file
def save_data(data):
    with open(DATA_FILE, "w") as file:
        json.dump(data, file, indent=4)

# Step 4: Add income with numeric validation
def add_income(data):
    try:
        amount = float(input("Enter income amount: "))
        category = input("Enter income category: ").strip()
        if category.isdigit():
            print("❌ Invalid category: Cannot be a number.\n")
            return
        data.append({"type": "income", "amount": amount, "category": category})
        save_data(data)
        print("✅ Income added successfully!\n")
    except ValueError:
        print("❌ Invalid amount: Please enter a numeric value.\n")

# Step 5: Add expense with numeric validation
def add_expense(data):
    try:
        amount = float(input("Enter expense amount: "))
        category = input("Enter expense category: ").strip()
        if category.isdigit():
            print("❌ Invalid category: Cannot be a number.\n")
            return
        data.append({"type": "expense", "amount": amount, "category": category})
        save_data(data)
        print("✅ Expense added successfully!\n")
    except ValueError:
        print("❌ Invalid amount: Please enter a numeric value.\n")

# Step 6: View all income and expenses
def view_all(data):
    if not data:
        print("⚠️ No records found.\n")
        return
    print("\n=== All Transactions ===")
    for i, entry in enumerate(data):
        print(f"{i+1}. {entry['type'].capitalize()} - ₹{entry['amount']:.2f} - Category: {entry['category']}")
    print()

# Step 7: View total expenses only
def view_total_expense(data):
    total = sum(entry['amount'] for entry in data if entry['type'] == 'expense')
    print(f"💸 Total Expenses: ₹{total:.2f}\n")

# Step 8: View summary by category
def view_category_summary(data):
    summary = {}
    for entry in data:
        key = entry['category']
        summary[key] = summary.get(key, 0) + entry['amount']
    print("\n📊 Category Summary:")
    for category, total in summary.items():
        print(f"{category}: ₹{total:.2f}")
    print()

# Step 9: View income vs expense summary
def view_expense_summary(data):
    income = sum(entry['amount'] for entry in data if entry['type'] == 'income')
    expense = sum(entry['amount'] for entry in data if entry['type'] == 'expense')
    balance = income - expense
    print(f"\n💼 Income: ₹{income:.2f}")
    print(f"💸 Expense: ₹{expense:.2f}")
    print(f"🧾 Balance: ₹{balance:.2f}\n")

# Step 10: Edit a transaction (income/expense/category)
def edit_transaction(data):
    view_all(data)
    try:
        index = int(input("Enter transaction number to edit: ")) - 1
        if index < 0 or index >= len(data):
            print("❌ Invalid transaction number.\n")
            return

        entry = data[index]
        print(f"Editing: {entry['type'].capitalize()} - ₹{entry['amount']} - {entry['category']}")

        # Edit amount
        new_amount = input("Enter new amount (leave blank to keep current): ").strip()
        if new_amount:
            try:
                entry['amount'] = float(new_amount)
            except ValueError:
                print("❌ Invalid amount. Edit cancelled.\n")
                return

        # Edit category
        new_category = input("Enter new category (leave blank to keep current): ").strip()
        if new_category:
            if new_category.isdigit():
                print("❌ Invalid category. Edit cancelled.\n")
                return
            entry['category'] = new_category

        save_data(data)
        print("✅ Transaction updated successfully!\n")
    except ValueError:
        print("❌ Invalid input. Edit cancelled.\n")

# Step 11: Main menu loop
def main():
    data = load_data()
    while True:
        print("===== Expense Tracker =====")
        print("1. Add Income")
        print("2. Add Expense")
        print("3. View All Expenses")
        print("4. View Total Expense")
        print("5. View Category Summary")
        print("6. View Expenses Summary")
        print("7. Edit Transaction")
        print("8. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            add_income(data)
        elif choice == '2':
            add_expense(data)
        elif choice == '3':
            view_all(data)
        elif choice == '4':
            view_total_expense(data)
        elif choice == '5':
            view_category_summary(data)
        elif choice == '6':
            view_expense_summary(data)
        elif choice == '7':
            edit_transaction(data)
        elif choice == '8':
            print("👋 Exiting Expense Tracker. Stay smart with your spending!")
            break
        else:
            print("❌ Invalid choice. Please try again.\n")

# Step 12: Run the program
if __name__ == "__main__":
    main()
