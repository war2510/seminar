from tkinter import Tk, Button, Toplevel, Label, Entry, messagebox, Frame
from tkinter import TOP, X, LEFT, RIGHT, BOTTOM, BOTH, YES, Canvas, Scrollbar


phone_book, search_book = [], []
filename1 = "phonebook.txt"
filename2 = "phonebook.csv"
fields = ["Фамилия", "Имя", "Телефон", "Описание"]
button_options = {"padx": 5, "pady": 5, "ipadx": 10, "ipady": 10}


# Чтение справочника из текстового файла/
def read_txt(filename):
    phone_book.clear()
    try:
        with open(filename, "r", encoding="utf-8") as phb:
            for line in phb:
                if line.strip():
                    record = dict(zip(fields, line.strip().split(",")))
                    phone_book.append(record)
    except FileNotFoundError:
        print(f"Файл {filename} не найден.")


# Сохранение справочника в текстовом формате/
def saveCmd(phone_book):
    phone_book = sorted(phone_book, key=lambda x: (x["Фамилия"], x["Имя"]))
    with open(filename1, "w", encoding="utf-8") as phout:
        for record in phone_book:
            s = ",".join(record.values())
            phout.write(f"{s}\n")

    print("Справочник сохранён в текстовом формате")


# Сохранение записи в текстовом формате/
def saveCmdRec(record):
    with open(filename2, "w", encoding="utf-8") as phout:
        phout.write(",".join(fields) + "\n")
        s = ",".join(record.values())
        phout.write(f"{s}\n")

    print("Запись сохранена в формате .CSV")


# Сохранить и закончить работу/
def endCmd():
    saveCmd(phone_book)
    print("Работа завершена")
    exit()


# Добавление абонента в справочник/
def addCmd():
    record = {k: "" for k in fields}
    phone_book.append(record)
    open_edit_contact_form(phone_book[-1])


# Редактирование абонента в справочнике/
def open_edit_contact_form(contact):
    edit_window = Toplevel()
    edit_window.title("Редактировать контакт")

    entries = {}
    for field in fields:
        row = Frame(edit_window)
        label = Label(row, width=15, text=field, anchor="w")
        entry = Entry(row)
        entry.insert(0, contact[field])
        row.pack(side=TOP, fill=X, padx=5, pady=5)
        label.pack(side=LEFT)
        entry.pack(side=RIGHT, expand=YES, fill=X)
        entries[field] = entry

    def save_contact():
        # Сохранение изменений контакта
        for field in fields:
            contact[field] = entries[field].get()

        edit_window.destroy()  # Закрываем окно редактирования

    # Кнопка для сохранения изменений
    Button(edit_window, text="Сохранить", command=save_contact).pack(
        side=TOP, **button_options
    )


# Отображение справочника/
def print_contacts(contacts, header_message):
    def editCmd():  # Изменение абонента в справочнике
        id = int(search_entry.get()) - 1
        if id in range(len(contacts)):
            open_edit_contact_form(contacts[id])
            results_window.destroy()
        else:
            print("Нет такого абонента в справочнике")
            messagebox.showinfo("Результат", "Нет такого абонента")
            search_entry.delete(0, "end")

    def delCmd():  # Удаление абонента из справочника
        id = int(search_entry.get()) - 1
        if id in range(len(contacts)):
            phone_book.remove(contacts[id])
            results_window.destroy()
        else:
            print("Нет такого абонента в справочнике")
            messagebox.showinfo("Результат", "Нет такого абонента")
            search_entry.delete(0, "end")

    def saveCmd():  # Сохранение абонента в файле
        id = int(search_entry.get()) - 1
        if id in range(len(contacts)):
            saveCmdRec(contacts[id])
            results_window.destroy()
        else:
            print("Нет такого абонента в справочнике")
            messagebox.showinfo("Результат", "Нет такого абонента")
            search_entry.delete(0, "end")

    # Создание основного окна для отображения контактов
    results_window = Toplevel()
    results_window.title("Справочник абонентов")

    # Верхняя непрокручиваемая область для заголовка и шапки таблицы
    header_frame = Frame(results_window)
    header_frame.pack(side=TOP, fill=X)
    Label(
        header_frame, text=f"\n{header_message}\n", font=("Courier", 12, "bold")
    ).pack(side=TOP, anchor="w", fill=X)
    Label(
        header_frame,
        text=" ID | {:<15} | {:<15} | {:<10} | {:<25}".format(*fields)
        + f"\n{'-' * 80}",
        font=("Courier", 10, "bold"),
    ).pack(side=LEFT, anchor="w", fill=X)

    # Нижняя непрокручиваемая область для ввода ID и кнопок
    action_frame = Frame(results_window)
    action_frame.pack(side=BOTTOM, fill=X)
    Label(action_frame, text=" Введите ID записи:", font=("Courier", 10, "bold")).pack(
        side=LEFT
    )
    search_entry = Entry(action_frame, width=10)
    search_entry.pack(side=LEFT, **button_options)
    Button(action_frame, text="Изменить", command=editCmd).pack(
        side=LEFT, **button_options
    )
    Button(action_frame, text="Скопировать", command=saveCmd).pack(
        side=LEFT, **button_options
    )
    Button(action_frame, text="Удалить", command=delCmd).pack(
        side=LEFT, **button_options
    )

    # Прокручиваемая область для контактов
    canvas = Canvas(results_window)
    scrollbar = Scrollbar(results_window, orient="vertical", command=canvas.yview)
    scrollable_frame = Frame(canvas)
    canvas.configure(yscrollcommand=scrollbar.set)
    canvas.create_window((0, 0), window=scrollable_frame, anchor="nw")
    canvas.pack(side=LEFT, fill=BOTH, expand=True)
    scrollbar.pack(side=RIGHT, fill="y")
    canvas.bind(
        "<Configure>", lambda e: canvas.configure(scrollregion=canvas.bbox("all"))
    )

    # Добавление контактов в прокручиваемую область
    for i, record in enumerate(contacts, start=1):
        Label(
            scrollable_frame,
            text=" {:<3}| {:<15} | {:<15} | {:<10} | {:<25}".format(
                i, *record.values()
            ),
            font=("Courier", 10),
        ).pack(anchor="w")


# Найти и изменить/удалить абонента (find_contact, print_contacts, open_edit_contact_form)/
def searchCmdChu():
    def find_contact(search_value, search_field):
        search_book.clear()
        search_window.destroy()
        for record in phone_book:
            if search_value.lower() in record[search_field].lower():
                search_book.append(record)
        print_contacts(
            search_book, f"Результаты поиска {search_field} содержит {search_value}"
        )

    search_window = Toplevel()
    search_window.title("Поиск абонента")
    Label(
        search_window,
        text="\nВведите значение для поиска\nи нажмите соответствующую кнопку\n",
        font=("Courier", 12),
    ).pack(side=TOP, anchor="w", fill=X)
    search_entry = Entry(search_window, width=30)
    search_entry.pack(side=TOP, **button_options)
    for i, field in enumerate(fields):
        Button(
            search_window,
            text=field,
            command=lambda f=field: find_contact(search_entry.get(), f),
        ).pack(side=LEFT, **button_options)


# Главное меню/
def mainMenu():
    read_txt(filename1)  # Инициализация данных справочника

    root = Tk()
    root.title("My phone book")
    # Создание и размещение кнопок
    Button(
        root,
        text="Отобразить весь справочник",
        width=40,
        command=lambda f="Справочник абонентов": print_contacts(phone_book, f),
    ).pack(side=TOP, **button_options)
    Button(
        root,
        text="Найти и изменить/удалить абонента",
        width=40,
        command=searchCmdChu,
    ).pack(side=TOP, **button_options)
    Button(
        root,
        text="Добавить абонента в справочник",
        width=40,
        command=addCmd,
    ).pack(side=TOP, **button_options)
    Button(
        root,
        text="Сохранить справочник в текстовом формате",
        width=40,
        command=lambda: saveCmd(phone_book),
    ).pack(side=TOP, **button_options)
    Button(
        root, text="Сохранить справочник и завершить работу", width=40, command=endCmd
    ).pack(side=TOP, **button_options)

    root.mainloop()
