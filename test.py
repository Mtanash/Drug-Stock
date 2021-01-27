# database = [['adol', {'10/2022': '3', '05/2023': '9'}],
#             ['panadol', {'11/2021': '6', '06/2024': '36'}]]


def writeDatabaseToFile(database):
    file = open("data.txt", "w")
    for i in range(len(database)):
        name = database[i][0]
        dates = list(database[i][1].keys())
        amounts = list(database[i][1].values())

        for x in range(len(dates)):
            file.write(f"{name} {dates[x]} {amounts[x]}\n")
        # file.write(f"{name} {dates} {amounts}\n")


def check_if_name_exist(name, database):
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
        # if check_if_name_exist(splited_data[0], database) != None:
        #     index = check_if_name_exist(splited_data[0], database)
        #     if database[index][1].get(splited_data[1]) != None:
        #         new_amount = int(
        #             database[index][1][splited_data[1]]) + int(splited_data[2])
        #         database[index][1][splited_data[1]] = new_amount
        #     else:
        #         database[index][1][splited_data[1]] = splited_data[2]
        # else:
        #     database.append(
        #         [splited_data[0], {splited_data[1]: splited_data[2]}])
        name, date, amount = splited_data
        print(name, date, amount)
    return database


readDatabaseFromFile("data.txt")
