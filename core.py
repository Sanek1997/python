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
    
def createUser(login, password:str, rules:list):
    letters = 'qwertyuiopasdfghjklzxcvbnm1234567890'
    minPassLen = 6
    for char in password.lower():
        if not(char in letters):
            return 'Недопустимые символы'
    if not(len(login)): return 'Введите имя пользователя' 
    if len(password) < minPassLen: return 'Мин. длина пароля: ' + str(minPassLen)
    user = getUser(login)
    if user: return 'Логин занят'
    if '2' in rules:
        hasUpperCase = password != password.lower()
        hasLowerCase = password != password.upper()
        hasDigit = any(map(str.isdigit, password))
        res = all([hasUpperCase, hasLowerCase, hasDigit])
        if not(res): return False
    addUser(login, password, rules)
    return True

def checkRules(password:str, rules:list): 
    for rule in rules:
        if rule == '2':     # Проверяем пароль на буквы разных регистров и цифры
            hasUpperCase = password != password.lower()
            hasLowerCase = password != password.upper()
            hasDigit = any(map(str.isdigit, password))
            return all([hasUpperCase, hasLowerCase, hasDigit])