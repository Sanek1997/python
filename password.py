from cProfile import label
from tkinter import*
from turtle import clear

config = {
    'btn_color_1': '#FA8072',                           # Цвет кнопок в обычном состоянии (добавить пользователя, Список имен пользователей, Изменить пароль)
    'btn_color_2': '#FA8072',                           # Цвет кнопок в наведенном состоянии (добавить пользователя, Список имен пользователей, Изменить пароль)
    'btn_color_3': '#AFEEEE'                            # Цвет кнопок в обычном состоянии ()
}

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
    font=('Times Roman', 12, 'bold')
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
    font=('Times Roman', 12, 'bold')
)

btn_11 = Button(
    text='Ограничения на пароль',
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
    font=('Times Roman', 12, 'bold')
)

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
    text='Изменить',
    background=config['btn_color_1'],
    activebackground=config['btn_color_2'],
    width='22',
    padx='0',
    pady='0',
    font=('Times Roman', 12, 'bold'),
)

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

txt_1 = Entry(window, width=10)

txt_2 = Entry(window, width=10)

txt_3 = Entry(window, width=10)

txt_4 = Entry(window, width=10)

txt_5 = Entry(window, width=10)

txt_6 = Entry(window, width=10)

chk = Checkbutton(window, text='Заблокировать пользователя',
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

lbl_8=Label(text='имя пользователя: ',
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


def Login():
    window.geometry('415x255')              
    window.configure(bg = '#00FF7F')                                # задаем цвет окна
    window.title('Вход в систему') 
    lbl_1.place(height=32, width=150, x = 42, y = 50)               # введите логин
    lbl_2.place(height=32, width=170, x = 25, y = 90)               # введите пароль
    txt_2.place(height=24, width=150, x = 200, y = 55)              # форма для заполнения №1
    txt_3.place(height=24, width=150, x = 200, y = 95)              # форма для заполнения №2
    btn_13.place(height=32, width=120, x = 150, y = 155)            # войти
    btn_1.place_forget()                                            # скрывает
    btn_2.place_forget()
    btn_3.place_forget()
    btn_4.place_forget()
    btn_5.place_forget()
    lbl_3.place_forget()
    lbl_4.place_forget()
    lbl_5.place_forget()
    lbl_6.place_forget()
    btn_14.place_forget()
    lbl_7.place_forget()
    txt_4.place_forget()
    btn_15.place_forget()
    lbl_8.place_forget()
    btn_16.place_forget()

def Admin_Mode():
    window.geometry('415x255')              
    window.configure(bg ='#00FF7F')                          
    window.title('Admin Mode') 
    btn_1.place(height=35, width=250, x = 20, y = 20)               # добавить пользователя
    btn_2.place(height=35, width=250, x = 80, y = 80)               # список имен пользователей
    btn_3.place(height=32, width=250, x = 140, y = 140)             # изменить пароль
    btn_4.place(height=32, width=150, x = 20, y = 200)              # о программе
    btn_5.place(height=32, width=150, x = 240, y = 200)             # выход       

def Add_user():                                                    
    print('HEllO')
    window.geometry('415x255')              
    window.configure(bg = '#00FF7F')                                # задаем цвет окна
    window.title('Добавление пользователя')                         
    txt_1.place(height=30, width=150, x = 10, y = 15)               
    btn_6.place(height=32, width=120, x = 170, y = 15)              # предыдущий
    btn_7.place(height=32, width=110, x = 290, y = 15)              # следующий
    btn_8.place(height=32, width=220, x = 95, y = 150)              # удалить пользователя
    btn_9.place(height=30, width=120, x = 80, y = 210)              # сохранить
    btn_10.place(height=30, width=120, x = 210, y = 210)            # отмена
    btn_11.place(height=30, width=230, x = 90, y = 90)              # ограничения на пароль
    chk.place(height=20, width=180, x = 10, y = 50)                 # виджет кнопки

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

def user():
    print('HEllO')
    window.geometry('415x255')              
    window.configure(bg = '#00FF7F')           
    window.title('Вход пользователя')
    lbl_7.place(height=30, width=150, x = 30, y = 70)               # новый пароль
    txt_4.place(height=25, width=200, x = 160, y = 72)              # форма для текста №1
    btn_15.place(height=25, width=120, x = 150, y = 120)            # изменить
    lbl_8.place(height=25, width=240, x = 80, y = 20)               # имя пользователя
    btn_16.place(height=25, width=120, x = 150, y = 200)

def add_user():
    print('HEllO')
    window.geometry('415x255')              
    window.configure(bg = '#00FF7F')           
    window.title('Добавление пользователя')  
    lbl_9.place(height=25, width=200, x = 10, y = 20)
    lbl_10.place(height=25, width=250, x = 10, y = 50)
    txt_5.place(height=25, width=300, x = 80, y = 20)
    txt_6.place(height=25, width=300, x = 20, y = 50)
#add_user()
user()
#Author()
#Admin_Mode()
#Input()
#Add_user()

mainloop()
