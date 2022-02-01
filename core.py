from dataManager import *

class Main:
    def __init__(self) -> None:
        self.psTryValue = 4

    def setName(self, name):
        self.name = name
        self.psTry = 0

    def getName(self):
        return self.name

    def psTry(self):
        self.psTryValue -= 1
        return self.psTryValue


    


def login(login, password):
    user = getUser(login)
    if user:
        if user['status'] == 'blocked':
            return 'Пользователь заблокирован'
        if user['password'] == password:
            return True
        return False
    return 'Пользователь не найден'
        
