import random
import tkinter

import nsi

length = 400
window = tkinter.Tk()
value = tkinter.IntVar()
canvas = tkinter.Canvas(window, bg='grey', height=length, width=length)
x, y = -1, -1


def main():
    value.set(1)
    canvas.pack(side=tkinter.LEFT)
    canvas.bind("<Button-1>", click)
    frame = tkinter.Frame(window, borderwidth=2, relief=tkinter.GROOVE)
    frame.pack(side=tkinter.TOP)
    radiobutton1 = tkinter.Radiobutton(frame, text="Segment", variable=value, value=1)
    radiobutton2 = tkinter.Radiobutton(frame, text="Rectangle", variable=value, value=2)
    radiobutton3 = tkinter.Radiobutton(frame, text="Disque", variable=value, value=3)
    radiobutton1.pack(side=tkinter.TOP, padx=5, pady=5)
    radiobutton2.pack(side=tkinter.TOP, padx=5, pady=5)
    radiobutton3.pack(side=tkinter.TOP, padx=5, pady=5)
    quitButton = tkinter.Button(window, text='Quitter', command=window.quit)
    quitButton.pack(side=tkinter.BOTTOM, padx=5, pady=5)
    formButton = tkinter.Button(window, text='Tracer la forme', command=lambda: tracer_forme())
    formButton.pack(side=tkinter.TOP, padx=5, pady=5)
    eraseButton = tkinter.Button(window, text='Effacer', command=lambda: clear_canvas(canvas))
    eraseButton.pack(side=tkinter.TOP, padx=5, pady=5)
    window.mainloop()


def click(event):
    global x, y
    if x == -1:
        x, y = event.x, event.y
    else:
        tracer_forme(x, y, event.x, event.y)
        x, y = -1, -1


def tracer_forme(x1=random.randint(0, length), y1=random.randint(0, length), x2=random.randint(0, length),
                 y2=random.randint(0, length)):
    if value.get() == 1:
        draw_line(canvas, x1, y1, x2, y2)
    elif value.get() == 2:
        draw_rectangle(canvas, x1, y1, x2, y2)
    else:
        draw_circle(canvas, x1, y1, x2, y2)


def draw_line(canvas: tkinter.Canvas, x1, y1, x2, y2, width=2):
    for i in range(5):
        canvas.create_line(x1, y1, x2, y2, width=width,
                           fill=random.choice(['white', 'black', 'red', 'green', 'blue', 'cyan', 'yellow', 'magenta']))


def draw_rectangle(canvas: tkinter.Canvas, x1, y1, x2, y2, width=2):
    for i in range(5):
        canvas.create_rectangle(x1, y1, x2, y2, width=width,
                                fill=random.choice(
                                    ['white', 'black', 'red', 'green', 'blue', 'cyan', 'yellow', 'magenta']))


def draw_circle(canvas: tkinter.Canvas, x1, y1, x2, y2, width=2):
    for i in range(5):
        canvas.create_oval(x1, y1, x2, y2, width=width,
                           fill=random.choice(['white', 'black', 'red', 'green', 'blue', 'cyan', 'yellow', 'magenta']))


def clear_canvas(canvas: tkinter.Canvas):
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
    planete_max = max(planetes, key=lambda planete: planetes[planete][1])
    print("Le planète avec le plus grand diamètre est", planete_max, "avec un diamètre de", planetes[planete_max][1])
    # app = Test.Test()
    # app.run()
