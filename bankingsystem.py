import os
from datetime import datetime

CUSTOMER_FILE = "customers.txt"
TRANSACTION_FILE = "transactions.txt"

class BankingSystem:
    def __init__(self):
        self.customers = self.load_customers()

    def load_customers(self):
        """Load customers into dictionary from file."""
        customers = {}
        if not os.path.exists(CUSTOMER_FILE):
            open(CUSTOMER_FILE, "w").close()
        with open(CUSTOMER_FILE, "r") as f:
            for line in f:
                line = line.strip()
                if not line:
                    continue
                try:
                    name, acc_num, balance = line.split(",")
                    customers[acc_num] = {"name": name, "balance": float(balance)}
                except ValueError:
                    print(f"Skipping invalid record: {line}")
        return customers

    def save_customers(self):
        """Save all customers back to file."""
        with open(CUSTOMER_FILE, "w") as f:
            for acc_num, data in self.customers.items():
                f.write(f"{data['name']},{acc_num},{data['balance']}\n")

    def log_transaction(self, acc_num, action, amount):
        """Log deposit/withdrawal in file."""
        balance = self.customers[acc_num]["balance"]
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        with open(TRANSACTION_FILE, "a") as f:
            f.write(f"{timestamp},{acc_num},{action},{amount},{balance}\n")

    def deposit(self, acc_num, amount):
        if acc_num not in self.customers:
            print("Account not found.")
            return
        if amount <= 0:
            print("Deposit amount must be positive.")
            return
        self.customers[acc_num]["balance"] += amount
        self.log_transaction(acc_num, "Deposit", amount)
        print(f"Deposit successful. New balance: {self.customers[acc_num]['balance']}")

    def withdraw(self, acc_num, amount):
        if acc_num not in self.customers:
            print("Account not found.")
            return
        if amount <= 0:
            print("Withdrawal amount must be positive.")
            return
        if self.customers[acc_num]["balance"] < amount:
            print("Insufficient funds.")
            return
        self.customers[acc_num]["balance"] -= amount
        self.log_transaction(acc_num, "Withdrawal", amount)
        print(f"Withdrawal successful. New balance: {self.customers[acc_num]['balance']}")

    def display_customer(self, acc_num):
        if acc_num not in self.customers:
            print("Account not found.")
            return
        data = self.customers[acc_num]
        print(f"Name: {data['name']}, Account: {acc_num}, Balance: {data['balance']}")

    def create_account(self, name, acc_num, balance=0):
        if acc_num in self.customers:
            print("Account already exists.")
            return
        self.customers[acc_num] = {"name": name, "balance": balance}
        self.save_customers()
        print(f"Account created for {name} with balance {balance}.")


def main():
    bank = BankingSystem()

    while True:
        print("\n--- Banking System ---")
        print("1. Create Account")
        print("2. Deposit")
        print("3. Withdraw")
        print("4. View Customer")
        print("5. Exit")

        choice = input("Enter choice: ")

        if choice == "1":
            name = input("Enter customer name: ")
            acc = input("Enter account number: ")
            try:
                bal = float(input("Enter initial balance: "))
            except ValueError:
                print("Invalid balance.")
                continue
            bank.create_account(name, acc, bal)

        elif choice == "2":
            acc = input("Enter account number: ")
            try:
                amt = float(input("Enter amount: "))
            except ValueError:
                print("Invalid amount.")
                continue
            bank.deposit(acc, amt)

        elif choice == "3":
            acc = input("Enter account number: ")
            try:
                amt = float(input("Enter amount: "))
            except ValueError:
                print("Invalid amount.")
                continue
            bank.withdraw(acc, amt)

        elif choice == "4":
            acc = input("Enter account number: ")
            bank.display_customer(acc)

        elif choice == "5":
            bank.save_customers()
            print("Exiting... Data saved.")
            break
        else:
            print("Invalid choice.")


if __name__ == "__main__":
    main()
