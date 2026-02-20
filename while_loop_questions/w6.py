# simulate a login system with 3 attempts.

user = "jishu"
pwd = 1234

count = 3


while count>0 :
    username = str(input("Enter username: "))
    password = int(input("Enter password: "))

    if(username == user and password == pwd):
        print("login successful")
        break
    else:
        print("invalid credentials")
        count-=1
        print(count, " attempts left")