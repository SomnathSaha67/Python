class Account:
    def __init__(self, account_number, account_password):
        self.account_number = account_number
        self.__account_password = account_password  # Private attribute
    def get_account_info(self):
        return f"Account Number: {self.account_number}"
    def verify_password(self, password):
        return self.__account_password == password
number_of_accounts = int(input("Enter number of accounts: "))
accounts = []
for _ in range(number_of_accounts):
    account_number = input("Enter account number: ")
    account_password = input("Enter account password: ")
    account = Account(account_number, account_password)
    accounts.append(account)
for idx, account in enumerate(accounts, start=1):
    print(f"Account {idx}:")
    print(account.get_account_info())
    test_password = input("Enter password to verify: ")
    if account.verify_password(test_password):
        print("Password is correct.")
    else:
        print("Password is incorrect.")