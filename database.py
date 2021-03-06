class DataBase:
    def __init__(self, database, file_path):
        self.database = database
        self.file_path = file_path

    def writeDatabaseToFile(self):
        with open(self.file_path, "w") as file:
            for i in range(len(self.database)):
                name = self.database[i][0]
                dates = list(self.database[i][1].keys())
                amounts = list(self.database[i][1].values())

                for x in range(len(dates)):
                    file.write(f"{name} {dates[x]} {amounts[x]}\n")

    def check_if_name_exist(self, name):
        if len(self.database) >= 1:
            for i in range(len(self.database)):
                if self.database[i][0] == name:
                    return i
                    break
        else:
            return None

    def create(self, name, date, amount):
        if self.check_if_name_exist(name) != None:
            index = self.check_if_name_exist(name)
            if self.database[index][1].get(date) != None:
                new_amount = int(self.database[index][1][date]) + int(amount)
                self.database[index][1][date] = new_amount
            else:
                self.database[index][1][date] = amount
        else:
            self.database.append([name, {date: amount}])
            print("Created new product successfuly!")
        self.writeDatabaseToFile()

    def readDatabaseFromFile(self, file_path):
        with open(file_path, "r") as file:
            data_list = file.readlines()
            database = []
            for i in data_list:
                splited_data = i.split()
                name, date, amount = splited_data
                self.create(name, date, amount)
        return database

    def print_all(self):
        with open(self.file_path, "r") as file:
            data_list = file.readlines()
            printed_products = []
            for i in data_list:
                splited_data = i.split()
                name, date, amount = splited_data
                print(
                    """
        [{}]
    {}      {}
    --------------------
    """.format(name, date, amount))
