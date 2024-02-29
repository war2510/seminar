import datetime
import os
import zipfile
from pathlib import Path
from tkinter import filedialog


def select_file():
    """Открыть диалоговое окно для выбора файла."""
    filename = filedialog.askopenfilename(
        title="Открыть файл", filetypes=(("All files", "*.*"), ("CSV files", ".csv"))
    )

    return Path(filename) if filename else None


def zip_file(filename, compression_level=9):
    """Архивировать указанный файл."""
    if not filename or not filename.exists():
        print("Файл не существует. Выход.")
        return

    filename_out = filename.with_suffix(".zip")

    with zipfile.ZipFile(
        filename_out,
        mode="w",
        compression=zipfile.ZIP_DEFLATED,
        compresslevel=compression_level,
    ) as zf:
        zf.write(filename, arcname=filename.name)

        for file_info in zf.infolist():
            date = datetime.datetime(*file_info.date_time)
            print(
                f"{file_info.filename}\t{file_info.file_size:,}\t{file_info.compress_size:,}\t"
                f"{file_info.compress_size / file_info.file_size:.2%}\t"
                f"{date.strftime('%H:%M %d.%m.%Y')}\t{os.getcwd()}"
            )


def main():
    filename = select_file()

    if not filename:
        print("Файл не выбран. Выход.")
        return

    zip_file(filename)


if __name__ == "__main__":
    main()
