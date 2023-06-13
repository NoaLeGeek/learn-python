# Returns the last element of a list
import tkinter
from tkinter import Entry


def last_element(lizt: list) -> object:
    return lizt[len(lizt) - 1]


def generate_choices(choices: dict) -> str:
    string = ""
    for x in range(len(choices)):
        string += str("[" + str(x) + "] " + choices[x] + "\n")
    return string


def entry_set(entry: Entry, string: str) -> None:
    entry.delete(0, tkinter.END)
    entry.insert(0, string)


