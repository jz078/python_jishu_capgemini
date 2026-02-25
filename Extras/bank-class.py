# create a bank class
    # it should have 4 static (class) members
    # create 3 objects
    # each object should have 3 object (specific) members




# class Bank:
#     # 4 static (clsss) members
#     bank_name = "SBI"
#     branch = "khadagpur"
#     ifsc = "SBIN0001234"
#     interest_rate = 3.4

#     def __init__(self, acc_no, name, balance):
#         # each object have 3 object (specific) members
#         self.acc_no = acc_no

#         self.name = name
#         self.balance = balance


# # created 3 objects
# b1 = Bank(101, "aman", 4000)
# b2 = Bank(102, "riya", 3000)
# b3 = Bank(103, "rahul", 5000)

# print(b1.acc_no, b1.name, b1.balance)
# print(b2.acc_no, b2.name, b2.balance)
# print(b3.acc_no, b3.name, b3.balance)


# # accessing static members
# print(Bank.bank_name, Bank.branch, Bank.ifsc, Bank.interest_rate)







class Bank:
    # 4 static (class) members
    bank_name = "State Bank"
    branch = "Kharagpur"
    ifsc = "SBIN0001234"
    interest_rate = 6.5


# creating 3 objects
b1 = Bank()
b2 = Bank()
b3 = Bank()

# adding 3 object-specific members manually
b1.acc_no = 101
b1.name = "Aman"
b1.balance = 5000

b2.acc_no = 102
b2.name = "Riya"
b2.balance = 8000

b3.acc_no = 103
b3.name = "Rahul"
b3.balance = 12000


# printing object details
print(b1.acc_no, b1.name, b1.balance)
print(b2.acc_no, b2.name, b2.balance)
print(b3.acc_no, b3.name, b3.balance)

# accessing static members
print(Bank.bank_name, Bank.branch, Bank.ifsc, Bank.interest_rate)





















# class Bank:
#     # 4 static (class) members
#     bank_name = "State Bank"
#     branch = "Kharagpur"
#     ifsc = "SBIN0001234"
#     interest_rate = 6.5

#     def __init__(self, acc_no, name, balance):
#         # 3 object (instance) members
#         self.acc_no = acc_no
#         self.name = name
#         self.balance = balance


# # creating 3 objects
# b1 = Bank(101, "Aman", 5000)
# b2 = Bank(102, "Riya", 8000)
# b3 = Bank(103, "Rahul", 12000)


# # printing object details
# print(b1.acc_no, b1.name, b1.balance)
# print(b2.acc_no, b2.name, b2.balance)
# print(b3.acc_no, b3.name, b3.balance)

# # accessing static members
# print(Bank.bank_name, Bank.branch, Bank.ifsc, Bank.interest_rate)