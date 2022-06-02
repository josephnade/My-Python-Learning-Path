import json
import os


class User:
    def __init__(self, username, password, email):
        self.username = username
        self.password = password
        self.email = email


class UserRepository:
    def __init__(self):
        self.users = []
        self.isLoggedIn = False
        self.currentUser = {}
        # load from .json file
        self.loadUsers()

    def loadUsers(self):
        if os.path.exists("users.json"):
            with open("users.json", "r", encoding="utf-8") as file:
                users = json.load(file)
                for user in users:
                    user = json.loads(user)
                    newUser = User(username=user["username"], password=user["password"], email=user["email"])
                    self.users.append(newUser)

    def register(self, user: User):
        self.users.append(user)
        self.savetoFile()
        print("User has been created.")

    def login(self, username, password):
        for user in self.users:
            if user.username == username and user.password == password:
                self.isLoggedIn = True
                self.currentUser = user
            else:
                self.isLoggedIn = False
        if self.isLoggedIn == True:
            print("Succesfully Log in!")
        else:
            print("Failed to Log in!")

    def logout(self):
        self.isLoggedIn = False
        self.currentUser = {}
        print("Successfully Log out!")

    def identity(self):
        if self.isLoggedIn == True:
            print(
                f"1-) Username:{self.currentUser.username} \n2-)Password: {self.currentUser.password}\n3-)Email: {self.currentUser.email}")
        else:
            print("Not Logged In!")

    def savetoFile(self):
        list = []
        for user in self.users:
            list.append(json.dumps(user.__dict__))
        with open("users.json", "w") as file:
            json.dump(list, file)


repository = UserRepository()
while True:
    print('Menu'.center(50, '*'))
    choose = input("1- Register\n2- Login\n 3- Logout\n4- Identity \n5- Exit\nPlease choose 1-5: ")
    if choose == "5":
        print("Have a good day".center(50, "*"))
        break
    elif choose == "1":
        # Register
        username = input("Username: ")
        password = input("Password: ")
        email = input("Email: ")
        user = User(username=username, password=password, email=email)
        repository.register(user)
    elif choose == "2":
        username = input("Username: ")
        password = input("Password: ")
        repository.login(username=username, password=password)
        pass
    elif choose == "3":
        repository.logout()
    elif choose == "4":
        # Identity
        print("Current User".center(50, "*"))
        repository.identity()
    else:
        print("Wrong choose.")
