class BankAccount:
    def __init__(self, account_number, account_holder, balance):
        self.account_number = account_number    # Public
        self._account_holder = account_holder   # Protected
        self.__balance = balance                # Private

    # Public method to display account info
    def display_account_info(self):
        print(f"Account Number: {self.account_number}")
        print(f"Account Holder: {self._account_holder}")

    # Public method to access private balance safely
    def get_balance(self):
        return self.__balance

    # Public method to update private balance safely
    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            print(f"Deposited {amount}. New Balance: {self.__balance}")
        else:
            print("Deposit amount must be positive.")

    def withdraw(self, amount):
        if 0 < amount <= self.__balance:
            self.__balance -= amount
            print(f"Withdrew {amount}. New Balance: {self.__balance}")
        else:
            print("Insufficient balance or invalid amount!")


# Create object
acc1 = BankAccount("123456", "Alex", 1000)

# Public variable
print("Account Number:", acc1.account_number)

# Protected variable (accessible, but not recommended outside class or subclass)
print("Account Holder (Protected):", acc1._account_holder)

# Private variable (will raise AttributeError if accessed directly)
# print(acc1.__balance)   #  Error

# Correct way to access private variable
print("Balance:", acc1.get_balance())

# Using methods
acc1.deposit(500)
acc1.withdraw(200)
