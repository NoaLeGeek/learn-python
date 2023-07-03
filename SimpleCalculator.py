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
        self.total_expression = "0"
        self.current_expression = "0"
        self.display_frame = tk.Frame(self.window, height=221, bg="#F5F5F5")
        self.display_frame.pack(expand=True, fill="both")
        self.buttons_frame = tk.Frame(self.window)
        self.buttons_frame.pack(expand=True, fill="both")
        for x in range(0, 5):
            self.buttons_frame.rowconfigure(x, weight=1)
            if x != 0:
                self.buttons_frame.columnconfigure(x, weight=1)
        self.total_label = tk.Label(self.display_frame, text=self.total_expression, anchor=tk.E, bg="#F5F5F5",
                               fg="#25265E", padx=24, font=("Arial", 16))
        self.total_label.pack(expand=True, fill='both')
        self.label = tk.Label(self.display_frame, text=self.current_expression, anchor=tk.E, bg="#F5F5F5", fg="#25265E",
                              padx=24, font=("Arial", 40, "bold"))
        self.label.pack(expand=True, fill="both")
        button_positions = {
            "%": (1, 1), "CE": (1, 2), "C": (1, 3), "\u232B": (1, 4),
            "1/x": (2, 1), "x²": (2, 2), "²√x": (2, 3), "\u00F7": (2, 4),
            "7": (3, 1), "8": (3, 2), "9": (3, 3), "\u00D7": (3, 4),
            "4": (4, 1), "5": (4, 2), "6": (4, 3), "-": (4, 4),
            "1": (5, 1), "2": (5, 2), "3": (5, 3), "+": (5, 4),
            "±": (6, 1), "0": (6, 2), ",": (6, 3), "=": (6, 4)
        }
        # self.entry = tk.Entry(self.window, width=80, font=("Century Gothic", 9))
        # self.entry.grid(rowspan=1, columnspan=5, sticky=tk.EW)
        #TODO you maybe want to put the command directly in that button_positions (rename the variable)
        for value, position in button_positions.items():
            button = tk.Button(self.buttons_frame, text=value, borderwidth=0)
            index = (position[0]-1)*4 + position[1]
            # The button is a digit
            if index in [9, 10, 11, 13, 14, 15, 17, 18, 19, 22]:
                button.configure(bg="#FFFFFF", fg="#25265E", font=("Arial", 24, "bold"))
            # The button is = button
            elif index == 24:
                button.configure(bg="#CCEDFF", fg="#25265E", font=("Arial", 20))
            # The button is an operator
            else:
                button.configure(bg="#F8FAFF", fg="#25265E", font=("Arial", 20))
            button.grid(row=position[0]-1, column=position[1], sticky=tk.NSEW)

        for row in range(0, 6):
            for col in range(0, 4):
                index = 4 * row + col
                match index:
                    # Button is the CE button
                    case 1:
                        button.configure(command=self.clear_entry)
                    # Button is the C button
                    case 2:
                        button.configure(command=lambda: Utils.delete_entry(self.entry))
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
                            button.configure(command=lambda
                            # This function seems weird but it's actually a Lagrange interpolation
                                num=index - (-row * row * row + 9 * row * row + 16 * row - 54) / 6: self.insert(num))
                        # Button is an operator to insert
                        elif index in [7, 11, 15, 19, 22]:
                            button.configure(command=lambda char=button.cget("text"): self.insert(char))
                # Place the button
                # button.grid(row=row + 1, column=col, padx=1, pady=1)

    # Evaluate the contents of the calculator
    def eval(self):
        self.last_added.append(self.total_expression)
        self.total_expression += self.current_expression
        self.update_total_label()
        try:
            self.current_expression = str(eval(self.total_expression))
            self.total_expression = ""
        except Exception as e:
            self.current_expression = "Division by zero" if isinstance(e, ZeroDivisionError) else "Error"
        finally:
            self.update_label()

    # Delete the last character
    def backspace(self):
        self.last_added.append(self.total_expression)
        self.total_expression = self.total_expression[:-1]

    def update_total_label(self):
        expression = self.total_expression
        if "\u00F7" in expression:
            expression = expression.replace("\u00F7", "/")
        if "\u00D7" in expression:
            expression = expression.replace("\u00D7", "*")
        if "," in expression:
            expression = expression.replace(",", ".")
        if "²" in expression:
            expression = expression.replace("²", "**2")
        if "√" in expression:
            matches = re.finditer(r'√+-?\d+(\.\d+)?', expression)
            for _, match in enumerate(matches, start=1):
                expression = expression.replace(match.group(), f"{match.group().replace('√', '')}**{1 / (2 ** match.group().count('√'))}")
        result = eval(expression)
        self.total_label.config(text=str(int(result)) if re.match(r"^-?\d+\.0*$", str(result)) else str(result))

    def update_label(self):
        self.label.config(text=self.current_expression[:11])

    # Restore the contents of the calculator before the last modification
    def clear_entry(self):
        self.total_expression = self.last_added[-1]
        self.last_added = self.last_added[:-1]

    # Delete the last recognized number in the entry
    def delete_last_number(self):
        self.total_expression = self.total_expression[:-len(self.get_numbers()[-1])]

    # Insert the char or the number
    def insert(self, text):
        self.last_added.append(self.total_expression)
        self.total_expression = (self.total_expression[:-1] if len(self.total_expression) != 0 and not MathsUtils.is_number(text) and self.total_expression[-1] in MathsUtils.operators else self.total_expression) + MathsUtils.formatted_number(str(text))

    def run(self):
        self.window.mainloop()

    # Return a list of string that are numbers in the entry
    def get_numbers(self) -> list[str]:
        return [number.group() for number in re.finditer(r"(\(1\/)+-?\d+(\.\d+)?\)+|-?\d+(\.\d+)?", self.total_expression)]

    # Used by the x² button
    def squared(self):
        self.last_added.append(self.total_expression)
        self.total_expression += (self.get_numbers()[-1] if self.total_expression[-1] in MathsUtils.operators else "") + "²"

    # Used by the 1/x button
    def reciprocal(self):
        self.last_added.append(self.total_expression)
        numbers = self.get_numbers()
        if not self.total_expression[-1] in MathsUtils.operators:
            self.delete_last_number()
        self.total_expression += f"(1/{numbers[-1]})"

    # Used by the ± button
    def opposite(self):
        self.last_added.append(self.total_expression)
        if not self.total_expression[-1] in MathsUtils.operators:
            self.delete_last_number()
        self.total_expression = MathsUtils.formatted_expression(self.total_expression + MathsUtils.formatted_number("{:+}".format(-float(self.get_numbers()[-1]))))

    # Used by the ²√x button
    def squared_root(self):
        self.last_added.append(self.total_expression)
        numbers = self.get_numbers()
        if self.total_expression[-1] in MathsUtils.operators:
            self.total_expression += numbers[-1]
        index = len(self.total_expression) - len(numbers[-1])
        self.total_expression = f"{self.total_expression[:index]}√{self.total_expression[index:]}"

    # Used by the % button
    def out_of_hundred(self):
        self.last_added.append(self.total_expression)
        # Get all numbers in the string
        numbers = self.get_numbers()
        # Last character is an operator
        if self.total_expression[-1] in MathsUtils.operators:
            self.total_expression += str(float(numbers[-1]) / 100 * (float(numbers[-1]) if self.total_expression[-1] in MathsUtils.operators[0:2] else 1))
        # Last character is a number
        else:
            self.delete_last_number()
            if len(self.total_expression) != 0 and self.total_expression[-1] in MathsUtils.operators[2:4]:
                self.total_expression += str(float(numbers[1]) / 100)
            else:
                number = (float(numbers[-2]) * float(numbers[-1]) / 100) if len(numbers) > 1 else 0
                if len(numbers) > 1 and float(numbers[-2]) < 0:
                    if number < 0:
                        self.total_expression = self.total_expression[:-1] + MathsUtils.formatted_number(str(number))
                    else:
                        self.total_expression += f"{number:+}"
                else:
                    self.total_expression += str(number)


if __name__ == '__main__':
    simple_calculator = SimpleCalculator()
    simple_calculator.run()
