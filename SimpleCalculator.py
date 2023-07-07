#!/usr/bin/env python3
import tkinter as tk

import re

import MathsUtils
import Utils


class SimpleCalculator:
    # This variable is filled with the contents of the calculator as the user presses its buttons.
    last_added = []

    def __init__(self):
        self.window = tk.Tk()
        self.window.title("SimpleCalculator")
        self.window.geometry("375x667")
        self.window.resizable(0, 0)
        self.expression = "0"
        self.display_frame = tk.Frame(self.window, height=221, bg="#F5F5F5")
        self.display_frame.pack(expand=True, fill="both")
        self.buttons_frame = tk.Frame(self.window)
        self.buttons_frame.pack(expand=True, fill="both")
        for x in range(0, 5):
            self.buttons_frame.rowconfigure(x, weight=1)
            if x != 0:
                self.buttons_frame.columnconfigure(x, weight=1)
        self.label = tk.Label(self.display_frame, text=self.expression, anchor=tk.E, bg="#F5F5F5", fg="#25265E",
                              padx=24, font=("Arial", 20, "bold"))
        self.label.pack(expand=True, fill="both")
        # The buttons are placed on the first row (row 0) and the second column (column 1) of the grid
        button_information = {
            "%": (0, 1, self.out_of_hundred), "CE": (0, 2, self.clear_entry), "C": (0, 3, self.clear), "\u232B": (0, 4, self.backspace),
            "1/x": (1, 1, self.reciprocal), "x²": (1, 2, self.squared), "²√x": (1, 3, self.squared_root), "\u00F7": (1, 4),
            "7": (2, 1), "8": (2, 2), "9": (2, 3), "\u00D7": (2, 4),
            "4": (3, 1), "5": (3, 2), "6": (3, 3), "-": (3, 4),
            "1": (4, 1), "2": (4, 2), "3": (4, 3), "+": (4, 4),
            "±": (5, 1, self.opposite), "0": (5, 2), ",": (5, 3), "=": (5, 4)
        }
        for value, information in button_information.items():
            # information[0] is the button's position's row
            # information[1] is the button's position's column
            # information[2] is the button's command, if information[2] doesn't exist, the button's command will be set in this loop
            # Nothing happens if the "command" parameter is set to an empty string
            button = tk.Button(self.buttons_frame, text=value, borderwidth=0)
            index = information[0]*4 + information[1]
            # The button is the = button
            if index == 24:
                button.configure(bg="#CCEDFF", fg="#25265E", font=("Arial", 20), command=self.eval)
            # The button is a digit button
            elif index in [9, 10, 11, 13, 14, 15, 17, 18, 19, 22]:
                button.configure(bg="#FFFFFF", fg="#25265E", font=("Arial", 24, "bold"), command=lambda digit=-3 * (information[0] - 4) + information[1] + (1 if information[0] > 4 else 0): self.insert(digit))
            # The button is an operator
            else:
                button.configure(bg="#F8FAFF", fg="#25265E", font=("Arial", 20), command=information[2] if len(information) > 2 else lambda operator=value: self.insert(operator))
            button.grid(row=information[0], column=information[1], sticky=tk.NSEW)

    # Evaluate the contents of the calculator
    def eval(self):
        self.last_added.append(self.expression)
        if "\u00F7" in self.expression:
            self.expression = self.expression.replace("\u00F7", "/")
        if "\u00D7" in self.expression:
            self.expression = self.expression.replace("\u00D7", "*")
        if "," in self.expression:
            self.expression = self.expression.replace(",", ".")
        if "²" in self.expression:
            matches = re.finditer(r'-?\d+(\.\d+)?²+', self.expression)
            for _, match in enumerate(matches, start=1):
                self.expression = self.expression.replace(match.group(), f"{'('*match.group().count('²')}{match.group().replace('²', '')}{'**2)'*match.group().count('²')}")
        if "√" in self.expression:
            matches = re.finditer(r'√+-?\d+(\.\d+)?', self.expression)
            for _, match in enumerate(matches, start=1):
                self.expression = self.expression.replace(match.group(), f"{match.group().replace('√', '')}**{1 / (2 ** match.group().count('√'))}")
        try:
            result = eval(self.expression)
            self.expression = str(int(result)) if re.match(r"^-?\d+\.0*$", str(result)) else str(result)
        except Exception as e:
            self.expression = "Division by zero" if isinstance(e, ZeroDivisionError) else ("Syntax error" if isinstance(e, SyntaxError) else "Error")
            print(e)
        finally:
            self.update_label()

    def clear(self):
        self.expression = ""
        self.update_label()

    # Delete the last character
    def backspace(self):
        self.last_added.append(self.expression)
        self.expression = self.expression[:-1]
        self.update_label()

    def update_label(self):
        self.label.config(text=self.expression[:22])

    # Restore the contents of the calculator before the last modification
    def clear_entry(self):
        self.expression = self.last_added[-1]
        self.update_label()
        self.last_added = self.last_added[:-1]

    # Delete the last recognized number in the entry
    def delete_last_number(self):
        self.expression = self.expression[:-len(self.get_numbers()[-1])]

    # Insert the char or the number
    def insert(self, text):
        self.last_added.append(self.expression)
        self.expression = (self.expression[:-1] if self.expression == "0" or (len(self.expression) != 0 and not MathsUtils.is_number(text) and self.expression[-1] in MathsUtils.operators) else self.expression) + MathsUtils.formatted_number(str(text))
        self.update_label()

    def run(self):
        self.window.mainloop()

    # Return a list of string that are numbers in the entry
    def get_numbers(self) -> list[str]:
        return [number.group() for number in re.finditer(r"(\(1\/)+-?\d+(\.\d+)?²*\)+|-?\d+(\.\d+)?²*", self.expression)]

    # Used by the x² button
    def squared(self):
        self.last_added.append(self.expression)
        self.expression += (self.get_numbers()[-1] if self.expression[-1] in MathsUtils.operators else "") + "²"
        self.update_label()

    # Used by the 1/x button
    def reciprocal(self):
        self.last_added.append(self.expression)
        numbers = self.get_numbers()
        if not self.expression[-1] in MathsUtils.operators:
            self.delete_last_number()
        self.expression += f"(1/{numbers[-1]})"
        self.update_label()

    # Used by the ± button
    def opposite(self):
        self.last_added.append(self.expression)
        if not self.expression[-1] in MathsUtils.operators:
            self.delete_last_number()
        self.expression = MathsUtils.formatted_expression(self.expression + MathsUtils.formatted_number("{:+}".format(-float(self.get_numbers()[-1]))))
        self.update_label()

    # Used by the ²√x button
    def squared_root(self):
        self.last_added.append(self.expression)
        numbers = self.get_numbers()
        if self.expression[-1] in MathsUtils.operators:
            self.expression += numbers[-1]
        index = len(self.expression) - len(numbers[-1])
        self.expression = f"{self.expression[:index]}√{self.expression[index:]}"
        self.update_label()

    # Used by the % button
    def out_of_hundred(self):
        self.last_added.append(self.expression)
        # Get all numbers in the string
        numbers = self.get_numbers()
        # Last character is an operator
        if self.expression[-1] in MathsUtils.operators:
            self.expression += str(float(numbers[-1]) / 100 * (float(numbers[-1]) if self.expression[-1] in MathsUtils.operators[0:2] else 1))
        # Last character is a number
        else:
            self.delete_last_number()
            if len(self.expression) != 0 and self.expression[-1] in MathsUtils.operators[2:4]:
                self.expression += str(float(numbers[1]) / 100)
            else:
                number = (float(numbers[-2]) * float(numbers[-1]) / 100) if len(numbers) > 1 else 0
                if len(numbers) > 1 and float(numbers[-2]) < 0:
                    if number < 0:
                        self.expression = self.expression[:-1] + MathsUtils.formatted_number(str(number))
                    else:
                        self.expression += f"{number:+}"
                else:
                    self.expression += str(number)
        self.update_label()


if __name__ == '__main__':
    simple_calculator = SimpleCalculator()
    simple_calculator.run()
