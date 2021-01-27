class User:
    def __init__(self, name=None, email=None, password=None):
        self.name = name
        self.email = email
        self.password = password

    def print_data(self):
        print(f'User name => {self.name}')
        print(f'User email => {self.email}')

    def check_user(self):
        if self.name == None:
            print("There is no current user logged in!")
        else:
            self.print_data()
