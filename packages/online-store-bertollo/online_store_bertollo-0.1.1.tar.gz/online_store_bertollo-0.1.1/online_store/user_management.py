class UserManager:
    def __init__(self):
        self.users = {}

    def add_user(self, user_id, user_data):
        if self.users.get(user_id) is not None:
            print(f"Клиент с ID {user_id} уже существует")
            return
        self.users[user_id] = user_data
        print(f"Клиент с ID {user_id} добавлен")

    def remove_user(self, user_id):
        if self.users.get(user_id) is None:
            print(f"Клиент с ID {user_id} не найден")
            return
        del self.users[user_id]
        print(f"Клиент с ID {user_id} удалён")

    def update_user(self, user_id, user_data):
        if self.users.get(user_id) is None:
            print(f"Клиент с ID {user_id} не найден")
            return
        for k, v in user_data.items():
            self.users[user_id][k] = v
        print(f"Данные клиента с ID {user_id} обновлены")

    def find_user(self, user_id):
        if self.users.get(user_id) is None:
            print(f"Клиент с ID {user_id} не найден")
            return
        return self.users[user_id]
