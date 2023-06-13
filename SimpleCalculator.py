from math import *

import customtkinter as ctk
import tkinter as tk

import MathsUtils
import re

import Utils


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
                match index:
                    # Button is the backspace button
                    case 3:
                        button.configure(command=self.backspace)
                    # Button is the x² button
                    case 5:
                        button.configure(command=self.squared)
                    # Button is the ²√x button
                    case 6:
                        button.configure(command=self.squared_root)
                    # Button is the 1/x button
                    case 4:
                        button.configure(command=self.reciprocal)
                    # Button is the ± button
                    case 20:
                        button.configure(command=self.opposite)
                    # Button is the % button
                    case 0:
                        button.configure(command=self.out_of_hundred)
                    # Button is the evaluate button
                    case 23:
                        button.configure(command=self.eval)
                    case _:
                        # Button is a number to insert
                        if index in [8, 9, 10, 12, 13, 14, 16, 17, 18, 21]:
                            button.configure(command=lambda num=index - (-row * row * row + 9 * row * row + 16 * row - 54) / 6: self.insert(num))
                        # Button is an operator to insert
                        elif index in [7, 11, 15, 19, 22]:
                            button.configure(command=lambda char=button.cget("text"): self.insert(char))
                button.grid(row=row + 1, column=col, padx=1, pady=1)

    def eval(self):
        entry = self.entry.get()
        if "," in entry:
            entry = entry.replace(",", ".")
        if "²" in entry:
            entry = entry.replace("²", "**2")
        if "√" in entry:
            matches = re.finditer(r'√+-?\d+(\.\d+)?', entry)
            for matchNum, match in enumerate(matches, start=1):
                entry = entry.replace(match.group(), f"{match.group().replace('√', '')}**{1 / (2 ** match.group().count('√'))}")
        # Evaluate the string for the result
        result = eval(entry)
        # Empty the entry and insert the result
        Utils.delete_entry(self.entry)
        self.entry.insert(0, str(int(result)) if re.match(r"^-?\d+\.0*$", str(result)) else str(result))

    # Delete the last character
    def backspace(self):
        self.entry.delete(len(self.entry.get()) - 1)

    # Delete the last recognized number in the entry
    def delete_last_number(self):
        self.entry.delete(len(self.entry.get()) - len(self.get_numbers()[-1]), tk.END)

    # Insert the text at the end of the entry, format the text if it's a number
    def insert(self, text):
        self.entry.insert(tk.END, MathsUtils.formatted_number(str(text)) if type(text) == float else text)

    def insert_behind(self, text: str, behind: str):
        self.entry.insert(len(self.entry.get()) - len(behind), text)

    def run(self):
        self.window.mainloop()

    # Return a list of string that are numbers in the entry
    def get_numbers(self) -> list[str]:
        return [number.group() for number in re.finditer(r"(\(1\/)+-?(\.\d+)?\d+\)+|-?\d+(\.\d+)?", self.entry.get())]

    def squared(self):
        numbers = self.get_numbers()
        if self.entry.get()[-1] in MathsUtils.operators:
            self.insert(numbers[-1])
        self.insert("²")

    def reciprocal(self):
        numbers = self.get_numbers()
        if not self.entry.get()[-1] in MathsUtils.operators:
            self.delete_last_number()
        self.insert(f"(1/{numbers[-1]})")

    def opposite(self):
        numbers = self.get_numbers()
        if not self.entry.get()[-1] in MathsUtils.operators:
            self.delete_last_number()
        Utils.entry_set(self.entry, MathsUtils.formatted_expression(self.entry.get() + MathsUtils.formatted_number("{:+}".format(-float(numbers[-1])))))

    def squared_root(self):
        numbers = self.get_numbers()
        if self.entry.get()[-1] in MathsUtils.operators:
            self.insert(float(numbers[-1]))
        self.insert_behind("√", numbers[-1])

    def out_of_hundred(self):
        # Get all numbers in the string
        numbers = self.get_numbers()
        # Last character is * or /
        if self.entry.get()[-1] in MathsUtils.operators[2:4]:
            self.insert(float(numbers[-1]) / 100)
        # Last character is + or -
        elif self.entry.get()[-1] in MathsUtils.operators[0:2]:
            self.insert((float(numbers[-1]) / 100) * float(numbers[-1]))
        # Last character is a number
        else:
            self.delete_last_number()
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
