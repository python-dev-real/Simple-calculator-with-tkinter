import tkinter as tk
from tkinter import font
import math

class AdvancedCalculator:
    def __init__(self, root):
        self.root = root
        self.root.title("Advanced Calculator")
        self.root.geometry("500x700")
        self.root.configure(bg="#1e1e1e")
        self.root.resizable(False, False)

        self.expression = ""

        self.display_var = tk.StringVar()

        display = tk.Entry(
            root,
            textvariable=self.display_var,
            font=("Consolas", 24),
            bd=0,
            bg="#2d2d2d",
            fg="white",
            justify="right"
        )
        display.pack(fill="both", padx=10, pady=10, ipady=20)

        btn_frame = tk.Frame(root, bg="#1e1e1e")
        btn_frame.pack(expand=True, fill="both")

        buttons = [
            ["C", "⌫", "(", ")"],
            ["sin", "cos", "tan", "√"],
            ["log", "ln", "^", "/"],
            ["7", "8", "9", "*"],
            ["4", "5", "6", "-"],
            ["1", "2", "3", "+"],
            ["0", ".", "π", "="]
        ]

        for r, row in enumerate(buttons):
            for c, text in enumerate(row):
                self.create_button(btn_frame, text, r, c)

        for i in range(7):
            btn_frame.rowconfigure(i, weight=1)

        for i in range(4):
            btn_frame.columnconfigure(i, weight=1)

    def create_button(self, parent, text, row, col):
        colors = {
            "=": "#4CAF50",
            "C": "#f44336",
            "⌫": "#ff9800"
        }

        bg = colors.get(text, "#3a3a3a")

        btn = tk.Button(
            parent,
            text=text,
            font=("Segoe UI", 18, "bold"),
            bg=bg,
            fg="white",
            bd=0,
            activebackground="#555555",
            command=lambda t=text: self.on_click(t)
        )

        btn.grid(
            row=row,
            column=col,
            sticky="nsew",
            padx=3,
            pady=3
        )

    def on_click(self, value):
        if value == "C":
            self.expression = ""
            self.display_var.set("")

        elif value == "⌫":
            self.expression = self.expression[:-1]
            self.display_var.set(self.expression)

        elif value == "=":
            self.calculate()

        elif value == "√":
            self.expression += "sqrt("
            self.display_var.set(self.expression)

        elif value == "π":
            self.expression += str(math.pi)
            self.display_var.set(self.expression)

        elif value == "^":
            self.expression += "**"
            self.display_var.set(self.expression)

        elif value == "sin":
            self.expression += "sin("
            self.display_var.set(self.expression)

        elif value == "cos":
            self.expression += "cos("
            self.display_var.set(self.expression)

        elif value == "tan":
            self.expression += "tan("
            self.display_var.set(self.expression)

        elif value == "log":
            self.expression += "log10("
            self.display_var.set(self.expression)

        elif value == "ln":
            self.expression += "log("
            self.display_var.set(self.expression)

        else:
            self.expression += value
            self.display_var.set(self.expression)

    def calculate(self):
        try:
            allowed = {
                "sin": lambda x: math.sin(math.radians(x)),
                "cos": lambda x: math.cos(math.radians(x)),
                "tan": lambda x: math.tan(math.radians(x)),
                "sqrt": math.sqrt,
                "log10": math.log10,
                "log": math.log,
                "pi": math.pi
            }

            result = eval(self.expression, {"__builtins__": None}, allowed)

            self.display_var.set(str(result))
            self.expression = str(result)

        except Exception:
            self.display_var.set("Error")
            self.expression = ""

if __name__ == "__main__":
    root = tk.Tk()
    app = AdvancedCalculator(root)
    root.mainloop()

