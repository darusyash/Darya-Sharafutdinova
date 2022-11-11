# Библиотеки и пакеты
from tkinter import *  # Графический пакет
import random  # Генерация случайных комбинаций

# Вызов генератора паролей
def Click():
    n = r_z.get()  # Результат радиокнопки
    global p, l_g, btn_g  # Глобальные переменные генерации пароля, вывода пароля и копирования пароля 
    # Вызов генератора 0-ого уровня
    if n == 1:
        p = Gener_0()
        l_g = Label(root, text=p, font=("Times New Roman", 15))
        l_g.grid(column=0, row=10, columnspan=2)
        btn_g = Button(root, text='Копировать', font=("Times New Roman", 15), command=Copier)
        btn_g.grid(column=0, row=11, columnspan=2)
    # Вызов генератора 1-ого уровня
    elif n == 2:
        p = Gener_1()
        l_g = Label (root, text=p, font=("Times New Roman", 15))
        l_g.grid(column=0, row=10, columnspan=2)
        btn_g = Button(root, text='Копировать', font=("Times New Roman", 15), command=Copier)
        btn_g.grid(column=0, row=11, columnspan=2)
    # Вызов генератора 2-ого уровня
    elif n == 3:
        p = Gener_2()
        l_g = Label (root, text=p, font=("Times New Roman", 15))
        l_g.grid(column=0, row=10, columnspan=2)
        btn_g = Button(root, text='Копировать', font=("Times New Roman", 15), command=Copier)
        btn_g.grid(column=0, row=11, columnspan=2)
    # Вызов генератора 3-ого уровня
    elif n == 4:
        p = Gener_3()
        l_g = Label (root, text=p, font=("Times New Roman", 15))
        l_g.grid(column=0, row=10, columnspan=2)
        btn_g = Button(root, text='Копировать', font=("Times New Roman", 15), command=Copier)
        btn_g.grid(column=0, row=11, columnspan=2)

# Перемещивание пароля с биграммами
def Shuffler_1(bigramm, pw):
    for word in bigramm:
        if word.lower() in pw.lower():
            l_pw = []  # Перевод строки в список символов
            for sim in pw:
                l_pw.append(sim)
            random.shuffle(l_pw)  # Перемешивание списка
            pw=''  # Перевод списка в строку
            for sim in l_pw:
                pw += sim
    return(pw)

# Перемещивание пароля с триграммами
def Shuffler_2(trigramm, pw):
    for word in trigramm:
        if word.lower() in pw.lower():
            l_pw = []  # Перевод строки в список символов
            for sim in pw:
                l_pw.append(sim)
            random.shuffle(l_pw)  # Перемешивание списка
            pw=''  # Перевод списка в строку
            for sim in l_pw:
                pw += sim
    return(pw)

# Копирование пароля
def Copier():
    global p    # Глобальная переменная генерации пароля
    root.clipboard_clear()  # Очистка буфера обмена
    root.clipboard_append(p)  # Добавление пароля в буфер обмена
    Cleaner()

# Очистка пароля
def Cleaner():
    global l_g, btn_g  # Глобальные переменные вывода пароля и копирования пароля
    l_g.destroy()  # Удаление сгенерироваанного пароля из окна
    btn_g.destroy()  # Удаление кнопки копирования из окна

# Генератор паролей 0-ого уровня    
def Gener_0():
    d = dl.get()
    sim = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklnopqrstuvwxyz'
    pw = ''
    for i in range(d):
        pw += random.choice(sim)
    return(pw)

# Генератор паролей 1-ого уровня 
def Gener_1():
    d = dl.get()
    sim = 'BCDFGJKLMPQUVWXYZbcdfgjklpquvwxyz'
    pw =''
    for i in range(d):
        pw += random.choice(sim)
    return(pw)

# Генератор паролей 2-ого уровня 
def Gener_2():
    d = dl.get()
    sim = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklnopqrstuvwxyz'
    bigramm = ['ED', 'HA', 'HE', 'AN', 'AT', 'EN',  'ER', 'ES', 'IN', 'IT', 'ND', 'NG', 'RE', 'TH', 'TI', 'NT', 'ON', 'ST']
    pw =''
    for i in range(d):
        pw += random.choice(sim)
    pw = Shuffler_1(bigramm, pw)   
    return(pw)

# Генератор паролей 3-ого уровня
def Gener_3():
    d = dl.get()
    sim = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklnopqrstuvwxyz'
    trigramm = ['THE', 'AND', 'ING', 'HER', 'THA', 'ERE', 'HAT', 'ETH', 'ENT', 'NTH', 'FOR', 'HIS', 'THI', 'TER', 'INT', 'DTH', 'YOU', 'ALL', 'HES', 'ION', 'ITH', 'OTH', 'EST', 'TTH', 'OFT', 'VER', 'STH', 'ERS', 'FTH', 'REA', 'WAS']
    pw =''
    for i in range(d):
        pw += random.choice(sim)
    pw = Shuffler_2(trigramm, pw) 
    return(pw)

# Окно    
root = Tk()  # Создание окна программы
root.title ('Генератор паролей')  # Название окна программы
root.geometry('500x320')  # Размер окна программы

# Специальные классы-переменные пакета Tkinter
r_z = IntVar()
dl = IntVar()
p = StringVar()

# Тело программы
l_1 = Label (root, text ='Добро пожаловать в генератор паролей!', font=("Times New Roman", 20), padx=15)
l_1.grid(column=0, row=0, columnspan=2)
l_2 = Label (root, text ='Здесь можно создать защищённый и сложный пароль', font=("Times New Roman", 15))
l_2.grid(column=0, row=1, columnspan=2)
l_3 = Label (root, text ='Выберите уровень защиты пароля:', font=("Times New Roman", 10))
l_3.grid(column=0, row=2, columnspan=2)
r_1 = Radiobutton (root, text='0-все символы', font=("Times New Roman", 10), variable=r_z, value=1)
r_1.grid(column=0, row=3, columnspan=2)
r_2 = Radiobutton (root, text='1-исключение популярных символов', font=("Times New Roman", 10), variable=r_z, value=2) 
r_2.grid(column=0, row=4, columnspan=2)
r_3 = Radiobutton (root, text='2-исключение популярных биграмм', font=("Times New Roman", 10), variable=r_z, value=3)
r_3.grid(column=0, row=5, columnspan=2)
r_4 = Radiobutton (root, text='3-исключение популярных триграмм', font=("Times New Roman", 10), variable=r_z, value=4)
r_4.grid(column=0, row=6, columnspan=2)
l_5 = Label(root, text ='Введите длину пароля', font=("Times New Roman", 10))
l_5.grid(column=0, row=7, stick='e')
ent = Entry(root, width=20, textvariable=dl, font=("Times New Roman", 10), justify=CENTER)
ent.grid(column=1, row=7, stick='w')
ent.delete(0, END)
btn = Button(root, text ='Сгенерировать', font=("Times New Roman", 15), command=Click)
btn.grid(column=0, row=8, columnspan=2)
root.mainloop()
