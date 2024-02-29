from tkinter import Tk, Button, Entry, Label, messagebox, END, Listbox, W, E, N, S

phone_book, search_book = [], []
filename = "phonebook.txt"
fields = ["Фамилия", "Имя", "Телефон", "Описание"]


# Функция для чтения данных из файла
def loadData():
    try:
        with open(filename, "r") as file:
            lines = file.readlines()
        return [line.strip().split(",") for line in lines]
    except FileNotFoundError:
        messagebox.showerror("Ошибка", "Файл данных не найден.")
        return []


# Функция для сохранения данных в файл
def saveData(data):
    try:
        with open(filename, "w") as file:
            for record in data:
                file.write(",".join(record) + "\n")
        messagebox.showinfo("Сохранение", "Данные успешно сохранены.")
    except Exception as e:
        messagebox.showerror("Ошибка при сохранении", str(e))


# Функция для удаления абонента по ID
def delete_contact_by_id(contact_id):
    if 0 <= contact_id < len(phone_book):
        del phone_book[contact_id]
        messagebox.showinfo("Успех", "Запись удалена.")
        # saveData(phone_book)
    else:
        messagebox.showerror("Ошибка", "Неверный ID.")


# Функция для редактирования абонента по ID
def edit_contact_by_id(contact_id, new_data):
    if 0 <= contact_id < len(phone_book):
        phone_book[contact_id] = new_data
        messagebox.showinfo("Успех", "Запись обновлена.")
        # saveData(phone_book)
    else:
        messagebox.showerror("Ошибка", "Неверный ID.")


# Функция для добавления нового абонента
def addSubscriber(data, name, phone):
    for record in data:
        if record[0] == name:
            messagebox.showwarning("Внимание", "Абонент уже существует.")
            return
    data.append([name, phone])
    # saveData(phone_book)


def refresh():
    # Очистка списка контактов в GUI
    contacts_listbox.delete(0, "end")

    # Перезагрузка списка контактов из `phone_book`
    for index, contact in enumerate(phone_book):
        contacts_listbox.insert(index, f"{contact['Имя']}: {contact['Телефон']}")

    # Обновление списка контактов может также включать сохранение изменений в файл
    # saveData(phone_book)


# Функция для удаления абонента
def on_delete():
    contact_id = (
        int(delete_entry.get()) - 1
    )  # Получаем ID и корректируем его для использования в списке
    delete_contact_by_id(contact_id)
    refresh()  # Обновляем список контактов в GUI


# Функция для редактирования абонента
def on_edit():
    contact_id = int(edit_id_entry.get()) - 1  # ID для редактирования
    new_name = edit_name_entry.get()
    new_phone = edit_phone_entry.get()
    edit_contact_by_id(contact_id, {"Имя": new_name, "Телефон": new_phone})
    refresh()  # Обновляем список контактов в GUI


# Функция для поиска абонента
def searchSubscriber(data, name):
    for record in data:
        if record[0] == name:
            return record
    messagebox.showinfo("Результат поиска", "Абонент не найден.")
    return None


# Функция для изменения данных абонента
def modifySubscriber(data, name, new_phone):
    for record in data:
        if record[0] == name:
            record[1] = new_phone
            saveData(data)
            return
    messagebox.showinfo("Изменение данных", "Абонент не найден.")


# Основная функция GUI
def mainGUI():
    def refresh():
        entries = loadData()
        listbox.delete(0, END)
        for entry in entries:
            listbox.insert(END, entry[0] + " - " + entry[1])

    def addCmd():
        addSubscriber(loadData(), name_entry.get(), phone_entry.get())
        refresh()

    def searchCmd():
        result = searchSubscriber(loadData(), search_entry.get())
        if result:
            messagebox.showinfo(
                "Результат поиска", "Имя: " + result[0] + "\nТелефон: " + result[1]
            )

    def modifyCmd():
        modifySubscriber(loadData(), name_entry.get(), phone_entry.get())
        refresh()

    window = Tk()
    window.title("Телефонная книга")

    Label(window, text="Имя:").grid(row=0, column=0)
    name_entry = Entry(window)
    name_entry.grid(row=0, column=1)

    Label(window, text="Телефон:").grid(row=1, column=0)
    phone_entry = Entry(window)
    phone_entry.grid(row=1, column=1)

    Button(window, text="Добавить", command=addCmd).grid(row=2, column=0)
    Button(window, text="Изменить", command=modifyCmd).grid(row=2, column=1)

    Label(window, text="Поиск:").grid(row=3, column=0)
    search_entry = Entry(window)
    search_entry.grid(row=3, column=1)
    Button(window, text="Найти", command=searchCmd).grid(row=3, column=2)

    listbox = Listbox(window)
    listbox.grid(row=4, column=0, columnspan=2, sticky=W + E + N + S)

    delete_entry = Entry(window)
    delete_entry.grid(row=5, column=1)
    Button(window, text="Удалить по ID", command=on_delete).grid(row=5, column=2)

    edit_id_entry = Entry(window)
    edit_id_entry.grid(row=6, column=0)
    edit_name_entry = Entry(window)
    edit_name_entry.grid(row=6, column=1)
    edit_phone_entry = Entry(window)
    edit_phone_entry.grid(row=6, column=2)
    Button(window, text="Редактировать по ID", command=on_edit).grid(row=7, column=1)
    refresh()

    window.mainloop()


if __name__ == "__main__":
    mainGUI()
