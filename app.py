from database import DataBase
from login_system import LoginSystem
from user import User


commands = ["exit >> to exit the programe", "create >> to create a new product",
            "print_all >> to print all products", "print >> to print a product by it's name"]


class DrugStorage:
    def __init__(self, current_user, login_system, database, user_commands):
        super().__init__()
        self.current_user = current_user
        self.login_system = login_system
        self.database = database
        self.user_commands = user_commands

    def handle_login(self):
        username = input('Enter user name: ')
        password = input('Enter password: ')
        self.current_user = self.login_system.login(username, password)

    def handle_register(self):
        username = input('Enter user name: ')
        email = input('Enter a valid email: ')
        password = input('Enter password: ')
        password2 = input('Repeat password: ')
        self.login_system.register(username, email, password, password2)

    def handle_logout(self):
        self.login_system.logout(self.current_user)

    def print_user(self):
        self.current_user.check_user()

    def handle_create_product(self):
        name = input("Enter name: ")
        date = input("Enter date: ")
        amount = input("Enter amount: ")
        self.database.create(name, date, amount)

    def main(self):
        self.database.readDatabaseFromFile("data.txt")
        while True:
            user_input = input("Enter command: ").lower()
            if user_input == "exit":
                break
            elif user_input == "create":
                self.handle_create_product()
            elif user_input == "print_all":
                self.database.print_all()
            elif user_input == "login":
                self.handle_login()
            elif user_input == "logout":
                self.handle_logout()
            elif user_input == "register":
                self.handle_register()
            elif user_input == "print_user":
                self.print_user()
            else:
                print("Enter a valid command!", commands)


app = DrugStorage(User(), LoginSystem(), DataBase([], "data.txt"), commands)
app.main()
