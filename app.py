from database import DataBase

commands = ["exit >> to exit the programe", "create >> to create a new product",
            "print_all >> to print all products", "print >> to print a product by it's name"]


def main():
    myDatabase = DataBase([])
    myDatabase.readDatabaseFromFile("data.txt")
    while True:
        user_input = input("Enter command: ").lower()
        if user_input == "exit":
            break
        elif user_input == "create":
            name = input("Enter name: ")
            date = input("Enter date: ")
            amount = input("Enter amount: ")
            myDatabase.create(name, date, amount)
        elif user_input == "print_all":
            myDatabase.print_all_database()
        else:
            print("Enter a valid command!", commands)


if __name__ == "__main__":
    main()
