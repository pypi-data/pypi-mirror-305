class UserManager:
    def __init__(self):
        self.users = dict()

    def add_user(self, user_id, user_data):
        if user_id in self.users:
            print(f'Клиент с ID {user_id} уже существует')
        else:
            self.users[user_id] = user_data
            print(f'Клиент с ID {user_id} добавлен')

    def remove_user(self, user_id):
        if not(user_id in self.users):
            print(f'Клиент с ID {user_id} не найден')
        else:
            self.users.pop(user_id)
            print(f'Клиент с ID {user_id} удалён')

    def update_user(self, user_id, user_data):
        if not(user_id in self.users):
            print(f'Клиент с ID {user_id} не найден')
        else:
            for i, j in user_data.items():
                self.users[user_id][i] = j
            print(f'Данные клиента с ID {user_id} обновлены')

    def find_user(self, user_id):
        if not(user_id in self.users):
            return f'Клиент с ID {user_id} не найден'
        else:
            return self.users[user_id]