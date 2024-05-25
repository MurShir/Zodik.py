import tkinter as tk
from tkinter import ttk

def get_zodiac_sign(birth_date):

    day, month, year = map(int, birth_date.split('.'))

    if (month == 3 and day >= 21) or (month == 4 and day <= 19):
        return "Овен"
    elif (month == 4 and day >= 20) or (month == 5 and day <= 20):
        return "Телец"
    elif (month == 5 and day >= 21) or (month == 6 and day <= 20):
        return "Близнецы"
    elif (month == 6 and day >= 21) or (month == 7 and day <= 22):
        return "Рак"
    elif (month == 7 and day >= 23) or (month == 8 and day <= 22):
        return "Лев"
    elif (month == 8 and day >= 23) or (month == 9 and day <= 22):
        return "Дева"
    elif (month == 9 and day >= 23) or (month == 10 and day <= 22):
        return "Весы"
    elif (month == 10 and day >= 23) or (month == 11 and day <= 21):
        return "Скорпион"
    elif (month == 11 and day >= 22) or (month == 12 and day <= 21):
        return "Стрелец"
    elif (month == 12 and day >= 22) or (month == 1 and day <= 19):
        return "Козерог"
    elif (month == 1 and day >= 20) or (month == 2 and day <= 18):
        return "Водолей"
    elif (month == 2 and day >= 19) or (month == 3 and day <= 20):
        return "Рыбы"

class ZodiacApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Определение знака зодиака")
        self.geometry("400x300")
        self.configure(bg="black")
        self.attributes("-alpha", 0.8)

        # Создание стиля для виджетов
        self.style = ttk.Style()
        self.style.theme_use("clam")
        self.style.configure("TLabel", background="black", foreground="yellow", font=("Arial", 14))
        self.style.configure("TEntry", background="yellow", foreground="black", font=("Arial", 14))
        self.style.configure("TButton", background="yellow", foreground="black", font=("Arial", 14))

        # Создание виджетов
        self.label = ttk.Label(self, text="Введите дату рождения (дд.мм.гггг):")
        self.label.pack(pady=25)

        self.entry = ttk.Entry(self)
        self.entry.pack(pady=30)

        self.button = ttk.Button(self, text="Определить знак зодиака", command=self.show_zodiac_sign)
        self.button.pack(pady=20)

        self.result_label = ttk.Label(self, text="")
        self.result_label.pack(pady=20)

    def show_zodiac_sign(self):
        birth_date = self.entry.get()
        zodiac_sign = get_zodiac_sign(birth_date)
        self.result_label.configure(text=f"Ваш знак зодиака: {zodiac_sign}")

if __name__ == "__main__":
    app = ZodiacApp()
    app.mainloop()