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

class User:                          
    window.title('Вход в систему')

    psLabel=Label(
        text='новый пароль: ',
        background='#00FF7F',
        activebackground='#00FF7F',
        justify=CENTER,
        font=('Times Roman', 15),
        fg='black'
    )

    lgLabel=Label(
        text='Имя пользователя',
        background='#00FF7F',
        activebackground='#00FF7F',
        justify=CENTER,
        font=('Times Roman', 15, 'bold'),
        fg='red'
    )

    input = Entry(window, width=10)

    psBtn = Button(
        text='Change',
        background=config['btn_color_1'],
        activebackground=config['btn_color_2'],
        width='22',
        padx='0',
        pady='0',
        font=('Times Roman', 12, 'bold'),
    )

    exitBtn= Button(
        text='Выход',
        background='#00CED1',
        activebackground='#00CED1',
        width='22',
        padx='0',
        pady='0',
        font=('Times Roman', 12, 'bold'),
        command=lambda: Login()
    )

    psLabel.place(height=30, width=150, x = 30, y = 70)               # новый пароль
    input.place(height=25, width=200, x = 190, y = 72)              # форма для текста №1
    psBtn.place(height=25, width=120, x = 150, y = 120)            # изменить
    lgLabel.place(height=25, width=240, x = 80, y = 20)               # имя пользователя
    exitBtn.place(height=25, width=120, x = 150, y = 200)

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
    )

    aboutLabel.place(height=40, width=400, x = 20, y = 0)                # автор
    tasktitle.place(height=80, width=400, x = 20, y = 70)               # задание
    authorLabel.place(height=50, width=400, x = 30, y = 35)               # студент группы ИВТ-41 \rЛаптандер Александр Михайлович
    taskLabel.place(height=70, width=400, x = 10, y = 125)              # разработать программу, реализующую интерфейсную систему с применением механизмов парольной защиты
    exitBtn.place(height=30, width=70, x = 180, y = 210) 
    
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

    psOldLabel.place(height=30, width=150, x = 15, y = 38)    
    psNewLabel.place(height=30, width=150, x = 18, y = 84)   
    psOld.place(height=27, width=200, x = 180, y = 40)  
    psNew.place(height=27, width=200, x = 180, y = 85)  
    changeBtn.place(height=27, width=140, x = 140, y = 155)
    statusLabel.place(height=27, width=140, x = 140, y = 120)

def main():
    app = Login()
    app.start()
    app.end()
    
    mainloop()

main()

    
