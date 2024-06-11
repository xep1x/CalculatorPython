# calculator/ui.py

import tkinter as tk
from calculator.logic import evaluate_expression

class CalculatorApp:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Calculator")
        self.root.resizable(0, 0)  # Запрещаем изменение размера окна

        self.entry = tk.Entry(self.root, width=17, font=("Segoe UI", 24), bd=10, insertwidth=4, bg="#1e1e1e", fg="white", justify='right')
        self.entry.grid(row=0, column=0, columnspan=4, pady=10)

        self.create_buttons()

    def create_buttons(self):
        # Кнопки в стиле калькулятора Windows 10
        button_texts = [
            ('%', 1, 0), ('CE', 1, 1), ('C', 1, 2), ('←', 1, 3),
            ('1/x', 2, 0), ('x²', 2, 1), ('√x', 2, 2), ('/', 2, 3),
            ('7', 3, 0), ('8', 3, 1), ('9', 3, 2), ('*', 3, 3),
            ('4', 4, 0), ('5', 4, 1), ('6', 4, 2), ('-', 4, 3),
            ('1', 5, 0), ('2', 5, 1), ('3', 5, 2), ('+', 5, 3),
            ('±', 6, 0), ('0', 6, 1), ('.', 6, 2), ('=', 6, 3)
        ]

        for (text, row, col) in button_texts:
            button = tk.Button(self.root, text=text, padx=20, pady=20, font=("Segoe UI", 18),
                               bg="#333333", fg="white", activebackground="#4f4f4f", activeforeground="white",
                               command=lambda t=text: self.on_button_click(t))
            button.grid(row=row, column=col, padx=5, pady=5, sticky="nsew")

    def on_button_click(self, char):
        if char == 'C':
            self.entry.delete(0, tk.END)
        elif char == 'CE':
            self.entry.delete(0, tk.END)
        elif char == '←':
            current_text = self.entry.get()
            self.entry.delete(0, tk.END)
            self.entry.insert(tk.END, current_text[:-1])
        elif char == '=':
            expression = self.entry.get()
            result = evaluate_expression(expression)
            self.entry.delete(0, tk.END)
            self.entry.insert(tk.END, str(result))
        elif char == '±':
            current_text = self.entry.get()
            if current_text.startswith('-'):
                self.entry.delete(0, tk.END)
                self.entry.insert(tk.END, current_text[1:])
            else:
                self.entry.insert(0, '-')
        elif char == '1/x':
            try:
                current_value = float(self.entry.get())
                result = 1 / current_value
                self.entry.delete(0, tk.END)
                self.entry.insert(tk.END, str(result))
            except Exception as e:
                self.entry.delete(0, tk.END)
                self.entry.insert(tk.END, "Error")
        elif char == 'x²':
            try:
                current_value = float(self.entry.get())
                result = current_value ** 2
                self.entry.delete(0, tk.END)
                self.entry.insert(tk.END, str(result))
            except Exception as e:
                self.entry.delete(0, tk.END)
                self.entry.insert(tk.END, "Error")
        elif char == '√x':
            try:
                current_value = float(self.entry.get())
                result = current_value ** 0.5
                self.entry.delete(0, tk.END)
                self.entry.insert(tk.END, str(result))
            except Exception as e:
                self.entry.delete(0, tk.END)
                self.entry.insert(tk.END, "Error")
        elif char == '%':
            try:
                current_value = float(self.entry.get())
                result = current_value / 100
                self.entry.delete(0, tk.END)
                self.entry.insert(tk.END, str(result))
            except Exception as e:
                self.entry.delete(0, tk.END)
                self.entry.insert(tk.END, "Error")
        else:
            current_text = self.entry.get()
            new_text = current_text + char
            self.entry.delete(0, tk.END)
            self.entry.insert(tk.END, new_text)

    def run(self):
        self.root.mainloop()
