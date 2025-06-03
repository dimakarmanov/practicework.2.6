class User:
    def __init__(self, login, password):
        self.Login = login
        self.Password = password

    def current_user(self, login, password):
        for user in list:
            if login == self.Login and password == self.Password:
                return user

list = [
    User("qwerty", "asdfg"),
    User("wasd", "dfjhsgd"),
    User("admin", "admin"),
    User("martin", "martinwashere75"),
    User("dima", "whereismypassword?")
]

martin = User("martin", "martinwashere75")
martin.current_user(martin.Login, martin.Password)
print("Логин пользователя: ", martin.Login)
print("Пароль пользователя: ", martin.Password)