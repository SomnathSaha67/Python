class BankAccount:
    def __init__(self, account_number, account_holder, balance):
        self.account_number = account_number
        self.account_holder = account_holder
        self.balance = balance
    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            return self.balance
        else:
            return "Deposit amount must be positive."
    def withdraw(self, amount):
        if 0<= amount <= self.balance:
            print("Withdrawal successful!")
            self.balance -= amount
            return self.balance
        else:
            return "Insufficient balance or invalid amount."
number_of_accounts = int(input("Enter number of bank accounts: "))
accounts = []
for _ in range(number_of_accounts):
    account_number = input("Enter account number: ")
    account_holder = input("Enter account holder name: ")
    balance = float(input("Enter initial balance: "))
    account = BankAccount(account_number, account_holder, balance)
    accounts.append(account)
for account in accounts:
    print(f"\nAccount Number: {account.account_number}, Account Holder: {account.account_holder}, Balance: {account.balance}")
    deposit_amount = float(input("Enter amount to deposit: "))
    new_balance = account.deposit(deposit_amount)
    print(f"New Balance after deposit: {new_balance}")
    withdraw_amount = float(input("Enter amount to withdraw: "))
    new_balance = account.withdraw(withdraw_amount)
    print(f"New Balance after withdrawal: {new_balance}")
            