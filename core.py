from dataManager import *
import datetime
import random

def login(login, password):
    user = getUser(login)
    if user:
        if user['status'] == 'blocked':
            return 'Пользователь заблокирован'
        if '4' in user['rules']:
            currentDate = datetime.datetime.now()
            rules = getRule(login)
            arr = rules['psdead'].split('-')
            arr = list(map(int, arr))
            deadDate = datetime.datetime(year=arr[0], month=arr[1], day=arr[2])
            dif = deadDate - currentDate
            if dif.total_seconds() < 0:
                return 'Срок действия пароля истек'
        if '8' in user['rules']:
            rules = getRule(login)['psTry']
            psTry = int(rules) - 1 
            if rules == '0':
                return 'Вы потратили все попытки(5) по правилу 8'
            addToRule(login, 'psTry', str(psTry))
        if user['password'] == password:
            return True
        if '10' in user['rules']:
            return '400'
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

def handleGeneratePass():
    n = 10 # Длина пароля
    letters = 'qwertyuiopasdfghjklzxcvbnm'
    password = ''
    for n in range(1, n):
        randChar = letters[random.randint(0, len(letters)-1)]
        password += randChar
    upper = letters.upper()
    password = upper[random.randint(0, len(upper)-1)] + password
    for n in range(1, 3):
        password += str(random.randint(0, 9))
    return password
    
