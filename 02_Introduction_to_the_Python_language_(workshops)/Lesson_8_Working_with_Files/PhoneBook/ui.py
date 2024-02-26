from tkinter import Tk, Button

phone_book = []  # Глобальная переменная для хранения справочника


def read_txt(filename):
    global phone_book
    phone_book.clear()
    fields = ["Фамилия", "Имя", "Телефон", "Описание"]
    with open(filename, "r", encoding="utf-8") as phb:
        for line in phb:
            record = dict(zip(fields, line.strip().split(",")))
            phone_book.append(record)
    print(phone_book)
    return phone_book


def write_txt(filename, phone_book):
    with open(filename, "w", encoding="utf-8") as phout:
        for record in phone_book:
            s = ",".join(record.values())
            phout.write(f"{s}\n")


def showCmd(event):
    global phone_book
    for record in phone_book:
        print(record)


def findNameCmd(event):
    # Ваш код для поиска по фамилии
    pass


def findNumCmd(event):
    # Ваш код для поиска по номеру телефона
    pass


def addCmd(event):
    # Ваш код для добавления абонента
    pass


def saveCmd(event):
    global phone_book
    write_txt("phonebook.txt", phone_book)
    print("Справочник сохранён в текстовом формате")


def mainMenu():
    # Инициализация данных справочника
    read_txt("phonebook.txt")

    root = Tk()
    # Создание и размещение кнопок
    """
    Использование параметра sticky в методе .grid() для выравнивания внутри сетки.
    Задание параметра padx и pady для добавления внешних отступов между виджетами.
    Задание параметра ipadx и ipady для добавления внутренних отступов внутри виджетов.
    Установка фиксированной ширины для кнопок с помощью параметра width.
    """
    button_options = {"padx": 5, "pady": 5, "sticky": "w", "ipadx": 10, "ipady": 10}
    showBtn = Button(root, text="Отобразить весь справочник", width=40)
    showBtn.grid(row=1, column=0, **button_options)
    findNameBtn = Button(root, text="Найти абонента по фамилии", width=40)
    findNameBtn.grid(row=2, column=0, **button_options)
    findNumBtn = Button(root, text="Найти абонента по номеру телефона", width=40)
    findNumBtn.grid(row=3, column=0, **button_options)
    addBtn = Button(root, text="Добавить абонента в справочник", width=40)
    addBtn.grid(row=4, column=0, **button_options)
    saveBtn = Button(root, text="Сохранить справочник в текстовом формате", width=40)
    saveBtn.grid(row=5, column=0, **button_options)
    exitBtn = Button(root, text="Закончить работу", width=40, command=root.destroy)
    exitBtn.grid(row=6, column=0, **button_options)

    # Привязка обработчиков событий к кнопкам
    showBtn.bind("<Button-1>", showCmd)
    findNameBtn.bind("<Button-1>", findNameCmd)
    findNumBtn.bind("<Button-1>", findNumCmd)
    addBtn.bind("<Button-1>", addCmd)
    saveBtn.bind("<Button-1>", saveCmd)

    root.mainloop()
