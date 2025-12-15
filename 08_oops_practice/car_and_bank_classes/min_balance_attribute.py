class BankAccount:
    @staticmethod
    def min_balance():
        return 100.0  
    def __init__(self, account_number, account_holder, balance=0.0):
        self.account_number = account_number
        self.account_holder = account_holder
        self.balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"Deposited: ${amount:.2f}. New balance: ${self.balance:.2f}")
        else:
            print("Deposit amount must be positive.")

    def withdraw(self, amount):
        if amount > 0:
            if amount <= self.balance:
                if self.balance - amount < BankAccount.min_balance():
                    print(f"Cannot withdraw ${amount:.2f}. Minimum balance of ${BankAccount.min_balance():.2f} must be maintained.")
                    return
                self.balance -= amount
                print(f"Withdrew: ${amount:.2f}. New balance: ${self.balance:.2f}")
            else:
                print("Insufficient funds for this withdrawal.")
        else:
            print("Withdrawal amount must be positive.")

    def get_balance(self):
        return self.balance

    def get_account_info(self):
        return {
            "Account Number": self.account_number,
            "Account Holder": self.account_holder,
            "Balance": self.balance
        }
number_of_accounts = int(input("Enter number of bank accounts: "))
accounts = []
for _ in range(number_of_accounts):
    account_number = input("Enter account number: ")
    account_holder = input("Enter account holder name: ")
    initial_balance = float(input("Enter initial balance (or press Enter for $0.00): ") or 0.0)
    account = BankAccount(account_number, account_holder, initial_balance)
    accounts.append(account)
for account in accounts:
    info = account.get_account_info()
    print(f"\nAccount Number: {info['Account Number']}, Account Holder: {info['Account Holder']}, Balance: ${info['Balance']:.2f}")
    deposit_amount = float(input("Enter amount to deposit: "))
    account.deposit(deposit_amount)
    print(f"Current Balance: ${account.get_balance():.2f}")
    withdraw_amount = float(input("Enter amount to withdraw: "))
    account.withdraw(withdraw_amount)
