from tkinter import *
import requests as r
from tkinter import filedialog as fd
from tkinter import messagebox as mb
import pyperclip



def load_file():
    try:
        file = fd.askopenfilename()
        if file:
            answer = r.post("https://file.io", files={"file" : open(file, "rb")})
            if answer.status_code == 200:
                link_file = answer.json()["link"]
                e.delete(0, END)
                e.insert(0, link_file)
                pyperclip.copy(link_file)
            else:
                print("Не удалось связаться с file.io")
    except Exception as exc:
        mb.showerror("Ошибка", f"Ошибка {exc}")



window = Tk()
window.title("Обмен файлами")
window.geometry("300x150")

btn = Button(window, text="Загрузить файл", font=("Arial", 14), command=load_file)
btn.pack(pady=10)

e = Entry(window, font=("Arial", 14))
e.pack(pady=10)

window.mainloop()