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
def nonogram_boxes(*args, length: int = 10) -> list[int]:
    if len(args) - 1 + sum(args) > length:
        raise ValueError("The number must be smaller or equal than the length")
    if isinstance(args, int):
        args = (args,)
    if len(args) - 1 + sum(args) == length:
        return [1 if i % (num + 1) < num else 0 for num in args for i in range(num + 1)][:-1]
    positions = [1 if i % (num + 1) < num else 0 for num in args for i in range(num + 1)] + [0] * (
            length - sum(args) - len(args))
    boxes = positions.copy()
    for _ in range(length - sum(args) - len(args) + 1):
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


# Solve a system of two equations with two unknowns variables
def solve_system(a1, b1, c1, a2, b2, c2) -> tuple[int, int] | None:
    determinant = a1 * b2 - a2 * b1
    if determinant == 0:
        return None
    return (c1 * b2 - c2 * b1) / determinant, (a1 * c2 - a2 * c1) / determinant


# Ajust the length of a list to be a multiple of n
def ajust_len_list(lst, n):
    longueur_desiree = (len(lst) // n) * n
    return lst[:longueur_desiree]


# Divide a list into lists that have a length of n
def divide_list(lst, n):
    return [lst[i:i + n] for i in range(0, len(lst), n)]