from tkinter import *
from tkinter import ttk


class Test:

    def __init__(self):
        self.root = Tk()
        self.root.title("Profile Entry using Grid")
        self.root.geometry("500x300")  # set starting size of window
        self.root.maxsize(500, 300)  # width x height
        self.root.config(bg="lightgrey")

        # Enter specific information for your profile into the following widgets
        self.enter_info = Label(self.root, text="Please enter your information: ", bg="lightgrey")
        self.enter_info.grid(row=0, column=1, columnspan=4, padx=5, pady=5)

        # Name label and entry widgets
        Label(self.root, text="Name", bg="lightgrey").grid(row=1, column=1, padx=5, pady=5, sticky=E)

        self.name = Entry(self.root, bd=3)
        self.name.grid(row=1, column=2, padx=5, pady=5)

        # Gender label and dropdown widgets
        self.gender = Menubutton(self.root, text="Gender")
        self.gender.grid(row=2, column=2, padx=5, pady=5, sticky=W)
        self.gender.menu = Menu(self.gender, tearoff=0)
        self.gender["menu"] = self.gender.menu

        # choices in gender dropdown menu
        self.gender.menu.add_cascade(label="Male")
        self.gender.menu.add_cascade(label="Female")
        self.gender.menu.add_cascade(label="Other")
        self.gender.grid()

        # Eyecolor label and entry widgets
        Label(self.root, text="Eye Color", bg="lightgrey").grid(row=3, column=1, padx=5, pady=5, sticky=E)
        self.eyes = Entry(self.root, bd=3)
        self.eyes.grid(row=3, column=2, padx=5, pady=5)

        # Height and Weight labels and entry widgets
        Label(self.root, text="Height", bg="lightgrey").grid(row=4, column=1, padx=5, pady=5, sticky=E)
        Label(self.root, text="inches", bg="lightgrey").grid(row=4, column=3, sticky=W)

        self.height = Entry(self.root, bd=3)
        self.height.grid(row=4, column=2, padx=5, pady=5)

        Label(self.root, text="Weight", bg="lightgrey").grid(row=5, column=1, padx=5, pady=5, sticky=E)
        Label(self.root, text="lbs", bg="lightgrey").grid(row=5, column=3, sticky=W)

        self.weight = Entry(self.root, bd=3)
        self.weight.grid(row=5, column=2, padx=5, pady=5)

    def run(self):
        self.root.mainloop()


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
