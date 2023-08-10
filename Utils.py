# Returns the last element of a list
import tkinter as tk
from tkinter import Entry

import MathsUtils

def generate_choices(choices: dict) -> str:
    string = ""
    for x in range(len(choices)):
        string += str("[" + str(x) + "] " + choices[x] + "\n")
    return string


# Returns the boxes to be filled in a given nonogram column or row that are sure to be filled in
def nonogram_boxes(number: int, length: int = 10) -> list[int]:
    if number > length:
        raise ValueError("The number must be smaller or equal than the length")
    if number == length:
        return [1 for _ in range(length)]
    positions = [1 for _ in range(number)] + [0 for _ in range(length - number)]
    boxes = positions.copy()
    while positions[-1] != 1:
        positions.insert(0, 0)
        positions.pop()
        boxes = [0 if not (positions[i] == 1 and boxes[i] == 1) else 1 for i in range(len(positions))]
    return boxes

# Set a new value for the entry
def set_entry(entry: Entry, string: str) -> None:
    delete_entry(entry)
    entry.insert(0, string)


# Delete the whole entry
def delete_entry(entry: Entry) -> None:
    entry.delete(0, tk.END)


# Insert at the entry's end the specified text
def insert_entry(entry: Entry, string: str) -> None:
    entry.insert(tk.END, MathsUtils.formatted_number(string) if MathsUtils.is_number(string) else string)


