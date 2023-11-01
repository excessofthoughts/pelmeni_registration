import tkinter as tk
from tkinter import ttk

def image_block():
    new_win = tk.Toplevel(win)
    new_label = tk.Label(new_win, image=picture)
    new_label.pack()
    new_win.title('Вы заказали пельмени')
    new_win.minsize(650, 680)
    new_win.maxsize(650, 680)

def widget_stop():
    if gender_var.get() == 1:
        submit.config(state=tk.NORMAL)
        country.config(state=tk.NORMAL)
        check.config(state=tk.NORMAL)
    elif gender_var.get() == 2:
        submit.config(state=tk.NORMAL)
        country.config(state=tk.NORMAL)
        check.config(state=tk.NORMAL)
    elif gender_var.get() == 3:
        submit.config(state=tk.NORMAL)
        country.config(state=tk.NORMAL)
        check.config(state=tk.NORMAL)
    else:
        submit.config(state=tk.DISABLED)
        country.config(state=tk.DISABLED)
        check.config(state=tk.DISABLED)


win = tk.Tk()
win.title('Регистрация')
win.minsize(350, 300)
win.maxsize(400, 450)
win.config(bg='white')

gender_var = tk.IntVar()
permission = tk.BooleanVar()

label1 = tk.Label(win, text='Зарегистрироваться', bg='white', fg='black', font=('Arial', 20, 'bold'))
name = tk.Label(win, text='Имя:', bg='white', fg='black', font=('Arial', 16, 'bold'))
entry1 = tk.Entry(win, bg='white', fg='black')
surname = tk.Label(win, text='Фамилия:', bg='white', fg='black', font=('Arial', 16, 'bold'))
entry2 = tk.Entry(win, bg='white', fg='black')

gender = tk.Label(win, text='Пол(не паркет!):', bg='white', fg='black', font=('Arial', 16, 'bold'))
female = ttk.Radiobutton(win, text='Женский', variable=gender_var, value=1, command=widget_stop)
male = ttk.Radiobutton(win, text='Мужской', variable=gender_var, value=2, command=widget_stop)
floor = ttk.Radiobutton(win, text='Ламинат', variable=gender_var, value=3, command=widget_stop)
floor2 = ttk.Radiobutton(win, text='Паркет', variable=gender_var, value=4, command=widget_stop)

country_label = tk.Label(win, text='Выберите страну:', bg='white', fg='black', font=('Arial', 16, 'bold'))
country = ttk.Combobox(win, values=['Китай', 'Россия', 'Туркменистан', 'Великобритания', 'Италия', 'Канада', 'Аргентина', 'Уругвай', 'Мадагаскар', 'Сингапур', 'Казахстан', 'Индия'])

check = tk.Checkbutton(win, text='Я согласен с условиями доставки пельменей.', variable=permission, command=widget_stop)
check_label = tk.Label(win, text='')

picture = tk.PhotoImage(file='pelmeshechki2.png')
submit = tk.Button(win, text='Заказать пельмени', command=image_block)

label1.pack()
name.place(x=0, y=40)
entry1.place(x=90, y=40)
surname.place(x=0, y=70)
entry2.place(x=90, y=70)
gender.place(x=0, y=100)
female.place(x=90, y=130)
male.place(x=180, y=130)
floor.place(x=90, y=160)
floor2.place(x=180, y=160)
country_label.place(x=0, y=190)
country.place(x=90, y=220)
check.place(x=0, y=250)
submit.place(x=90, y=280)
win.mainloop()
