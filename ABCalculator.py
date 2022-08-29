# А/В калькулятор

import tkinter as tk

# Создание главного окна
root = tk.Tk()
root.geometry("280x300")
root.title("А/В калькулятор")

# Функция закрытия программы
def do_close():
    root.destroy()

# Добавление метки заголовка
lblTitle = tk.Label(text = "А/В калькулятор", font = ('Helvetika', 16, 'bold'), fg = '#0000cc')
lblTitle.place(x=55, y=20)

# Добавление кнопки "Рассчитать"
btnChart1 = tk.Button(root, text="Рассчитать", font = ('Helvetika', 10, 'bold'))
btnChart1.place(x=25, y=250, width=90, height=30)

# Добавление кнопки закрытия программы
btnChart2 = tk.Button(root, text="Закрыть", font = ('Helvetika', 10, 'bold'), command=do_close)
btnChart2.place(x=160, y=250, width=90, height=30)

# Запуск цикла mainloop
root.mainloop()
