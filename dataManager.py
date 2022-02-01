from turtle import update

fName = 'data.txt'
delimiter = '::'

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
