from turtle import update
from venv import create

fName = 'data.txt'
delimiter = '::'
rulesFName = 'rules.txt'
hisFName = 'history.txt'

#<local>
def _setMockData():
    mock = [
        'deniko::blocked::blocked::3-4-2',
        'petya::qwe::active::2',
        'alex::123qwe::active::2-3',
        'steve::14124::blocked::3-4'
    ]
    f = open(fName, 'w')
    f.write('\n'.join(mock))

def _remapLineToDict(line:str):
    arr = line[:-1].split(delimiter)
    return {
        'login': arr[0],
        'password': arr[1],
        'status': arr[2],
        'rules': arr[3].split('-'),
    }

def _remapDictToLine(dct: dict):
    dct['rules'] = '-'.join(dct['rules'])
    return delimiter.join(dct.values())+'\n'

def _getLogin(line:str):
    return line[:-1].split(delimiter)[0]

def _update(line:str, login, key, value):
    if _getLogin(line) == login:
        dct = _remapLineToDict(line)
        dct[key] = value
        return _remapDictToLine(dct)
    return line

def _remapRulesToDict(line:str):
    arr = line.split(',')
    out = {}
    for item in arr:
        elem = item.split('-')
        out[elem[0]] = elem[1]
    return out
#</local>

def getData():
    f = open(fName, 'r')
    users = []
    for line in f:
        users.append(_remapLineToDict(line))
    f.close()
    return users

def getUser(login:str):
    f = open(fName, 'r')
    for line in f:
        if (_getLogin(line) == login):
            return _remapLineToDict(line)
    f.close()

def updateUser(login, key, value):
    print('event', login, key, value)
    f = open(fName, 'r')
    lines = f.readlines()
    f.close()
    update = open(fName, 'w')
    newLines = list(map(lambda line: _update(line, login, key, value), lines))
    update.writelines(newLines)
    f.close()

def addUser(login, password, rules:list):
    f = open(fName, 'a')
    line = delimiter.join([login, password, 'active', '-'.join(rules)])+'\n'
    f.write(line)
    f.close()

def deleteUser(login):
    f = open(fName, 'r')
    lines = f.readlines()
    f.close()
    update = open(fName, 'w')
    newLines = list(filter(lambda line: _getLogin(line) != login, lines))
    update.writelines(newLines)
    f.close()

def addToRule(login, rule, value):
    f = open(rulesFName, 'r')
    lines = f.readlines()
    f.close()
    newLines = []
    for line in lines:
        elem = line[:-1].split(delimiter)
        if login == elem[0]:
            rules = _remapRulesToDict(elem[1])
            rules[rule] = value
            s = ''
            for key in rules:
                s += key+'-'+rules[key]+','
            s = login + delimiter +s[:-1] + '\n'
            newLines.append(s)
        else:
            newLines.append(line)
    f = open(rulesFName, 'w')
    f.writelines(newLines)
    f.close()


def createRule(login, rules, date):
    defaultPsTry = 5                # Правило 8: Ограничение на попытки ввода, в задаче не указано 
    f = open(rulesFName, 'a')       # на сколько попыток ставится ограничение, по умолчанию = 5
    data = {}
    if '4' in rules:
        data['psdead'] = date
    if '8' in rules:
        data['psTry'] = defaultPsTry
    line = ''
    for key in data:
        line += key+'-'+str(data[key])+','
    line = login+delimiter+line[:-1]+'\n'
    f.write(line)
    f.close()

def deleteRule(login):
    f = open(rulesFName, 'r')
    lines = f.readlines()
    f.close()
    newLines = []
    for line in lines:
        name = line.split(delimiter)[0]
        if login != name:
            newLines.append(line)
    f = open(rulesFName, 'w')
    f.writelines(newLines)
    f.close()

def createHistory(login, password):
    f = open(hisFName, 'a')
    line = login+delimiter+password+'\n'
    f.write(line)
    f.close()

def addPassToHistory(login, password):
    f = open(hisFName, 'r')
    lines = f.readlines()
    f.close()
    f = open(hisFName, 'w')
    newLines = []
    for line in lines:
        s = line.split(delimiter)
        if s[0] == login: 
            newLines.append(login+delimiter+s[1][:-1]+','+password+'\n')
        else:
            newLines.append(line)
    f.writelines(newLines)
    f.close()

def deleteHistory(login):
    f = open(hisFName, 'r')
    lines = f.readlines()
    f.close()
    newLines = []
    for line in lines:
        name = line.split(delimiter)[0]
        if login != name:
            newLines.append(line)
    f = open(hisFName, 'w')
    f.writelines(newLines)
    f.close()
