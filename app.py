database = []


def writeDatabaseToFile(database):
    file = open("data.txt", "w")
    for i in range(len(database)):
        name = database[i][0]
        dates = list(database[i][1].keys())
        amounts = list(database[i][1].values())

        for x in range(len(dates)):
            file.write(f"{name} {dates[x]} {amounts[x]}\n")


def check_if_name_exist(name):
    if len(database) >= 1:
        for i in range(len(database)):
            if database[i][0] == name:
                return i
                break
    else:
        return None


def readDatabaseFromFile(file_path):
    file = open(file_path, "r")
    data_list = file.readlines()
    database = []
    for i in data_list:
        splited_data = i.split()
        name, date, amount = splited_data
        create(name, date, amount)
    return database


def create(name, date, amount):
    if check_if_name_exist(name) != None:
        index = check_if_name_exist(name)
        if database[index][1].get(date) != None:
            new_amount = int(database[index][1][date]) + int(amount)
            database[index][1][date] = new_amount
        else:
            database[index][1][date] = amount
    else:
        database.append([name, {date: amount}])
    writeDatabaseToFile(database)


def print_all_database():
    for i in range(len(database)):
        output = f"name: {database[i][0]}, date: {database[i][1]}"
        print(output)


def print_element_of_database(element_name):
    for i in range(len(database)):
        if database[i][0] == element_name:
            output = f"name: {database[i][0]} , dates: {database[i][1]}"
            print(output)
            break
        else:
            print('There is no drug with this name!')


commands = ["exit >> to exit the programe", "create >> to create a new product",
            "print_all >> to print all products", "print >> to print a product by it's name"]


def main():
    readDatabaseFromFile("data.txt")
    while True:
        user_input = input("Enter command: ").lower()
        if user_input == "exit":
            break
        elif user_input == "create":
            name = input("Enter name: ")
            date = input("Enter date: ")
            amount = input("Enter amount: ")
            create(name, date, amount)
        elif user_input == "print_all":
            print_all_database()
        elif user_input == "print":
            print_element_of_database(input("Enter element name: "))
        else:
            print("Enter a valid command!", commands)


if __name__ == "__main__":
    main()
