database = [['adol', {'hhh': '3', 'lll': '9'}], ['panadol', {'7777': '6'}]]


def check_if_name_exist(name):
    for i in range(len(database)):
        if database[i][0] == name:
            return i
            break


def create():
    name = input("Enter name: ")
    date = input("Enter date: ")
    amount = input("Enter amount: ")
    if check_if_name_exist(name) != None:
        index = check_if_name_exist(name)
        if database[index][1][date] != None:
            new_amount = int(database[index][1][date]) + int(amount)
            database[index][1][date] = new_amount
        else:
            database[index][1][date] = amount
    else:
        database.append([name, {date: amount}])


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


while True:
    user_input = input("Enter command: ").lower()
    if user_input == "exit":
        break
    elif user_input == "create":
        create()
    elif user_input == "print_all":
        print_all_database()
    elif user_input == "print":
        print_element_of_database(input("Enter element name: "))
    print(database)
