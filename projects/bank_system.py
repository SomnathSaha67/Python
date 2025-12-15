# Simple Bank Management System (OOP + File I/O)

ACCOUNTS_FILE = "accounts.txt"


class BankAccount:
    # Class attribute: same minimum balance for all accounts
    min_balance = 0.0

    def __init__(self, account_number, holder_name, balance=0.0):
        self.account_number = account_number
        self.holder_name = holder_name
        self.balance = float(balance)

    def deposit(self, amount):
        if amount <= 0:
            print("Deposit amount must be positive.")
            return
        self.balance += amount
        print(f"Deposited {amount} to account {self.account_number}. New balance: {self.balance}")

    def withdraw(self, amount):
        if amount <= 0:
            print("Withdraw amount must be positive.")
            return
        if self.balance - amount < BankAccount.min_balance:
            print("Insufficient funds (would go below minimum balance).")
            return
        self.balance -= amount
        print(f"Withdrew {amount} from account {self.account_number}. New balance: {self.balance}")

    def transfer_to(self, other_account, amount):
        if amount <= 0:
            print("Transfer amount must be positive.")
            return
        if self.balance - amount < BankAccount.min_balance:
            print("Insufficient funds to transfer (would go below minimum balance).")
            return
        self.balance -= amount
        other_account.balance += amount
        print(
            f"Transferred {amount} from {self.account_number} "
            f"to {other_account.account_number}."
        )
        print(f"Your new balance: {self.balance}")

    def print_details(self):
        print("\n--- Account Details ---")
        print(f"Account number: {self.account_number}")
        print(f"Holder name   : {self.holder_name}")
        print(f"Balance       : {self.balance}")


class BankSystem:
    def __init__(self):
        # Store accounts in a dict: {account_number: BankAccount}
        self.accounts = {}
        self.next_account_number = 1  # simple auto-increment

    def load_from_file(self):
        """Load accounts from ACCOUNTS_FILE into self.accounts."""
        try:
            with open(ACCOUNTS_FILE, "r") as f:
                for line in f:
                    line = line.strip()
                    if not line:
                        continue
                    # Format: account_number,holder_name,balance
                    parts = line.split(",")
                    if len(parts) != 3:
                        continue
                    acc_no_str, holder_name, balance_str = parts
                    try:
                        acc_no = int(acc_no_str)
                        balance = float(balance_str)
                    except ValueError:
                        continue
                    account = BankAccount(acc_no, holder_name, balance)
                    self.accounts[acc_no] = account

                    # Keep track of the maximum account number to continue sequence
                    if acc_no >= self.next_account_number:
                        self.next_account_number = acc_no + 1

            print("Accounts loaded from file.")
        except FileNotFoundError:
            print("No accounts file found. Starting with an empty bank.")

    def save_to_file(self):
        """Save all accounts from self.accounts to ACCOUNTS_FILE."""
        with open(ACCOUNTS_FILE, "w") as f:
            for acc_no, account in self.accounts.items():
                # Format: account_number,holder_name,balance
                line = f"{account.account_number},{account.holder_name},{account.balance}\n"
                f.write(line)
        print("All accounts saved to file.")

    def create_account(self):
        holder_name = input("Enter account holder name: ").strip()
        if not holder_name:
            print("Holder name cannot be empty.")
            return

        try:
            initial_deposit = float(input("Enter initial deposit amount: "))
        except ValueError:
            print("Invalid amount.")
            return

        if initial_deposit < BankAccount.min_balance:
            print(f"Initial deposit must be at least {BankAccount.min_balance}.")
            return

        acc_no = self.next_account_number
        self.next_account_number += 1

        account = BankAccount(acc_no, holder_name, initial_deposit)
        self.accounts[acc_no] = account
        print(f"Account created successfully. Your account number is {acc_no}.")

    def find_account(self, acc_no):
        return self.accounts.get(acc_no)

    def delete_account(self):
        try:
            acc_no = int(input("Enter account number to delete: "))
        except ValueError:
            print("Invalid account number.")
            return

        account = self.find_account(acc_no)
        if account is None:
            print("Account not found.")
            return

        confirm = input(
            f"Are you sure you want to delete account {acc_no}? (yes/no): "
        ).strip().lower()
        if confirm == "yes":
            del self.accounts[acc_no]
            print(f"Account {acc_no} deleted.")
        else:
            print("Deletion cancelled.")

    def deposit_to_account(self):
        try:
            acc_no = int(input("Enter account number: "))
        except ValueError:
            print("Invalid account number.")
            return

        account = self.find_account(acc_no)
        if account is None:
            print("Account not found.")
            return

        try:
            amount = float(input("Enter amount to deposit: "))
        except ValueError:
            print("Invalid amount.")
            return

        account.deposit(amount)

    def withdraw_from_account(self):
        try:
            acc_no = int(input("Enter account number: "))
        except ValueError:
            print("Invalid account number.")
            return

        account = self.find_account(acc_no)
        if account is None:
            print("Account not found.")
            return

        try:
            amount = float(input("Enter amount to withdraw: "))
        except ValueError:
            print("Invalid amount.")
            return

        account.withdraw(amount)

    def transfer_between_accounts(self):
        try:
            from_acc_no = int(input("Enter your account number: "))
            to_acc_no = int(input("Enter target account number: "))
        except ValueError:
            print("Invalid account number.")
            return

        from_account = self.find_account(from_acc_no)
        to_account = self.find_account(to_acc_no)

        if from_account is None:
            print("Source account not found.")
            return
        if to_account is None:
            print("Target account not found.")
            return

        try:
            amount = float(input("Enter amount to transfer: "))
        except ValueError:
            print("Invalid amount.")
            return

        from_account.transfer_to(to_account, amount)

    def show_account_details(self):
        try:
            acc_no = int(input("Enter account number: "))
        except ValueError:
            print("Invalid account number.")
            return

        account = self.find_account(acc_no)
        if account is None:
            print("Account not found.")
        else:
            account.print_details()

    def list_all_accounts(self):
        if not self.accounts:
            print("No accounts available.")
            return
        print("\n--- All Accounts ---")
        for acc_no, account in self.accounts.items():
            print(
                f"Account: {acc_no}, Holder: {account.holder_name}, "
                f"Balance: {account.balance}"
            )

    def change_min_balance(self):
        try:
            new_min = float(input("Enter new minimum balance for all accounts: "))
        except ValueError:
            print("Invalid amount.")
            return
        if new_min < 0:
            print("Minimum balance cannot be negative.")
            return
        BankAccount.min_balance = new_min
        print(f"Minimum balance set to {BankAccount.min_balance}.")


def main():
    bank = BankSystem()
    bank.load_from_file()

    while True:
        print(
            "\n--- Bank Management System ---\n"
            " 1. Create new account\n"
            " 2. Deposit\n"
            " 3. Withdraw\n"
            " 4. Transfer\n"
            " 5. Show account details\n"
            " 6. List all accounts\n"
            " 7. Change minimum balance\n"
            " 8. Save & Exit"
        )
        choice = input("Enter choice number: ").strip()

        if choice == "1":
            bank.create_account()
        elif choice == "2":
            bank.deposit_to_account()
        elif choice == "3":
            bank.withdraw_from_account()
        elif choice == "4":
            bank.transfer_between_accounts()
        elif choice == "5":
            bank.show_account_details()
        elif choice == "6":
            bank.list_all_accounts()
        elif choice == "7":
            bank.change_min_balance()
        elif choice == "8":
            bank.save_to_file()
            print("Exiting Bank Management System.")
            break
        else:
            print("Invalid choice. Please enter a number from 1 to 8.")


main()
