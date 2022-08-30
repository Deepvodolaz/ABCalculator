# А/В калькулятор

import tkinter as tk

# Функция закрытия программы
def do_close():
    root.destroy()
    
def do_processing():
    # Считывание данных из полей ввода
    n1 = int(entVisitors1.get())
    c1 = int(entConversions1.get())
    n2 = int(entVisitors2.get())
    c2 = int(entConversions2.get())
    
    popup_window(n1, c1, n2, c2)
    
def popup_window(n1, c1, n2, c2):
    window = tk.Toplevel()
    window.geometry("280x300")
    window.title("A/B результат")
    
    # Добавление кнопки закрытия окна
    btnClosePopup = tk.Button(window, text="Закрыть", font = ('Helvetika', 10, 'bold'), command=window.destroy)
    btnClosePopup.place(x=160, y=250, width=90, height=30)
    
    # Перевод фокуса на созданное окно
    window.focus_force()
    

# Создание главного окна
root = tk.Tk()
root.geometry("280x300")
root.title("А/В калькулятор")

# Добавление метки заголовка
lblTitle = tk.Label(text = "А/В калькулятор", font = ('Helvetika', 16, 'bold'), fg = '#0000cc')
lblTitle.place(x=55, y=20)

# Добавление метки подзаголовка Контрольная группа
lblTitle1 = tk.Label(text = "Контрольная группа", font = ('Helvetika', 12, 'bold'), fg = '#0066ff')
lblTitle1.place(x=25, y=55)

# Добавление полей ввода Контрольной группы
lblVisitors1 = tk.Label(text = "Посетители:", font = ('Helvetika', 10, 'bold'))
lblVisitors1.place(x=25, y=85)

entVisitors1 = tk.Entry(font = ('Helvetika', 10, 'bold'), justify='center')
entVisitors1.place(x=115, y=85, width=90, height=20)
entVisitors1.insert(tk.END, '0')

lblConversions1 = tk.Label(text = "Конверсии:", font = ('Helvetika', 10, 'bold'))
lblConversions1.place(x=25, y=115)

entConversions1 = tk.Entry(font = ('Helvetika', 10, 'bold'), justify='center')
entConversions1.place(x=115, y=115, width=90, height=20)
entConversions1.insert(tk.END, '0')

# Добавление метки подзаголовка Тестовая группа
lblTitle2 = tk.Label(text = "Тестовая группа", font = ('Helvetika', 12, 'bold'), fg = '#008800')
lblTitle2.place(x=25, y=145)

# Добавление полей ввода Тестовой группы
lblVisitors2 = tk.Label(text = "Посетители:", font = ('Helvetika', 10, 'bold'))
lblVisitors2.place(x=25, y=175)

entVisitors2 = tk.Entry(font = ('Helvetika', 10, 'bold'), justify='center')
entVisitors2.place(x=115, y=175, width=90, height=20)
entVisitors2.insert(tk.END, '0')

lblConversions2 = tk.Label(text = "Конверсии:", font = ('Helvetika', 10, 'bold'))
lblConversions2.place(x=25, y=205)

entConversions2 = tk.Entry(font = ('Helvetika', 10, 'bold'), justify='center')
entConversions2.place(x=115, y=205, width=90, height=20)
entConversions2.insert(tk.END, '0')



# Добавление кнопки "Рассчитать"
btnChart1 = tk.Button(root, text="Рассчитать", font = ('Helvetika', 10, 'bold'), command=do_processing)
btnChart1.place(x=25, y=250, width=90, height=30)

# Добавление кнопки закрытия программы
btnChart2 = tk.Button(root, text="Закрыть", font = ('Helvetika', 10, 'bold'), command=do_close)
btnChart2.place(x=160, y=250, width=90, height=30)

# Запуск цикла mainloop
root.mainloop()
