class UserManager:
    def __init__(self):
        #Initialization a dictionary for storing accounts
        self.data_account = {}

    def add_user(self, user_id, user_data):
        #Add user if it not exists
        if user_id not in self.data_account.keys():
            self.data_account[user_id] = user_data
            return f"Клиент с ID <{user_id}> добавлен"
        return f"Клиент с ID <{user_id}> уже существует"

    def remove_user(self, user_id):
        #Remove user if it exists
        if user_id in self.data_account.keys():
            del self.data_account[user_id]
            return f"Клиент с ID <{user_id}> удалён"
        return f"Клиент с ID <{user_id}> не найден"

    def update_user(self, user_id, user_data):
        #Updata client data
        if user_id in self.data_account.keys():
            self.data_account[user_id] = user_data
            return f"Данные клиента с ID <{user_id}> обновлены"
        return f"Клиент с ID <{user_id}> не найден"

    def find_user(self, user_id):
        #Search account
        if user_id in self.data_account.keys():
            return self.data_account[user_id]
        return f"Клиент с ID <{user_id}> не найден"