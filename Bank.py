import datetime
import csv

# Step 1: Define the BankAccount class
class BankAccount:
    def __init__(self, owner, account_number):
        self.owner = owner
        self.account_number = account_number
        self.balance = 0.0
        self.transactions = []

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            self.transactions.append((datetime.datetime.now(), 'Deposit', amount, self.balance))
            print(f"Deposited ₹{amount:.2f}")
        else:
            print("Invalid deposit amount.")

    def withdraw(self, amount):
        if 0 < amount <= self.balance:
            self.balance -= amount
            self.transactions.append((datetime.datetime.now(), 'Withdrawal', -amount, self.balance))
            print(f"Withdrew ₹{amount:.2f}")
        else:
            print("Insufficient balance or invalid amount.")

    def check_balance(self):
        print(f"Current balance: ₹{self.balance:.2f}")

    def view_transactions(self):
        print("\nTransaction History:")
        print("Date & Time           | Type       | Amount   | Balance")
        print("----------------------------------------------------------")
        for t in self.transactions:
            date, t_type, amount, bal = t
            print(f"{date.strftime('%Y-%m-%d %H:%M:%S')} | {t_type:<10} | ₹{amount:>7.2f} | ₹{bal:>7.2f}")

    def export_statement(self, filename, filetype='txt'):
        try:
            if filetype == 'csv':
                with open(filename, 'w', newline='') as file:
                    writer = csv.writer(file)
                    writer.writerow(['Date & Time', 'Type', 'Amount', 'Balance'])
                    for t in self.transactions:
                        writer.writerow([t[0].strftime('%Y-%m-%d %H:%M:%S'), t[1], t[2], t[3]])
            else:
                with open(filename, 'w') as file:
                    file.write("Date & Time           | Type       | Amount   | Balance\n")
                    file.write("----------------------------------------------------------\n")
                    for t in self.transactions:
                        file.write(f"{t[0].strftime('%Y-%m-%d %H:%M:%S')} | {t[1]:<10} | ₹{t[2]:>7.2f} | ₹{t[3]:>7.2f}\n")
            print(f"Statement saved to {filename}")
        except Exception as e:
            print(f"Error saving statement: {e}")

    def edit_name(self, new_name):
        self.owner = new_name
        print(f"Name updated to: {self.owner}")

    def edit_account_number(self, new_number):
        self.account_number = new_number
        print(f"Account number updated to: {self.account_number}")

    def edit_last_deposit(self, new_amount):
        for i in reversed(range(len(self.transactions))):
            if self.transactions[i][1] == 'Deposit':
                old_amount = self.transactions[i][2]
                self.balance -= old_amount
                self.balance += new_amount
                self.transactions[i] = (
                    self.transactions[i][0], 'Deposit', new_amount, self.balance
                )
                print(f"Last deposit updated from ₹{old_amount:.2f} to ₹{new_amount:.2f}")
                return
        print("No deposit transaction found to edit.")

    def view_profile(self):
        print("\n===== Account Profile =====")
        print(f"Account Holder Name : {self.owner}")
        print(f"Account Number      : {self.account_number}")
        print(f"Current Balance     : ₹{self.balance:.2f}")
        print(f"Total Transactions  : {len(self.transactions)}")
        if self.transactions:
            last = self.transactions[-1]
            print(f"Last Transaction    : {last[1]} of ₹{last[2]:.2f} on {last[0].strftime('%Y-%m-%d %H:%M:%S')}")
        else:
            print("Last Transaction    : No transactions yet.")

# Step 2: Create a new account
def create_new_account(accounts):
    print("\n===== Create New Bank Account =====")
    owner = input("Enter your name: ")
    account_number = input("Enter desired account number: ")
    if account_number in accounts:
        print("Account number already exists.")
    else:
        accounts[account_number] = BankAccount(owner, account_number)
        print(f"Account created for {owner} (Account No: {account_number})")

# Step 3: Select an account by account number
def get_account(accounts):
    acc_num = input("Enter account number: ")
    if acc_num in accounts:
        return accounts[acc_num]
    else:
        print("Account not found.")
        return None

# Step 4: Main program loop
def main():
    accounts = {}

    while True:
        print("\n===== Intelligent Banking Transaction Simulator =====")
        print("1. Create New Account")
        print("2. Deposit")
        print("3. Withdraw")
        print("4. Check Balance")
        print("5. View Transactions")
        print("6. Export Statement")
        print("7. Edit Account Holder Name")
        print("8. Edit Account Number")
        print("9. Edit Last Deposit Amount")
        print("10. View Account Profile")
        print("11. Exit")
        choice = input("Select an option (1–11): ")

        if choice == '1':
            create_new_account(accounts)

        elif choice == '2':
            acc = get_account(accounts)
            if acc:
                name = input("Enter account holder name to confirm: ")
                if name == acc.owner:
                    amt = float(input("Enter amount to deposit: ₹"))
                    acc.deposit(amt)
                else:
                    print("Name does not match. Deposit cancelled.")

        elif choice == '3':
            acc = get_account(accounts)
            if acc:
                amt = float(input("Enter amount to withdraw: ₹"))
                acc.withdraw(amt)

        elif choice == '4':
            acc = get_account(accounts)
            if acc:
                acc.check_balance()

        elif choice == '5':
            acc = get_account(accounts)
            if acc:
                acc.view_transactions()

        elif choice == '6':
            acc = get_account(accounts)
            if acc:
                fname = input("Enter filename (e.g., statement.txt or statement.csv): ")
                ftype = 'csv' if fname.endswith('.csv') else 'txt'
                acc.export_statement(fname, ftype)

        elif choice == '7':
            acc = get_account(accounts)
            if acc:
                new_name = input("Enter new name: ")
                acc.edit_name(new_name)

        elif choice == '8':
            acc = get_account(accounts)
            if acc:
                new_number = input("Enter new account number: ")
                if new_number in accounts:
                    print("Error: Account number already exists.")
                else:
                    accounts[new_number] = acc
                    del accounts[acc.account_number]
                    acc.edit_account_number(new_number)

        elif choice == '9':
            acc = get_account(accounts)
            if acc:
                new_amount = float(input("Enter new deposit amount: ₹"))
                acc.edit_last_deposit(new_amount)

        elif choice == '10':
            acc = get_account(accounts)
            if acc:
                acc.view_profile()

        elif choice == '11':
            print("Thank you for using the simulator. Goodbye!")
            break

        else:
            print("Invalid option. Please try again.")

# Step 5: Run the program
if __name__ == "__main__":
    main()
