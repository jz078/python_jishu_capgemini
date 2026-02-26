# from abc import ABC, abstractmethod

# class BankAccount(ABC):
#     def __init__(self, customer_name, account_number, date_of_birth, balance = 0):
#         self.customer_name = customer_name
#         self.__account_number = account_number
#         self.__date_of_birth = date_of_birth
#         self.__balance = balance

# # abstract methods
#     @abstractmethod
#     def deposit(self, deposit_amount):
#         pass

#     @abstractmethod
#     def withdraw(self, withdraw_amount):
#         pass

#     def display_account_details(self):
#         print(f"Name: {self.customer_name}")
#         print(f"Account No: {self.__account_number}")
#         print(f"Balance: ₹{self.__balance}")

#     # Encapsulated getter
#     def get_balance(self):
#         return self.__balance
    
#     # Protected balance updater (used by subclasses)
#     def _update_balance(self, amount):
#         self.__balance += amount


# # savings acccount
# class SavingsAccount(BankAccount):
#     def __init__(self, customer_name, account_number, date_of_birth, balance=0, minimum_balance=1000):
#         super().__init__(customer_name, account_number, date_of_birth, balance)
#         self.__minimum_balance = minimum_balance

#         def deposit(self, deposit_amount):
#             balance += deposit_amount
#             print("Deposited rs{deposit_amount}")




from abc import ABC, abstractmethod

# Abstract Base Class
class BankAccount(ABC):
    def __init__(self, customer_name, date_of_birth, account_number, balance=0):
        self.customer_name = customer_name          # public
        self.__date_of_birth = date_of_birth        # private
        self.__account_number = account_number      # private
        self.__balance = balance                    # private


    @abstractmethod
    def deposit(self, amount):
        pass

    @abstractmethod
    def withdraw(self, amount):
        pass

    # Encapsulated getter
    def get_balance(self):
        return self.__balance

    # Protected balance updater (used by subclasses)
    def _update_balance(self, amount):
        self.__balance += amount

    def display_account_details(self):
        print(f"Name: {self.customer_name}")
        print(f"Account No: {self.__account_number}")
        print(f"Balance: ₹{self.__balance}")




# Savings Account
class SavingsAccount(BankAccount):
    def __init__(self, customer_name, date_of_birth, account_number, balance=0, minimum_balance=1000):
        super().__init__(customer_name, date_of_birth, account_number, balance)
        self.minimum_balance = minimum_balance

    def deposit(self, amount):
        if amount > 0:
            self._update_balance(amount)
            print(f"Deposited ₹{amount}")
        else:
            print("Invalid deposit amount")

    def withdraw(self, amount):
        if amount <= 0:
            print("Invalid withdraw amount")
        elif self.get_balance() - amount < self.minimum_balance:
            print("Withdrawal denied: Minimum balance required")
        else:
            self._update_balance(-amount)
            print(f"Withdrawn ₹{amount}")


# Current Account
class CurrentAccount(BankAccount):
    def __init__(self, customer_name, date_of_birth, account_number, balance=0, overdraft_limit=5000):
        super().__init__(customer_name, date_of_birth, account_number, balance)
        self.overdraft_limit = overdraft_limit

    def deposit(self, amount):
        if amount > 0:
            self._update_balance(amount)
            print(f"Deposited ₹{amount}")
        else:
            print("Invalid deposit amount")

    def withdraw(self, amount):
        if amount <= 0:
            print("Invalid withdraw amount")
        elif self.get_balance() + self.overdraft_limit < amount:
            print("Withdrawal denied: Overdraft limit exceeded")
        else:
            self._update_balance(-amount)
            print(f"Withdrawn ₹{amount}")


# ---- Example Usage ----
sav = SavingsAccount("Jishu", "01-01-2000", "SA123", balance=5000)
sav.deposit(1000)
sav.withdraw(4500)
sav.display_account_details()

print()

cur = CurrentAccount("Jishu", "01-01-2000", "CA456", balance=2000)
cur.withdraw(6000)
cur.display_account_details()