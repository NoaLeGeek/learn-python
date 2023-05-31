import math

import customtkinter as ctk
import tkinter as tk

import MathsUtils
import re


class SimpleCalculator:
    def __init__(self):
        self.window = tk.Tk()
        self.entry = tk.Entry(self.window, width=80)
        self.entry.grid(row=0, columnspan=4)
        for row in range(0, 6):
            for col in range(0, 4):
                index = 4 * row + col
                button = ctk.CTkButton(self.window,
                                       text=["%", "CE", "C", "\u232B",
                                             "1/x", "x²", "²√x", "/",
                                             "7", "8", "9", "*",
                                             "4", "5", "6", "-",
                                             "1", "2", "3", "+",
                                             "±", "0", ",", "="][index])
                # Button is a number to insert
                if index in [8, 9, 10, 12, 13, 14, 16, 17, 18, 21]:
                    button.configure(
                        command=lambda num=index - (-row * row * row + 9 * row * row + 16 * row - 54) / 6: self.insert(
                            num))
                # Button is an operator to insert
                elif index in [7, 11, 15, 19]:
                    button.configure(command=lambda char=button.cget("text"): self.insert(char))
                # Button is the backspace button
                elif index == 3:
                    button.configure(command=self.backspace)
                # Button is the x² button
                elif index == 5:
                    button.configure(command=self.squared)
                # Button is the % button
                elif index == 0:
                    button.configure(command=self.out_of_hundred)
                # Button is the evaluate button
                elif index == 23:
                    button.configure(command=self.eval)
                button.grid(row=row + 1, column=col, padx=1, pady=1)

    def eval(self):
        entry = self.entry.get().replace("²", "**2")
        # Evaluate the string for the result
        result = eval(entry)
        # Empty the entry and insert the result
        self.entry.delete(0, tk.END)
        self.entry.insert(0, str(result))

    def backspace(self):
        # Delete the last character
        self.entry.delete(len(self.entry.get()) - 1)

    def insert(self, text):
        # text is a number
        if type(text) == float:
            self.entry.insert(tk.END, str(int(text)) if re.match(r"^-?\d+\.0*$", str(text)) else str(text))
        # text is a string
        else:
            if len(self.entry.get()) != 0 and self.entry.get()[-1] in MathsUtils.operators:
                self.backspace()
            self.entry.insert(tk.END, text)

    def run(self):
        self.window.mainloop()

    def get_numbers(self):
        return re.findall(r"(-?\d+(?:\.\d+)?)", self.entry.get())

    def squared(self):
        numbers = self.get_numbers()
        if self.entry.get()[-1] in MathsUtils.operators:
            self.insert(numbers[-1])
        self.insert("²")


    def out_of_hundred(self):
        # Get all numbers in the string
        numbers = self.get_numbers()
        # Last character is * or /
        if self.entry.get()[-1] in MathsUtils.operators[2:4]:
            self.insert(float(numbers[-1])/100)
        # Last character is + or -
        elif self.entry.get()[-1] in MathsUtils.operators[0:2]:
            self.insert((float(numbers[-1]) / 100) * float(numbers[-1]))
        # Last character is a number
        else:
            self.entry.delete(len(self.entry.get()) - len(numbers[-1]), tk.END)
            if len(self.entry.get()) != 0 and self.entry.get()[-1] in MathsUtils.operators[2:4]:
                self.insert(float(numbers[1]) / 100)
            else:
                number = (float(numbers[-2]) if len(numbers) > 1 else 0) * (float(numbers[-1]) / 100)
                self.insert("+" if number > 0 else "")
                self.insert(number)


if __name__ == '__main__':
    ctk.set_appearance_mode('System')
    simple_calculator = SimpleCalculator()
    simple_calculator.run()
