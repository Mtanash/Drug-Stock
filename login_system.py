from user import User


class LoginSystem:
    # def __init__(self, current_user):
    #     self.current_user = current_user

    def login(self, username, password):
        file = open("users.txt", "r")
        users = file.readlines()
        for user in users:
            user_info = user.split()
            user_name = user_info[0]
            user_email = user_info[1]
            user_password = user_info[2]
            if username == user_name and password == user_password:
                print(f'You logged in successfuly! Welcome {user_name}')
                return User(user_name, user_email, user_password)
            else:
                print('Invalid user name or password!')

    def register(self, username, email, password, password2):
        if not (password2 == password):
            print('You entered password wrong!')
            return
        # dealing with text file
        file = open("users.txt", "w")
        file.write(f"{username} {email} {password}\n")
        file.close()
        print('You registered a new user successfuly! Please login ')

    def logout(self, current_user):
        current_user.name = None
        current_user.email = None
        current_user.password = None
        print("You logged out!")
