from tkinter import Tk, Button, Entry, Label, Toplevel, messagebox, Text, Scrollbar, END


phone_book = []  # Глобальная переменная для хранения справочника
button_options = {"padx": 5, "pady": 5, "sticky": "w", "ipadx": 10, "ipady": 10}
fields = ["Фамилия", "Имя", "Телефон", "Описание"]


def read_txt(filename):
    # global phone_book
    phone_book.clear()

    with open(filename, "r", encoding="utf-8") as phb:
        for line in phb:
            if len(line.strip()) == 0:
                continue
            record = dict(zip(fields, line.strip().split(",")))
            phone_book.append(record)
    return phone_book


def showDict(dictionary):
    show_window = Toplevel()
    show_window.title("Просмотр справочника")
    text_area = Text(show_window, wrap="none")
    scrollbar = Scrollbar(show_window, command=text_area.yview)
    text_area.configure(yscrollcommand=scrollbar.set)
    scrollbar.pack(side="right", fill="y")
    text_area.pack(expand=True, fill="both")

    text_area.insert(END, "{:<15} {:<15} {:<15} {:<15}\n".format(*fields))
    text_area.insert(END, "-" * 60 + "\n")

    for record in dictionary:
        text_area.insert(END, "{:<15} {:<15} {:<15} {:<15}\n".format(*record.values()))

    text_area.config(state="disabled")


def searchCmd(search_field):
    search_window = Toplevel()
    search_window.title(f"Поиск по {search_field}")
    Label(search_window, text=f"Введите {search_field.lower()}:").grid(
        row=0, column=0, **button_options
    )
    search_entry = Entry(search_window, width=30)
    search_entry.grid(row=0, column=1, **button_options)

    def on_search():
        search_term = search_entry.get().lower()
        filtered_records = [
            record
            for record in phone_book
            if search_term in record[search_field].lower()
        ]
        if filtered_records:
            showDict(filtered_records)
        else:
            messagebox.showinfo("Результат", "Записи не найдены")

    Button(search_window, text="Поиск", command=on_search).grid(
        row=1, column=0, columnspan=2, **button_options
    )


def addCmd():
    def save_new_contact():
        record = {
            "Фамилия": surname_entry.get(),
            "Имя": name_entry.get(),
            "Телефон": phone_entry.get(),
            "Описание": description_entry.get(),
        }
        phone_book.append(record)
        # Очищаем поля ввода
        surname_entry.delete(0, "end")
        name_entry.delete(0, "end")
        phone_entry.delete(0, "end")
        description_entry.delete(0, "end")
        # Показываем сообщение об успехе
        messagebox.showinfo("Успешно", "Новый абонент добавлен")

    new_contact_window = Toplevel()  # Используем Toplevel вместо Tk
    new_contact_window.title("Добавить абонента")

    # Создание и размещение меток и полей ввода
    Label(new_contact_window, text="Фамилия").grid(row=0, column=0, **button_options)
    surname_entry = Entry(new_contact_window, width=30)
    surname_entry.grid(row=0, column=1, **button_options)

    Label(new_contact_window, text="Имя").grid(row=1, column=0, **button_options)
    name_entry = Entry(new_contact_window, width=30)
    name_entry.grid(row=1, column=1, **button_options)

    Label(new_contact_window, text="Телефон").grid(row=2, column=0, **button_options)
    phone_entry = Entry(new_contact_window, width=30)
    phone_entry.grid(row=2, column=1, **button_options)

    Label(new_contact_window, text="Описание").grid(row=3, column=0, **button_options)
    description_entry = Entry(new_contact_window, width=30)
    description_entry.grid(row=3, column=1, **button_options)

    # Кнопка для сохранения нового абонента
    Button(new_contact_window, text="Сохранить", command=save_new_contact).grid(
        row=4, column=0, columnspan=2, padx=5, pady=5
    )


def saveCmd():
    global phone_book
    phone_book = sorted(phone_book, key=lambda x: x["Фамилия"])
    with open("phonebook.txt", "w", encoding="utf-8") as phout:
        for record in phone_book:
            s = ",".join(record.values())
            phout.write(f"{s}\n")
    print("Справочник сохранён в текстовом формате")


def endCmd():
    saveCmd()
    print("Работа завершена")
    exit()


def mainMenu():
    # Инициализация данных справочника
    read_txt("phonebook.txt")

    root = Tk()
    root.title("My phone book")
    # Создание и размещение кнопок
    Button(
        root,
        text="Отобразить весь справочник",
        width=40,
        command=lambda: showDict(phone_book),
    ).grid(row=1, column=0, **button_options)
    Button(
        root,
        text="Найти абонента по фамилии",
        width=40,
        command=lambda: searchCmd("Фамилия"),
    ).grid(row=2, column=0, **button_options)
    Button(
        root,
        text="Найти абонента по номеру телефона",
        width=40,
        command=lambda: searchCmd("Телефон"),
    ).grid(row=3, column=0, **button_options)
    Button(
        root,
        text="Добавить абонента в справочник",
        width=40,
        command=addCmd,
    ).grid(row=4, column=0, **button_options)
    Button(
        root,
        text="Сохранить справочник в текстовом формате",
        width=40,
        command=saveCmd,
    ).grid(row=5, column=0, **button_options)
    Button(root, text="Сохранить и закончить работу", width=40, command=endCmd).grid(
        row=6, column=0, **button_options
    )

    root.mainloop()
