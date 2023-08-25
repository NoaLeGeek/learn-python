import tkinter as tk
from tkinter import ttk


class Test:

    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Exemple de Slider Checkbox")

        self.slider_checkbox = SliderCheckbox(self.root)
        self.slider_checkbox.pack()
        self.slider_checkbox.slider.configure(command=self.on_slider_checkbox_changed)
        
    def run(self):
        self.root.mainloop()

    def on_slider_checkbox_changed(self):
        if self.slider_checkbox.is_checked():
            print("Slider ON, valeur:", self.slider_checkbox.get())
        else:
            print("Slider OFF")

    def toggle_slider(self, *args):
        if self.int.get():
            self.label.config(text="Slider ON")
        else:
            self.label.config(text="Slider OFF")

class SliderCheckbox(ttk.Frame):
    def __init__(self, master=None, *args, **kwargs):
        super().__init__(master, *args, **kwargs)
        
        self.checkbox_var = tk.BooleanVar()
        self.checkbox = ttk.Checkbutton(self, variable=self.checkbox_var)
        self.checkbox.pack(side=tk.LEFT)

        self.slider = ttk.Scale(self, from_=0, to=1, orient=tk.HORIZONTAL, length=100)
        self.slider.pack(side=tk.LEFT)

    def set(self, value):
        self.slider.set(value)

    def get(self):
        return self.slider.get()

    def is_checked(self):
        return self.checkbox_var.get()