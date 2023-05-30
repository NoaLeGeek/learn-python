import json
import os
import tkinter as tk
from tkinter import filedialog

from SimpleCalculator import SimpleCalculator

CONFIG_FILE = "config.json"


def read_config():
    config = {}
    if os.path.exists(CONFIG_FILE):
        with open(CONFIG_FILE) as file:
            config = json.load(file)
    return config


def save_config(config):
    with open(CONFIG_FILE, "w") as file:
        json.dump(config, file, indent=4)


def add_file_path(file_path):
    config = read_config()
    if file_path in config["file_paths"]:
        return
    config["file_paths"] = config.get("file_paths", [])
    config["file_paths"].append(file_path)
    save_config(config)


class MyApp:
    def __init__(self):
        self.window = tk.Tk()
        button = tk.Button(self.window, text="Select JSON File", command=self.select_file, fg="blue", bg="red")
        button.pack()

    def select_file(self):
        file_path = filedialog.askopenfilename(filetypes=[("JSON files", "*.json")])
        if file_path:
            with open(file_path) as file:
                data = json.load(file)
                print("File content:")
                print(data)
                add_file_path(file_path)
                file_selected = tk.Label(text="File: " + os.path.basename(file_path))
                file_selected.pack()
                entry = tk.Entry(self.window, width=50)
                entry.pack()
                entry.insert(0, "Are you enjoying that GUI?")

    def run(self):
        self.window.mainloop()


if __name__ == '__main__':
    app = SimpleCalculator()
    app.run()