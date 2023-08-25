import inspect
import json
import os
import tkinter as tk
from tkinter import filedialog, ttk
import ttkbootstrap 


class JSONKeyValueConfig:
    config_file = "config.json"
    default_config = {"filePath": [], "autoSlot": False}
    slots = {}
    list_buttons = []

    def __init__(self):
        config = self.default_config
        if os.path.isfile(self.config_file):
            try:
                with open(self.config_file, "r") as file:
                    config = json.load(file)
                    config["autoSlot"] = False
            except json.JSONDecodeError:
                pass
        with open(self.config_file, "w") as file:
            json.dump(config, file, indent=4)
        self.window = tk.Tk()
        self.window.title("JSONKeyValueConfig")
        self.window.geometry("500x500")
        self.auto_slot_button = tk.Button(self.window, text="Auto slot: OFF", command=self.toggle_auto_slot)
        self.auto_slot_button.pack(side="top")
        self.toggle_auto_slot = ttkbootstrap.Checkbutton(self.window, text="Auto slot", command=self.toggle_auto_slot)
        button = tk.Button(self.window, text="Add a filepath", command=self.add_filepath)
        button.pack(side="top")
        self.filepath = tk.Label(self.window, text="No file added")
        self.filepath.pack(side="top")
        with open(self.config_file, "r") as file:
            config = json.load(file)
            if config["filePath"]:
                self.add_slot([os.path.basename(path) for path in config["filePath"]])

    def add_filepath(self):
        filepath = tk.filedialog.askopenfilename(initialdir="/", title="Select a JSON file",
                                                 filetypes=(("JSON files", "*.json"), ("All files", "*.*")))
        self.update_config(filepath)

    def update_config(self, filepath):
        # This is the default config if the config_file doesn't exist
        config = self.default_config
        # If the config_file doesn't exist, it will be created
        if os.path.isfile(self.config_file):
            try:
                # Read the config_file
                with open(self.config_file, "r") as file:
                    config = json.load(file)
            except json.JSONDecodeError:
                pass
        # The filepath is empty
        if filepath == "":
            self.filepath.config(text="Empty filepath")
        # Add the new filepath to the config_file's list if it's not already in the list
        elif filepath not in config["filePath"]:
            config["filePath"].append(filepath)
            # Write the updated config to the config_file
            with open(self.config_file, "w") as file:
                json.dump(config, file, indent=4)
            # Update the filepath label
            self.filepath.config(text=os.path.basename(filepath))
            files = [os.path.basename(path) for path in config["filePath"]]
            # The list of slots isn't empty
            if self.slots.keys():
                # Update the slots' values
                self.update_slots(files)
                if config["autoSlot"]:
                    self.add_slot(files)
            else:
                self.add_slot(files)
        # The filepath is already in the list
        else:
            self.filepath.config(text="Filepath already added")

    def update_slots(self, filepaths):
        for slot in self.slots.keys():
            slot.config(values=filepaths)

    def add_slot(self, filepaths):
        variable = tk.StringVar()
        slot = ttk.OptionMenu(self.window, variable, filepaths[0], *filepaths)
        slot.pack(side="top")
        add_button = tk.Button(self.window, text="Add a slot", command=lambda: self.add_slot(filepaths))
        add_button.pack(side="top")
        remove_button = None
        if self.slots.keys():
            remove_button = tk.Button(self.window, text="Remove a slot",
                                      command=lambda index=len(self.slots): self.remove_slot(index))
            remove_button.pack(side="top")
        self.slots[slot] = variable, add_button, remove_button
        print(["values: "]+list(self.slots.values()))
        print(["keys: "]+list(self.slots.keys()))

    def remove_slot(self, index):
        # Update the slots' remove buttons only if the index isn't the last one
        if index != len(self.slots) - 1:
            for i in range(index, len(self.slots)):
                #TODO maybe delete index_slot variable
                print(list(self.slots.values())[i][2])
                list(self.slots.values())[i][2]["command"] = lambda index_slot=i - 1: self.remove_slot(index_slot)
        # Remove the slot and its buttons at the given index
        self.slots.pop(list(self.slots.keys())[index]).destroy()
        for button in list(self.slots.values())[index][1:]:
            button.destroy()
        print(["values R: "]+list(self.slots.values()))
        print(["keys R: "]+list(self.slots.keys()))
        

    def toggle_auto_slot(self):
        with open(self.config_file, "r") as file:
            config = json.load(file)
            auto_slot = not config["autoSlot"]
        # Update the auto slot button
        self.auto_slot_button.config(text=f"Auto slot: {'ON' if auto_slot else 'OFF'}")
        # Update the auto slot value in the config_file
        config = self.default_config
        if os.path.isfile(self.config_file):
            try:
                with open(self.config_file, "r") as file:
                    config = json.load(file)
            except json.JSONDecodeError:
                pass
        config["autoSlot"] = auto_slot
        with open(self.config_file, "w") as file:
            json.dump(config, file, indent=4)

    def run(self):
        self.window.mainloop()

#TODO change the placement system to the grid system
#TODO replace ttk.Combobox by ttk.OptionMenu
#TODO add a slider true/false for autoSlot button