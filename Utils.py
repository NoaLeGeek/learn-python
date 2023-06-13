# Returns the last element of a list
import tkinter as tk
from tkinter import Entry


def generate_choices(choices: dict) -> str:
    string = ""
    for x in range(len(choices)):
        string += str("[" + str(x) + "] " + choices[x] + "\n")
    return string


# Set a new value for the entry
def entry_set(entry: Entry, string: str) -> None:
    delete_entry(entry)
    entry.insert(0, string)


# Delete the whole entry
def delete_entry(entry: Entry) -> None:
    entry.delete(0, tk.END)


