import json
import os
import tkinter as tk
from tkinter import filedialog, ttk


class JSONKeyValueConfig:
    config_file = "config.json"
    def __init__(self):
        self.window = tk.Tk()
        self.window.title("JSONKeyValueConfig")
        self.window.geometry("500x500")
        button = tk.Button(self.window, text="Add a filepath", command=self.add_filepath)
        button.pack(side="top")
        self.filepath = tk.Label(self.window, text="No file added")
        self.filepath.pack(side="top")

    def add_filepath(self):
        filepath = tk.filedialog.askopenfilename(initialdir="/", title="Select a JSON file",
                                                 filetypes=(("JSON files", "*.json"), ("All files", "*.*")))
        self.update_config(filepath)

    def update_config(self, filepath):
        # This is the default config if the config_file doesn't exist
        config = {"filePath": []}
        # If the config_file doesn't exist, it will be created
        if os.path.isfile(self.config_file):
            try:
                # Read the config_file
                with open(self.config_file, "r") as file:
                    config = json.load(file)
            except json.JSONDecodeError:
                pass
        # Add the new filepath to the config_file's list if it's not already in the list
        if filepath == "":
            self.filepath.config(text="Empty filepath")
        elif filepath not in config["filePath"]:
            config["filePath"].append(filepath)
            # Write the updated config to the config_file
            with open(self.config_file, "w") as file:
                json.dump(config, file, indent=4)
            # Update the filepath label
            self.filepath.config(text=os.path.basename(filepath))
        else:
            self.filepath.config(text="Filepath already added")

    def run(self):
        self.window.mainloop()
