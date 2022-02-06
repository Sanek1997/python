from re import T
from tkinter import *
from tkinter import messagebox
from core import *
from tkcalendar import Calendar, DateEntry

config = {
    'btn_color_1': '#FA8072',                           # Цвет кнопок в обычном состоянии (добавить пользователя, Список имен пользователей, Изменить пароль)
    'btn_color_2': '#FA8072',                           # Цвет кнопок в наведенном состоянии (добавить пользователя, Список имен пользователей, Изменить пароль)
    'btn_color_3': '#AFEEEE'                            # Цвет кнопок в обычном состоянии ()
}

window = Tk()
window.geometry('415x255')              
window.configure(bg = '#00FF7F')  

class Login:
    def __init__(self) -> None:
        self.psTry = 4
    
    status = ''
    window.title('Login')
    lgLabel = Label(
        text='Введите логин: ',
        background='#00FF7F',
        activebackground='#00FF7F',
        justify=RIGHT,
        font=('Times Roman', 14, 'bold')
    )
    psLabel = Label(
        text='Введите пароль: ',
        background='#00FF7F',
        activebackground='#00FF7F',
        justify=RIGHT,
        font=('Times Roman', 14, 'bold')
    )
    status = Label(
        background='#00FF7F',
        activebackground='#00FF7F',
        justify=RIGHT,
        font=('Times Roman', 10, 'bold'),
        fg='red'
    )
    login = Entry(window, width=10)
    password = Entry(window, width=10)

    loginBtn = Button(
        text='войти',
        background=config['btn_color_1'],
        activebackground=config['btn_color_2'],
        width='22',
        padx='0',
        pady='0',
        font=('Times Roman', 12, 'bold'),
        command=lambda: handleLogin()
    )

    def setStatus(self, value):
        self.status.config(text=value)

    def psTryFn(self):
        print('and here')
        self.psTry -= 1
        return self.psTry

    def start(self):
        self.lgLabel.place(height=32, width=150, x = 42, y = 50)     
        self.psLabel.place(height=32, width=170, x = 25, y = 90)  
        self.login.place(height=24, width=150, x = 200, y = 55)  
        self.login.focus_set()
        self.password.place(height=24, width=150, x = 200, y = 95)  
        self.status.place(height=25, width=300, x = 100, y = 125) 
        self.loginBtn.place(height=32, width=120, x = 150, y = 155) 
    
    def end(self):
        self.login.delete(0, END)
        self.password.delete(0, END)
        self.status.config(text='')
        self.psTry = 4
        self.lgLabel.place_forget()
        self.psLabel.place_forget()
        self.login.place_forget()
        self.password.place_forget()
        self.status.place_forget()
        self.loginBtn.place_forget()

class Admin:
    def __init__(self) -> None:
        pass

    window.title('Admin Mode') 
    addUser = Button(
        text='Добавить пользователя', 
        background=config['btn_color_1'], 
        activebackground=config['btn_color_2'], 
        padx='0', 
        pady='0', 
        font=('Times Roman', 12, 'bold'),
        command=lambda:handleAddUserWd(),
    )
    userList = Button(
        text='Список имен пользователей',
        background=config['btn_color_1'],
        activebackground=config['btn_color_2'],
        width='22',
        padx='0',
        pady='0',
        font=('Times Roman', 12, 'bold'),
    )
    changePassword = Button(
        text='Изменить пароль',
        background=config['btn_color_1'],
        activebackground=config['btn_color_2'],
        width='22',
        padx='0',
        pady='0',
        font=('Times Roman', 12, 'bold'),
    )
    about = Button(
        text='о программе',
        background=config['btn_color_3'],
        activebackground=config['btn_color_2'],
        width='22',
        padx='0',
        pady='0',
        font=('Times Roman', 12, 'bold'),
        command=lambda: handleAddAboutWd(),
    )
    exit = Button(
        text='Выход',
        background=config['btn_color_3'],
        activebackground=config['btn_color_2'],
        width='22',
        padx='0',
        pady='0',
        font=('Times Roman', 12, 'bold'),
        command=lambda: handleExitAdmin(),
    )
    def start(self):
        self.addUser.place(height=35, width=250, x = 20, y = 20)          
        self.userList.place(height=35, width=250, x = 80, y = 80)          
        self.changePassword.place(height=32, width=250, x = 140, y = 140)        
        self.about.place(height=32, width=150, x = 20, y = 200)         
        self.exit.place(height=32, width=150, x = 240, y = 200) 

    def end(self):
        self.addUser.place_forget()
        self.userList.place_forget()
        self.changePassword.place_forget()
        self.about.place_forget()
        self.exit.place_forget()
    
    


class Rules:
    def __init__(self):
        self.rules = []
        self.w = Tk()
        self.w.geometry('315x255')              
        self.w.configure(bg = '#00FF7F')
        self.var_2 = IntVar(self.w)
        self.var_4 = IntVar(self.w)
        self.var_6 = IntVar(self.w) 
        self.var_8 = IntVar(self.w)
        self.var_10 = IntVar(self.w)
        self.var_11 = IntVar(self.w)

        self.rule_2 = Label(self.w,
            text='правило 2:',
            background='#00FF7F',
            activebackground='#00FF7F',
            justify=RIGHT,
            font=('Times Roman', 15),
            fg='black',
        )
        self.rule_4 = Label(self.w,
            text='правило 4:',
            background='#00FF7F',
            activebackground='#00FF7F',
            justify=RIGHT,
            font=('Times Roman', 15),
            fg='black'
        )
        self.rule_6 = Label(self.w,
            text='правило 6:',
            background='#00FF7F',
            activebackground='#00FF7F',
            justify=RIGHT,
            font=('Times Roman', 15),
            fg='black'
        )
        self.rule_8 = Label(self.w,
            text='правило 8:',
            background='#00FF7F',
            activebackground='#00FF7F',
            justify=RIGHT,
            font=('Times Roman', 15),
            fg='black'
        )
        self.rule_10 = Label(self.w,
            text='правило 10:',
            background='#00FF7F',
            activebackground='#00FF7F',
            justify=RIGHT,
            font=('Times Roman', 15),
            fg='black'
        )
        self.rule_11 = Label(self.w,
            text='правило 11:',
            background='#00FF7F',
            activebackground='#00FF7F',
            justify=RIGHT,
            font=('Times Roman', 15),
            fg='black'
        )
        self.chk_2 = Checkbutton(self.w, text='',                                # правило 1
            background=('#00FF7F'),
            activebackground=('#00FF7F'),
            state='active',
            command=self.setChecked,
            variable=self.var_2,
            onvalue=1,
            offvalue=0,
        )
        self.chk_4 = Checkbutton(self.w, text='',                                # правило 2
            background=('#00FF7F'),
            activebackground=('#00FF7F'),
            command=self.setChecked,
            onvalue=1,
            offvalue=0,
            variable=self.var_4
        )
        self.chk_6 = Checkbutton(self.w, text='',                                # правило 3
            background=('#00FF7F'),
            activebackground=('#00FF7F'),
            command=self.setChecked,
            variable=self.var_6,
            onvalue=1,
            offvalue=0,
        )
        self.chk_8 = Checkbutton(self.w, text='',                                # правило 4
            background=('#00FF7F'),
            activebackground=('#00FF7F'),
            command=self.setChecked,
            variable=self.var_8,
        )
        self.chk_10 = Checkbutton(self.w, text='',                                # правило 5
            background=('#00FF7F'),
            activebackground=('#00FF7F'),
            command=self.setChecked,
            variable=self.var_10,
            onvalue=1,
            offvalue=0,
        )
        self.chk_11 = Checkbutton(self.w, text='',                                # правило 6
            background=('#00FF7F'),
            activebackground=('#00FF7F'),
            command=self.setChecked,
            variable=self.var_11,
            onvalue=1,
            offvalue=0,
        )
        self.save = Button(self.w,
            text='сохранить',
            background='#00CED1',
            activebackground='#00CED1',
            width='22',
            padx='0',
            pady='0',
            font=('Times Roman', 12, 'bold'),
            command=lambda: handleSaveRules(rules=self.rules)
        )
        self.exit = Button(self.w,
            text='выход',
            background='#00CED1',
            activebackground='#00CED1',
            width='22',
            padx='0',
            pady='0',
            font=('Times Roman', 12, 'bold'),
        )
    
    def setChecked(self):
        tmp = []
        if (self.var_2.get()): tmp.append('2')
        if (self.var_4.get()): tmp.append('6')
        if (self.var_6.get()): tmp.append('10')
        if (self.var_8.get()): tmp.append('4')
        if (self.var_10.get()): tmp.append('8')
        if (self.var_11.get()): tmp.append('11')
        self.rules = tmp

    def start(self, values:list):
        if ('2' in values): self.var_2.set(1)
        if ('4' in values): self.var_8.set(1)
        if ('6' in values): self.var_4.set(1)
        if ('8' in values): self.var_10.set(1)
        if ('10' in values): self.var_6.set(1)
        if ('11' in values): self.var_11.set(1)
        self.rule_2.place(height=20, width=100, x = 120, y = 15)              
        self.rule_4.place(height=20, width=100, x = 120, y = 45)              
        self.rule_6.place(height=20, width=100, x = 120, y = 75)              
        self.rule_8.place(height=20, width=100, x = 120, y = 105)             
        self.rule_10.place(height=20, width=100, x = 120, y = 135)             
        self.rule_11.place(height=20, width=100, x = 120, y = 165)             
        self.chk_2.place(height=20, width=20, x = 230, y = 17)
        self.chk_8.place(height=20, width=20, x = 230, y = 47)
        self.chk_4.place(height=20, width=20, x = 230, y = 77)
        self.chk_10.place(height=20, width=20, x = 230, y = 107)
        self.chk_6.place(height=20, width=20, x = 230, y = 137)
        self.chk_11.place(height=20, width=20, x = 230, y = 167)
        self.save.place(height=30, width=120, x = 50, y = 205)              
        self.exit.place(height=30, width=120, x = 195, y = 205)

    def end(self):
        self.w.destroy()

class CreateUser:
    def __init__(self):
        self.ruleItems = []
        self.passDeadline = None
    
    userNameLabel = Label(text='имя пользователя:',
        background='#00FF7F',
        activebackground='#00FF7F',
        justify=RIGHT,
        font=('Times Roman', 15),
        fg='black'
    )

    passwordLabel = Label(text='пароль:',
        background='#00FF7F',
        activebackground='#00FF7F',
        justify=RIGHT,
        font=('Times Roman', 15),
        fg='black'
    )
    status=Label(
        background='#00FF7F',
        activebackground='#00FF7F',
        justify=RIGHT,
        font=('Times Roman', 10, 'bold'),
        fg='red'
    )
    name = Entry(window, width=10)
    password = Entry(window, width=10)
    rules = Button(
        text='правила',
        background='#EE82EE',
        activebackground='#EE82EE',
        width='22',
        padx='0',
        pady='0',
        font=('Times Roman', 12, 'bold'),
        command=lambda: handleAddRulesWd(),
    )
    create = Button(
        text='создать',
        background='#00CED1',
        activebackground='#00CED1',
        width='22',
        padx='0',
        pady='0',
        font=('Times Roman', 12, 'bold'),
        command=lambda: handleCreateUser(),
    )
    exit = Button(
        text='выход',
        background='#00CED1',
        activebackground='#00CED1',
        width='22',
        padx='0',
        pady='0',
        font=('Times Roman', 12, 'bold'),
        command=lambda: handleExitAddUserWd(),
    )
    def setRules(self, rules):
        self.ruleItems = rules

    def setStatus(self, value):
        self.status.config(text=value)

    def setPassDeadline(self, value):
        self.passDeadline = value

    def start(self):
        self.userNameLabel.place(height=25, width=170, x = 35, y = 39)               
        self.passwordLabel.place(height=25, width=80, x = 130, y = 79)              
        self.name.place(height=25, width=160, x = 215, y = 40)              
        self.password.place(height=25, width=160, x = 215, y = 80)              
        self.rules.place(height=25, width=100, x = 147, y = 150)            
        self.create.place(height=25, width=100, x = 90, y = 190)             
        self.exit.place(height=25, width=100, x = 210, y = 190)            
        self.status.place(height=25, width=180, x = 150, y = 115) 

    def end(self):
        self.userNameLabel.place_forget()               
        self.passwordLabel.place_forget()              
        self.name.place_forget()              
        self.password.place_forget()              
        self.rules.place_forget()            
        self.create.place_forget()             
        self.exit.place_forget()            
        self.status.place_forget()

class UserList:
    def __init__(self) -> None:
        pass

    prev = Button(
        text='предыдущий',
        background=config['btn_color_1'],
        activebackground=config['btn_color_2'],
        width='22',
        padx='0',
        pady='0',
        font=('Times Roman', 12, 'bold')
    )
    next = Button(
        text='cледующий',
        background=config['btn_color_1'],
        activebackground=config['btn_color_2'],
        width='22',
        padx='0',
        pady='0',
        font=('Times Roman', 12, 'bold')
    )
    deleteUser = Button(
        text='Удалить пользователя',
        background=config['btn_color_1'],
        activebackground=config['btn_color_2'],
        width='22',
        padx='0',
        pady='0',
        font=('Times Roman', 12, 'bold')
    )
    save = Button(
        text='Сохранить',
        background=config['btn_color_1'],
        activebackground=config['btn_color_2'],
        width='22',
        padx='0',
        pady='0',
        font=('Times Roman', 12, 'bold')
    )
    exit = Button(
        text='Закрыть',
        background=config['btn_color_1'],
        activebackground=config['btn_color_2'],
        width='22',
        padx='0',
        pady='0',
        font=('Times Roman', 12, 'bold'),
        command=lambda: Login()
    )
    rules = Button(
        text='Правила',
        background=config['btn_color_1'],
        activebackground=config['btn_color_2'],
        width='22',
        padx='0',
        pady='0',
        font=('Times Roman', 12, 'bold')
    )
    blocked = Checkbutton(text='Заблокировать пользователя',
        background=('#00FF7F'),
        activebackground=('#00FF7F'),
    )
    userName = Entry(window, width=10, state='readonly')

    def start(self):
        self.userName.place(height=30, width=150, x = 10, y = 15)               
        self.prev.place(height=32, width=120, x = 170, y = 15)              # предыдущий
        self.next.place(height=32, width=110, x = 290, y = 15)              # следующий
        self.deleteUser.place(height=32, width=220, x = 95, y = 90)              # удалить пользователя
        self.save.place(height=30, width=120, x = 80, y = 150)              # сохранить
        self.exit.place(height=30, width=120, x = 210, y = 150)            # отмена
        self.rules.place(height=30, width=120, x = 145, y = 210)             # правила
        self.blocked.place(height=20, width=180, x = 10, y = 50) 

    def end(self):
        self.userName.place_forget()
        self.prev.place_forget()
        self.next.place_forget()
        self.deleteUser.place_forget()
        self.save.place_forget()
        self.exit.place_forget()
        self.rules.place_forget()
        self.blocked.place_forget()

class User:             
    def __init__(self):
        self.login = ''

    window.title('Вход в систему')

    psLabel=Label(
        text='новый пароль: ',
        background='#00FF7F',
        activebackground='#00FF7F',
        justify=CENTER,
        font=('Times Roman', 15),
        fg='black'
    )

    userLabel=Label(
        text='',
        background='#00FF7F',
        activebackground='#00FF7F',
        justify=CENTER,
        font=('Times Roman', 15, 'bold'),
        fg='red'
    )

    input = Entry(window, width=10)

    change = Button(
        text='Change',
        background=config['btn_color_1'],
        activebackground=config['btn_color_2'],
        width='22',
        padx='0',
        pady='0',
        font=('Times Roman', 12, 'bold'),
        command=lambda:handleChangePassword(),
    )

    exitBtn= Button(
        text='Выход',
        background='#00CED1',
        activebackground='#00CED1',
        width='22',
        padx='0',
        pady='0',
        font=('Times Roman', 12, 'bold'),
        command=lambda: handleUserExit()
    )

    def getLogin(self):
        return self.login

    def start(self, value):
        self.login = value
        self.userLabel.config(text=value)
        self.psLabel.place(height=30, width=150, x = 30, y = 70)               # новый пароль
        self.input.place(height=25, width=200, x = 190, y = 72)              # форма для текста №1
        self.change.place(height=25, width=120, x = 150, y = 120)            # изменить
        self.userLabel.place(height=25, width=240, x = 80, y = 20)               # имя пользователя
        self.exitBtn.place(height=25, width=120, x = 150, y = 200)

    def end(self):
        self.psLabel.place_forget()
        self.input.place_forget()
        self.change.place_forget()
        self.userLabel.place_forget()
        self.exitBtn.place_forget()

class About:
    window.title('Об авторе')
    aboutLabel=Label(text='Автор: ',
        background='#00FF7F',
        activebackground='#00FF7F',
        justify=CENTER,
        font=('Times Roman', 16, 'bold'),
        fg='red'
    )
    tasktitle=Label(text='Задание: ',
        background='#00FF7F',
        activebackground='#00FF7F',
        justify=CENTER,
        font=('Times Roman', 16, 'bold'),
        fg='red'
    )
    authorLabel=Label(text='студент группы ИВТ-41 \rЛаптандер Александр Михайлович ',
        background='#00FF7F',
        activebackground='#00FF7F',
        justify=LEFT,
        font=('Times Roman', 15),
        fg='black'
    )
    taskLabel=Label(text='Разработать программу, реализующую \r интерфейсную систему с применением \r механизмов парольной защиты ',
        background='#00FF7F',
        activebackground='#00FF7F',
        justify=CENTER,
        font=('Times Roman', 15),
        fg='black'
    )   
    exitBtn = Button(
        text='выход',
        background=config['btn_color_1'],
        activebackground=config['btn_color_2'],
        width='22',
        padx='0',
        pady='0',
        font=('Times Roman', 12, 'bold'),
        command=lambda:handleExitAboutWd(),
    )

    def start(self):
        self.aboutLabel.place(height=40, width=400, x = 20, y = 0)                # автор
        self.tasktitle.place(height=80, width=400, x = 20, y = 70)               # задание
        self.authorLabel.place(height=50, width=400, x = 30, y = 35)               # студент группы ИВТ-41 \rЛаптандер Александр Михайлович
        self.taskLabel.place(height=70, width=400, x = 10, y = 125)              # разработать программу, реализующую интерфейсную систему с применением механизмов парольной защиты
        self.exitBtn.place(height=30, width=70, x = 180, y = 210) 

    def end(self):
        self.aboutLabel.place_forget()
        self.tasktitle.place_forget()
        self.authorLabel.place_forget()
        self.taskLabel.place_forget()
        self.exitBtn.place_forget()

class Change:
    window.title('Изменение пароля')
    
    psOldLabel=Label(text='старый пароль:',
        background='#00FF7F',
        activebackground='#00FF7F',
        justify=RIGHT,
        font=('Times Roman', 15),
        fg='black'
    )

    changeBtn = Button(
        text='Изменить',
        background=config['btn_color_1'],
        activebackground=config['btn_color_2'],
        width='22',
        padx='0',
        pady='0',
        font=('Times Roman', 12, 'bold'),
    )

    statusLabel=Label(text='статус:',
        background='#00FF7F',
        activebackground='#00FF7F',
        justify=RIGHT,
        font=('Times Roman', 15),
        fg='black'
    )

    psNewLabel=Label(text='новый пароль:',
        background='#00FF7F',
        activebackground='#00FF7F',
        justify=RIGHT,
        font=('Times Roman', 15),
        fg='black'
    )

    psOld = Entry(window, width=10)
    psNew = Entry(window, width=10)

    def start(self):
        self.psOldLabel.place(height=30, width=150, x = 15, y = 38)    
        self.psNewLabel.place(height=30, width=150, x = 18, y = 84)   
        self.psOld.place(height=27, width=200, x = 180, y = 40)  
        self.psNew.place(height=27, width=200, x = 180, y = 85)  
        self.changeBtn.place(height=27, width=140, x = 140, y = 155)
        self.statusLabel.place(height=27, width=140, x = 140, y = 120)

    def end(self):
        self.psOldLabel.place_forget()
        self.psNewLabel.place_forget()
        self.psOld.place_forget()
        self.psNew.place_forget()
        self.changeBtn.place_forget()
        self.statusLabel.place_forget()

class CalendarWd:
    def __init__(self) -> None:
        self.tkobj = Tk()
        self.tkobj.geometry("300x300+700+200")
        self.tkobj.title("Calendar picker")
        self.tkc = Calendar(self.tkobj,selectmode="day",year=2022,month=2,date=7)
        self.but = Button(self.tkobj,text="Select Date", command=lambda:handleSaveDate(),bg="black", fg='white')
        self.date = Label(self.tkobj,text='Выберите дату сброса пароля',
            justify=RIGHT,
            font=('Times Roman', 10),
            fg='black'
        )        
        self.tkobj.overrideredirect(True)

    def setCalLabel(self, value):
        self.date.config(text=value)
        
    def start(self):
        self.but.pack()
        self.date.pack()
        self.tkc.pack(pady=40)

    def end(self):
        self.but.pack_forget()
        self.tkc.pack_forget()
        self.date.pack_forget()
        self.tkobj.destroy()




        

login_wd = Login()
# login_wd.start()
user_wd = User()
admin_wd = Admin()
admin_wd.start()
addUser_wd = CreateUser()
about_wd = About()

def handleLogin():
    login_val = login_wd.login.get()
    password = login_wd.password.get()
    res = login(login_val, password)
    if type(res) == str:
        login_wd.setStatus(res)
    else:
        if res:
            login_wd.end()
            if login_val == 'ADMIN':
                admin_wd.start()
            else:
                user_wd.start(login_val)
        else:
            count = login_wd.psTryFn()
            if count == 0:
                window.destroy()
            tmp = 'Неверный пароль, осталось попыток:' + str(count)
            login_wd.setStatus(tmp)

def handleChangePassword():
    password = user_wd.input.get()
    login = user_wd.getLogin()
    updateUser(login, 'password', password)
    messagebox.showinfo("Change password", "Пароль изменен")

def handleUserExit():
    user_wd.end()
    login_wd.start()

def handleAddUserWd():
    admin_wd.end()
    addUser_wd.start()

def handleSaveRules(rules:list):
    if '4' in rules:
        handleAddCalendar()
    addUser_wd.setRules(rules)
    rules_wd.end()

def handleAddRulesWd():
    global rules_wd
    rules_wd = Rules()
    rules_wd.start(addUser_wd.ruleItems)

def handleAddCalendar():
    global cal
    cal = CalendarWd()
    cal.start()

def handleSaveDate():
    date = cal.tkc.get_date()
    if not(date):
        cal.setCalLabel('Выберите дату')
    else:
        addUser_wd.setPassDeadline(date)
        cal.end()
    
def handleCreateUser():
    login_val = addUser_wd.name.get()
    password = addUser_wd.password.get()
    rules = addUser_wd.ruleItems
    res = createUser(login_val, password, rules)
    if (type(res)==str):
        print('401')
        addUser_wd.setStatus(res)
    else:
        if res:
            addUser_wd.setStatus('')
            messages = []
            if '2' in rules: messages.append('Правило 2: Пароль состоит из цифр, символов верхнего и нижнего регистра')
            if '4' in rules: messages.append('Правило 4: Пароль действует до ' + addUser_wd.passDeadline)
            if '6' in rules: messages.append('Правило 6: Включен журнал истории паролей(history.txt)')
            if '8' in rules: messages.append('Правило 8: Ограничение на ввод пароля(5 попыток, после ввода последней пользователь блокируется)')
            if '10' in rules: messages.append('Правило 10: Включен таймаут на ввод пароля')
            if '11' in rules: messages.append('Правило 11: Пользователь не может менять пароль')
            out = 'Пользователь создан\n' + '\n'.join(messages) 
            messagebox.showinfo('Succes', out)
        else:
            messagebox.showwarning('', 'Правило 2: Пароль должен содержать цифры, символы верхнего и нижнего регистра')

def handleExitAdmin():
    admin_wd.end()
    login_wd.start()

def handleAddAboutWd():
    admin_wd.end()
    about_wd.start()

def handleExitAboutWd():
    about_wd.end()
    admin_wd.start()

def handleExitAddUserWd():
    addUser_wd.end()
    admin_wd.start()
    
mainloop()

    
