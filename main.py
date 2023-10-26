import random
import tkinter

import nsi

length = 400
window = tkinter.Tk()
canvas = tkinter.Canvas(window, bg='grey', height=length, width=length)
x1, y1 = -1, -1


def main():
    canvas.pack(side=tkinter.LEFT)
    canvas.bind("<Button-1>", click)
    value = tkinter.IntVar()
    frame = tkinter.Frame(window, borderwidth=2, relief=tkinter.GROOVE)
    frame.pack(side=tkinter.TOP)
    bouton4 = tkinter.Radiobutton(frame, text="Segment", variable=value, value=1)
    bouton5 = tkinter.Radiobutton(frame, text="Rectangle", variable=value, value=2)
    bouton6 = tkinter.Radiobutton(frame, text="Disque", variable=value, value=3)
    bouton4.pack(side=tkinter.TOP, padx=5, pady=5)
    bouton5.pack(side=tkinter.TOP, padx=5, pady=5)
    bouton6.pack(side=tkinter.TOP, padx=5, pady=5)
    button1 = tkinter.Button(window, text='Quitter', command=window.quit)
    button1.pack(side=tkinter.BOTTOM, padx=5, pady=5)
    cmd = None
    print(value.get())
    if value.get() == 1:
        cmd = lambda: drawLine(canvas, length)
    elif value.get() == 2:
        cmd = lambda: drawRectangle(canvas, length)
    else:
        cmd = lambda: drawCircle(canvas, length)
    button2 = tkinter.Button(window, text='Tracer la forme', command=cmd)
    button2.pack(side=tkinter.TOP, padx=5, pady=5)
    button3 = tkinter.Button(window, text='Effacer', command=lambda: clearCanvas(canvas))
    button3.pack(side=tkinter.TOP, padx=5, pady=5)
    window.mainloop()


def click(event):
    global x1, y1
    if x1 == -1:
        x1, y1 = event.x, event.y
    else:
        canvas.create_line(x1, y1, event.x, event.y, width=2,
                           fill=random.choice(['white', 'black', 'red', 'green', 'blue', 'cyan', 'yellow', 'magenta']))
        x1, y1 = -1, -1


def drawLine(canvas: tkinter.Canvas, length, width=2):
    for i in range(5):
        canvas.create_line(random.randint(0, length), random.randint(0, length),
                           random.randint(0, length), random.randint(0, length), width=width,
                           fill=random.choice(['white', 'black', 'red', 'green', 'blue', 'cyan', 'yellow', 'magenta']))


def drawRectangle(canvas: tkinter.Canvas, length, width=2):
    for i in range(5):
        canvas.create_rectangle(random.randint(0, length), random.randint(0, length),
                                random.randint(0, length), random.randint(0, length), width=width,
                                fill=random.choice(
                                    ['white', 'black', 'red', 'green', 'blue', 'cyan', 'yellow', 'magenta']))


def drawCircle(canvas: tkinter.Canvas, length, width=2):
    for i in range(5):
        canvas.create_oval(random.randint(0, length), random.randint(0, length),
                           random.randint(0, length), random.randint(0, length), width=width,
                           fill=random.choice(['white', 'black', 'red', 'green', 'blue', 'cyan', 'yellow', 'magenta']))


def clearCanvas(canvas: tkinter.Canvas):
    canvas.delete(tkinter.ALL)


if __name__ == '__main__':
    main()
    carre = [[4, 14, 15, 1],
             [9, 7, 6, 12],
             [5, 11, 10, 8],
             [16, 2, 3, 13]]
    print(nsi.carre_magique(carre))
    planetes = {'Mercure': (58, 4878 / 149.5978707, 0),
                'Vénus': (108, 12100 / 149.5978707, 0),
                'Terre': (150, 12756 / 149.5978707, 1),
                'Mars': (228, 6795 / 149.5978707, 2),
                'Jupiter': (778, 142984 / 149.5978707, 16),
                'Saturne': (1427, 120600 / 149.5978707, 18),
                'Uranus': (2870, 51300 / 149.5978707, 15),
                'Neptune': (4496, 49500 / 149.5978707, 8),
                'Pluton': (5900, 2000 / 149.5978707, 1)}
    print(max(j[1] for j in planetes.values()))
    print("Le planète avec le plus grand diamètre", [i for i in planetes if max(j[1] for j in planetes) in i][0])
    # app = Test.Test()
    # app.run()
