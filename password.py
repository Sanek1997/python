from cProfile import label
from tkinter import*
from turtle import clear
from xmlrpc.client import Boolean
from core import *

config = {
    'btn_color_1': '#FA8072',                           # Цвет кнопок в обычном состоянии (добавить пользователя, Список имен пользователей, Изменить пароль)
    'btn_color_2': '#FA8072',                           # Цвет кнопок в наведенном состоянии (добавить пользователя, Список имен пользователей, Изменить пароль)
    'btn_color_3': '#AFEEEE'                            # Цвет кнопок в обычном состоянии ()
}

main = Main()

window = Tk()

btn_1 = Button(
    text='Добавить пользователя', 
    background=config['btn_color_1'], 
    activebackground=config['btn_color_2'], 
    padx='0', 
    pady='0', 
    font=('Times Roman', 12, 'bold'),
    command=lambda: clear()
)

btn_2 = Button(
    text='Список имен пользователей',
    background=config['btn_color_1'],
    activebackground=config['btn_color_2'],
    width='22',
    padx='0',
    pady='0',
    font=('Times Roman', 12, 'bold'),
    command=lambda: List_of_users()
)

btn_3 = Button(
    text='Изменить пароль',
    background=config['btn_color_1'],
    activebackground=config['btn_color_2'],
    width='22',
    padx='0',
    pady='0',
    font=('Times Roman', 12, 'bold'),
    command=lambda: Admin_Mode(),
)

btn_4 = Button(
    text='о программе',
    background=config['btn_color_3'],
    activebackground=config['btn_color_2'],
    width='22',
    padx='0',
    pady='0',
    font=('Times Roman', 12, 'bold'),
    command=lambda: Author()
)

btn_5 = Button(
    text='Выход',
    background=config['btn_color_3'],
    activebackground=config['btn_color_2'],
    width='22',
    padx='0',
    pady='0',
    font=('Times Roman', 12, 'bold'),
    command=lambda: Login()
)

btn_6 = Button(
    text='предыдущий',
    background=config['btn_color_1'],
    activebackground=config['btn_color_2'],
    width='22',
    padx='0',
    pady='0',
    font=('Times Roman', 12, 'bold')
)

btn_7 = Button(
    text='cледующий',
    background=config['btn_color_1'],
    activebackground=config['btn_color_2'],
    width='22',
    padx='0',
    pady='0',
    font=('Times Roman', 12, 'bold')
)

btn_8 = Button(
    text='Удалить пользователя',
    background=config['btn_color_1'],
    activebackground=config['btn_color_2'],
    width='22',
    padx='0',
    pady='0',
    font=('Times Roman', 12, 'bold')
)

btn_9 = Button(
    text='Сохранить',
    background=config['btn_color_1'],
    activebackground=config['btn_color_2'],
    width='22',
    padx='0',
    pady='0',
    font=('Times Roman', 12, 'bold')
)

btn_10 = Button(
    text='Отмена',
    background=config['btn_color_1'],
    activebackground=config['btn_color_2'],
    width='22',
    padx='0',
    pady='0',
    font=('Times Roman', 12, 'bold'),
    command=lambda: Login()
)

btn_11 = Button(
    text='Правила',
    background=config['btn_color_1'],
    activebackground=config['btn_color_2'],
    width='22',
    padx='0',
    pady='0',
    font=('Times Roman', 12, 'bold')
)

btn_12 = Button(
    text='войти',
    background=config['btn_color_1'],
    activebackground=config['btn_color_2'],
    width='22',
    padx='0',
    pady='0',
    font=('Times Roman', 12, 'bold')
)

btn_13 = Button(
    text='войти',
    background=config['btn_color_1'],
    activebackground=config['btn_color_2'],
    width='22',
    padx='0',
    pady='0',
    font=('Times Roman', 12, 'bold'),
    command=lambda: handleLogin()
)


def handleLogin():
    login_val = txt_2.get()
    res = login(login_val, txt_3.get())
    if type(res) == str:
        lbl_11.config(text=res)
    else:
        if res:
            main.setName(login_val)
            forgetAll()
            if login_val == 'ADMIN':
                Admin_Mode()
            else:
                lbl_8.config(text=login_val)
                User()
        else:
            count = main.psTry()
            if count == 0:
                window.destroy()
            tmp = 'Неверный пароль, осталось попыток:' + str(count)
            lbl_11.config(text=tmp)

    
btn_14 = Button(
    text='выход',
    background=config['btn_color_1'],
    activebackground=config['btn_color_2'],
    width='22',
    padx='0',
    pady='0',
    font=('Times Roman', 12, 'bold'),
    command=lambda: Login()
)

btn_15 = Button(
    text='Change',
    background=config['btn_color_1'],
    activebackground=config['btn_color_2'],
    width='22',
    padx='0',
    pady='0',
    font=('Times Roman', 12, 'bold'),
    command=lambda: handleChangePassword()
)

def handleChangePassword():
    pass


btn_16 = Button(
    text='Выход',
    background='#00CED1',
    activebackground='#00CED1',
    width='22',
    padx='0',
    pady='0',
    font=('Times Roman', 12, 'bold'),
    command=lambda: Login()
)

btn_17 = Button(
    text='правила',
    background='#EE82EE',
    activebackground='#EE82EE',
    width='22',
    padx='0',
    pady='0',
    font=('Times Roman', 12, 'bold'),
)

btn_18 = Button(
    text='создать',
    background='#00CED1',
    activebackground='#00CED1',
    width='22',
    padx='0',
    pady='0',
    font=('Times Roman', 12, 'bold'),
)

btn_19 = Button(
    text='выход',
    background='#00CED1',
    activebackground='#00CED1',
    width='22',
    padx='0',
    pady='0',
    font=('Times Roman', 12, 'bold'),
)

btn_20 = Button(
    text='сохранить',
    background='#00CED1',
    activebackground='#00CED1',
    width='22',
    padx='0',
    pady='0',
    font=('Times Roman', 12, 'bold'),
)

btn_21 = Button(
    text='выход',
    background='#00CED1',
    activebackground='#00CED1',
    width='22',
    padx='0',
    pady='0',
    font=('Times Roman', 12, 'bold'),
    command=lambda: Login()
)

txt_1 = Entry(window, width=10)

txt_2 = Entry(window, width=10)

txt_3 = Entry(window, width=10)

txt_4 = Entry(window, width=10)

txt_5 = Entry(window, width=10)

txt_6 = Entry(window, width=10)

chk_1 = Checkbutton(text='Заблокировать пользователя',
    background=('#00FF7F'),
    activebackground=('#00FF7F'),
)

chk_2 = Checkbutton(window, text='',                                # правило 1
    background=('#00FF7F'),
    activebackground=('#00FF7F')
)

chk_3 = Checkbutton(window, text='',                                # правило 2
    background=('#00FF7F'),
    activebackground=('#00FF7F')
)

chk_4 = Checkbutton(window, text='',                                # правило 3
    background=('#00FF7F'),
    activebackground=('#00FF7F')
)

chk_5 = Checkbutton(window, text='',                                # правило 4
    background=('#00FF7F'),
    activebackground=('#00FF7F')
)

chk_6 = Checkbutton(window, text='',                                # правило 5
    background=('#00FF7F'),
    activebackground=('#00FF7F')
)

chk_7 = Checkbutton(window, text='',                                # правило 6
    background=('#00FF7F'),
    activebackground=('#00FF7F')
)

lbl_1=Label(text='Введите логин: ',
    background='#00FF7F',
    activebackground='#00FF7F',
    justify=RIGHT,
    font=('Times Roman', 14, 'bold')
)

lbl_2=Label(text='Введите пароль: ',
    background='#00FF7F',
    activebackground='#00FF7F',
    justify=RIGHT,
    font=('Times Roman', 14, 'bold')
)

lbl_3=Label(text='Автор: ',
    background='#00FF7F',
    activebackground='#00FF7F',
    justify=CENTER,
    font=('Times Roman', 16, 'bold'),
    fg='red'
)

lbl_4=Label(text='Задание: ',
    background='#00FF7F',
    activebackground='#00FF7F',
    justify=CENTER,
    font=('Times Roman', 16, 'bold'),
    fg='red'
)

lbl_5=Label(text='студент группы ИВТ-41 \rЛаптандер Александр Михайлович ',
    background='#00FF7F',
    activebackground='#00FF7F',
    justify=LEFT,
    font=('Times Roman', 15),
    fg='black'
)

lbl_6=Label(text='Разработать программу, реализующую \r интерфейсную систему с применением \r механизмов парольной защиты ',
    background='#00FF7F',
    activebackground='#00FF7F',
    justify=CENTER,
    font=('Times Roman', 15),
    fg='black'
)

lbl_7=Label(text='новый пароль: ',
    background='#00FF7F',
    activebackground='#00FF7F',
    justify=CENTER,
    font=('Times Roman', 15),
    fg='black'
)

lbl_8=Label(text='',
    background='#00FF7F',
    activebackground='#00FF7F',
    justify=CENTER,
    font=('Times Roman', 15, 'bold'),
    fg='red'
)

lbl_9=Label(text='имя пользователя:',
    background='#00FF7F',
    activebackground='#00FF7F',
    justify=RIGHT,
    font=('Times Roman', 15),
    fg='black'
)

lbl_10=Label(text='пароль:',
    background='#00FF7F',
    activebackground='#00FF7F',
    justify=RIGHT,
    font=('Times Roman', 15),
    fg='black'
)

lbl_11=Label(
    background='#00FF7F',
    activebackground='#00FF7F',
    justify=RIGHT,
    font=('Times Roman', 10, 'bold'),
    fg='red'
)

lbl_12=Label(text='правило 1:',
    background='#00FF7F',
    activebackground='#00FF7F',
    justify=RIGHT,
    font=('Times Roman', 15),
    fg='black'
)

lbl_13=Label(text='правило 2:',
    background='#00FF7F',
    activebackground='#00FF7F',
    justify=RIGHT,
    font=('Times Roman', 15),
    fg='black'
)

lbl_14=Label(text='правило 3:',
    background='#00FF7F',
    activebackground='#00FF7F',
    justify=RIGHT,
    font=('Times Roman', 15),
    fg='black'
)

lbl_15=Label(text='правило 4:',
    background='#00FF7F',
    activebackground='#00FF7F',
    justify=RIGHT,
    font=('Times Roman', 15),
    fg='black'
)

lbl_16=Label(text='правило 5:',
    background='#00FF7F',
    activebackground='#00FF7F',
    justify=RIGHT,
    font=('Times Roman', 15),
    fg='black'
)

lbl_17=Label(text='правило 6:',
    background='#00FF7F',
    activebackground='#00FF7F',
    justify=RIGHT,
    font=('Times Roman', 15),
    fg='black'
)

authorLabel=Label(text='old password',
    background='#00FF7F',
    activebackground='#00FF7F',
    justify=LEFT,
    font=('Times Roman', 15),
    fg='black'
)

def Login():
    window.geometry('415x255')              
    window.configure(bg = '#00FF7F')                                # задаем цвет окна
    window.title('Вход в систему') 
    lbl_1.place(height=32, width=150, x = 42, y = 50)               # введите логин
    lbl_2.place(height=32, width=170, x = 25, y = 90)               # введите пароль
    txt_2.place(height=24, width=150, x = 200, y = 55)              # форма для заполнения №1
    txt_3.place(height=24, width=150, x = 200, y = 95)              # форма для заполнения №2
    lbl_11.place(height=25, width=300, x = 100, y = 125) 
    btn_13.place(height=32, width=120, x = 150, y = 155)            # войти

def Admin_Mode():
    window.geometry('415x255')              
    window.configure(bg ='#00FF7F')                          
    window.title('Admin Mode') 
    btn_1.place(height=35, width=250, x = 20, y = 20)               # добавить пользователя
    btn_2.place(height=35, width=250, x = 80, y = 80)               # список имен пользователей
    btn_3.place(height=32, width=250, x = 140, y = 140)             # изменить пароль
    btn_4.place(height=32, width=150, x = 20, y = 200)              # о программе
    btn_5.place(height=32, width=150, x = 240, y = 200)             # выход       

def List_of_users():                                                    
    print('HEllO')
    window.geometry('415x255')              
    window.configure(bg = '#00FF7F')                                # задаем цвет окна
    window.title('Добавление пользователя')                         
    txt_1.place(height=30, width=150, x = 10, y = 15)               
    btn_6.place(height=32, width=120, x = 170, y = 15)              # предыдущий
    btn_7.place(height=32, width=110, x = 290, y = 15)              # следующий
    btn_8.place(height=32, width=220, x = 95, y = 90)              # удалить пользователя
    btn_9.place(height=30, width=120, x = 80, y = 150)              # сохранить
    btn_10.place(height=30, width=120, x = 210, y = 150)            # отмена
    btn_11.place(height=30, width=120, x = 145, y = 210)             # правила
    chk_1.place(height=20, width=180, x = 10, y = 50)                 # виджет кнопки
    btn_1.place_forget()
    btn_2.place_forget()
    btn_3.place_forget()
    btn_4.place_forget()
    btn_5.place_forget()

def Author():
    print('HEllO')
    window.geometry('415x255')              
    window.configure(bg = '#00FF7F')           
    window.title('Добавление пользователя')  
    lbl_3.place(height=40, width=400, x = 20, y = 0)                # автор
    lbl_4.place(height=80, width=400, x = 20, y = 70)               # задание
    lbl_5.place(height=50, width=400, x = 30, y = 35)               # студент группы ИВТ-41 \rЛаптандер Александр Михайлович
    lbl_6.place(height=70, width=400, x = 10, y = 125)              # разработать программу, реализующую интерфейсную систему с применением механизмов парольной защиты
    btn_14.place(height=30, width=70, x = 180, y = 210)             # войти
    btn_1.place_forget()
    btn_2.place_forget()
    btn_3.place_forget()
    btn_4.place_forget()
    btn_5.place_forget()

def User():
    window.geometry('415x255')              
    window.configure(bg = '#00FF7F')           
    window.title('Вход пользователя')
    lbl_7.place(height=30, width=150, x = 30, y = 70)               # новый пароль
    txt_4.place(height=25, width=200, x = 190, y = 72)              # форма для текста №1
    btn_15.place(height=25, width=120, x = 150, y = 120)            # изменить
    lbl_8.place(height=25, width=240, x = 80, y = 20)               # имя пользователя
    btn_16.place(height=25, width=120, x = 150, y = 200)

def add_user():
    print('HEllO')
    window.geometry('415x255')              
    window.configure(bg = '#00FF7F')           
    window.title('Добавление пользователя')  
    lbl_9.place(height=25, width=170, x = 35, y = 39)               # имя пользователя
    lbl_10.place(height=25, width=80, x = 130, y = 79)              # пароль
    txt_5.place(height=25, width=160, x = 215, y = 40)              # форма для заполнения имени пользователя
    txt_6.place(height=25, width=160, x = 215, y = 80)              # форма для заполнения пароля
    btn_17.place(height=25, width=100, x = 147, y = 150)            # правила
    btn_18.place(height=25, width=100, x = 90, y = 190)             # создать
    btn_19.place(height=25, width=100, x = 210, y = 190)            # выход
    lbl_11.place(height=25, width=100, x = 150, y = 115)            # статус

def restrictions():
    print('HELLO')
    window.geometry('415x255')              
    window.configure(bg = '#00FF7F')           
    window.title('правила')
    lbl_12.place(height=20, width=100, x = 140, y = 15)              # правило 1
    lbl_13.place(height=20, width=100, x = 140, y = 45)              # правило 2
    lbl_14.place(height=20, width=100, x = 140, y = 75)              # правило 3
    lbl_15.place(height=20, width=100, x = 140, y = 105)              # правило 4
    lbl_16.place(height=20, width=100, x = 140, y = 135)              # правило 5
    lbl_17.place(height=20, width=100, x = 140, y = 165)              # правило 6
    chk_2.place(height=20, width=20, x = 250, y = 17)
    chk_3.place(height=20, width=20, x = 250, y = 47)
    chk_4.place(height=20, width=20, x = 250, y = 77)
    chk_5.place(height=20, width=20, x = 250, y = 107)
    chk_6.place(height=20, width=20, x = 250, y = 137)
    chk_7.place(height=20, width=20, x = 250, y = 167)
    btn_20.place(height=30, width=120, x = 70, y = 205)                 # сохранить
    btn_21.place(height=30, width=120, x = 215, y = 205)                 # выход

def forgetAll():
    btn_1.place_forget()                                            # скрывает
    btn_2.place_forget()
    btn_3.place_forget()
    btn_4.place_forget()
    btn_5.place_forget()
    btn_6.place_forget()
    btn_7.place_forget()
    btn_8.place_forget()
    btn_9.place_forget()
    btn_10.place_forget()
    btn_11.place_forget()
    btn_12.place_forget()
    btn_13.place_forget()
    btn_14.place_forget()
    btn_15.place_forget()
    btn_16.place_forget()
    btn_17.place_forget()
    btn_18.place_forget()
    btn_19.place_forget()
    btn_20.place_forget()
    btn_21.place_forget()
    lbl_1.place_forget()
    lbl_2.place_forget()
    lbl_3.place_forget()
    lbl_4.place_forget()
    lbl_5.place_forget()
    lbl_6.place_forget()
    lbl_7.place_forget()
    lbl_8.place_forget()
    lbl_12.place_forget()
    lbl_13.place_forget()
    lbl_14.place_forget()
    lbl_15.place_forget()
    lbl_16.place_forget()
    lbl_17.place_forget()
    txt_1.place_forget()
    txt_2.place_forget()
    txt_3.place_forget()
    txt_4.place_forget()
    chk_1.place_forget()
    chk_2.place_forget()
    chk_3.place_forget()
    chk_4.place_forget()
    chk_5.place_forget()
    chk_6.place_forget()
    chk_7.place_forget()

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


def change():
    window.geometry('415x255')              
    window.configure(bg = '#00FF7F')           
    window.title('правила')

    psOldLabel.place(height=30, width=150, x = 15, y = 38)    
    psNewLabel.place(height=30, width=150, x = 18, y = 84)   
    psOld.place(height=27, width=200, x = 180, y = 40)  
    psNew.place(height=27, width=200, x = 180, y = 85)  
    changeBtn.place(height=27, width=140, x = 140, y = 155)
    statusLabel.place(height=27, width=140, x = 140, y = 120)
    
# add_user()
#User()
# Author()
# Admin_Mode()
#Login()
#List_of_users()
change()
#restrictions()

mainloop()
