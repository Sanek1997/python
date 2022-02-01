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

def main():
    app = Login()
    app.start()
    app.end()
    
    mainloop()

main()

    
