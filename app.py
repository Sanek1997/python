from tkinter import *

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
    loginBtn = Button(
        text='войти',
        background=config['btn_color_1'],
        activebackground=config['btn_color_2'],
        width='22',
        padx='0',
        pady='0',
        font=('Times Roman', 12, 'bold'),
    )
    login = Entry(window, width=10)
    password = Entry(window, width=10)
    
    def start(self):
        self.lgLabel.place(height=32, width=150, x = 42, y = 50)     
        self.psLabel.place(height=32, width=170, x = 25, y = 90)  
        self.login.place(height=24, width=150, x = 200, y = 55)  
        self.password.place(height=24, width=150, x = 200, y = 95)  
        self.status.place(height=25, width=300, x = 100, y = 125) 
        self.loginBtn.place(height=32, width=120, x = 150, y = 155) 
    
    def end(self):
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
    )

    exit = Button(
        text='Выход',
        background=config['btn_color_3'],
        activebackground=config['btn_color_2'],
        width='22',
        padx='0',
        pady='0',
        font=('Times Roman', 12, 'bold'),
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
    def __init__(self, rules:list):
        self.rules = rules
        print('lol')
        w = Tk()
        w.geometry('315x255')              
        w.configure(bg = '#00FF7F') 

        self.rule_2 = Label(w,
            text='правило 2:',
            background='#00FF7F',
            activebackground='#00FF7F',
            justify=RIGHT,
            font=('Times Roman', 15),
            fg='black'
        )

        self.rule_4 = Label(w,
            text='правило 4:',
            background='#00FF7F',
            activebackground='#00FF7F',
            justify=RIGHT,
            font=('Times Roman', 15),
            fg='black'
        )

        self.rule_6 = Label(w,
            text='правило 6:',
            background='#00FF7F',
            activebackground='#00FF7F',
            justify=RIGHT,
            font=('Times Roman', 15),
            fg='black'
        )

        self.rule_8 = Label(w,
            text='правило 8:',
            background='#00FF7F',
            activebackground='#00FF7F',
            justify=RIGHT,
            font=('Times Roman', 15),
            fg='black'
        )

        self.rule_10 = Label(w,
            text='правило 10:',
            background='#00FF7F',
            activebackground='#00FF7F',
            justify=RIGHT,
            font=('Times Roman', 15),
            fg='black'
        )

        self.rule_11 = Label(w,
            text='правило 11:',
            background='#00FF7F',
            activebackground='#00FF7F',
            justify=RIGHT,
            font=('Times Roman', 15),
            fg='black'
        )
        self.chk_2 = Checkbutton(w, text='',                                # правило 1
            background=('#00FF7F'),
            activebackground=('#00FF7F')
        )

        self.chk_4 = Checkbutton(w, text='',                                # правило 2
            background=('#00FF7F'),
            activebackground=('#00FF7F')
        )

        self.chk_6 = Checkbutton(w, text='',                                # правило 3
            background=('#00FF7F'),
            activebackground=('#00FF7F')
        )

        self.chk_8 = Checkbutton(w, text='',                                # правило 4
            background=('#00FF7F'),
            activebackground=('#00FF7F')
        )

        self.chk_10 = Checkbutton(w, text='',                                # правило 5
            background=('#00FF7F'),
            activebackground=('#00FF7F')
        )

        self.chk_11 = Checkbutton(w, text='',                                # правило 6
            background=('#00FF7F'),
            activebackground=('#00FF7F')
        )
        self.save = Button(w,
            text='сохранить',
            background='#00CED1',
            activebackground='#00CED1',
            width='22',
            padx='0',
            pady='0',
            font=('Times Roman', 12, 'bold'),
        )
        self.exit = Button(w,
            text='выход',
            background='#00CED1',
            activebackground='#00CED1',
            width='22',
            padx='0',
            pady='0',
            font=('Times Roman', 12, 'bold'),
        )
    def start(self):
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
        self.rule_2.place_forget()
        self.rule_4.place_forget()
        self.rule_6.place_forget()
        self.rule_8.place_forget()
        self.rule_10.place_forget()
        self.rule_11.place_forget()
        self.chk_2.place_forget()
        self.chk_8.place_forget()
        self.chk_4.place_forget()
        self.chk_10.place_forget()
        self.chk_6.place_forget()
        self.chk_11.place_forget()
        self.save.place_forget()
        self.exit.place_forget()

class CreateUser:
    def __init__(self) -> None:
        pass
    
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
    )
    create = Button(
        text='создать',
        background='#00CED1',
        activebackground='#00CED1',
        width='22',
        padx='0',
        pady='0',
        font=('Times Roman', 12, 'bold'),
    )
    exit = Button(
        text='выход',
        background='#00CED1',
        activebackground='#00CED1',
        width='22',
        padx='0',
        pady='0',
        font=('Times Roman', 12, 'bold'),
    )

    def start(self):
        self.userNameLabel.place(height=25, width=170, x = 35, y = 39)               
        self.passwordLabel.place(height=25, width=80, x = 130, y = 79)              
        self.name.place(height=25, width=160, x = 215, y = 40)              
        self.password.place(height=25, width=160, x = 215, y = 80)              
        self.rules.place(height=25, width=100, x = 147, y = 150)            
        self.create.place(height=25, width=100, x = 90, y = 190)             
        self.exit.place(height=25, width=100, x = 210, y = 190)            
        self.status.place(height=25, width=100, x = 150, y = 115) 

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



def main():
    CreateUser().start()
    
    mainloop()

main()

    
