# Returns the last element of a list
import tkinter as tk
from tkinter import Entry

import MathsUtils

def generate_choices(choices: dict) -> str:
    string = ""
    for x in range(len(choices)):
        string += str("[" + str(x) + "] " + choices[x] + "\n")
    return string


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


