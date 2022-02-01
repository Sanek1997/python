from dataManager import *

def login(login, password):
    user = getUser(login)
    if user:
        if user['status'] == 'blocked':
            return 'Пользователь заблокирован'
        if user['password'] == password:
            return True
        return False
    return 'Пользователь не найден'
    
def createUser(login, password, rules):
    user = getUser(login)
    if user: return 'Логин занят'
    addUser(login, password, rules)
    return True
