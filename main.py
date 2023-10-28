import random
import tkinter

import nsi

length = 400
window = tkinter.Tk()
value = tkinter.IntVar()
triangleValue = tkinter.IntVar()
canvas = tkinter.Canvas(window, bg='grey', height=length, width=length)
x, y = -1, -1
triangle_points = []


def main():
    value.set(1)
    triangleValue.set(1)
    canvas.pack(side=tkinter.LEFT)
    canvas.bind("<Button-1>", click)
    frame = tkinter.Frame(window, borderwidth=2, relief=tkinter.GROOVE)
    frame.pack(side=tkinter.TOP)
    triangleFrame = tkinter.Frame(window, borderwidth=2, relief=tkinter.GROOVE)
    radiobutton1 = tkinter.Radiobutton(frame, text="Segment", variable=value, value=1,
                                       command=lambda f=triangleFrame: toggle_widget(f))
    radiobutton1.pack(side=tkinter.TOP, padx=5, pady=5)
    radiobutton2 = tkinter.Radiobutton(frame, text="Rectangle", variable=value, value=2,
                                       command=lambda f=triangleFrame: toggle_widget(f))
    radiobutton2.pack(side=tkinter.TOP, padx=5, pady=5)
    radiobutton3 = tkinter.Radiobutton(frame, text="Disque", variable=value, value=3,
                                       command=lambda f=triangleFrame: toggle_widget(f))
    radiobutton3.pack(side=tkinter.TOP, padx=5, pady=5)
    radiobutton4 = tkinter.Radiobutton(frame, text="Triangle", variable=value, value=4,
                                       command=lambda f=triangleFrame: toggle_widget(f))
    radiobutton4.pack(side=tkinter.TOP, padx=5, pady=5)
    triangleButton1 = tkinter.Radiobutton(triangleFrame, text='Circoncentre', variable=triangleValue, value=1)
    triangleButton1.pack(side=tkinter.TOP, padx=5, pady=5)
    triangleButton2 = tkinter.Radiobutton(triangleFrame, text='Circonscrit', variable=triangleValue, value=2)
    triangleButton2.pack(side=tkinter.TOP, padx=5, pady=5)
    triangleButton3 = tkinter.Radiobutton(triangleFrame, text='Centroïde', variable=triangleValue, value=3)
    triangleButton3.pack(side=tkinter.TOP, padx=5, pady=5)
    triangleButton4 = tkinter.Radiobutton(triangleFrame, text='Orthocentre', variable=triangleValue, value=4)
    triangleButton4.pack(side=tkinter.TOP, padx=5, pady=5)
    quitButton = tkinter.Button(window, text='Quitter', command=window.quit)
    quitButton.pack(side=tkinter.BOTTOM, padx=5, pady=5)
    formButton = tkinter.Button(window, text='Tracer la forme',
                                command=lambda: tracer_forme((random.randint(0, length), random.randint(0, length)),
                                                             (random.randint(0, length), random.randint(0, length))))
    formButton.pack(side=tkinter.TOP, padx=5, pady=5)
    eraseButton = tkinter.Button(window, text='Effacer', command=lambda: clear_canvas(canvas))
    eraseButton.pack(side=tkinter.TOP, padx=5, pady=5)
    window.mainloop()


def click(event):
    if value.get() == 4:
        canvas.create_oval(event.x - 1, event.y - 1, event.x + 1, event.y + 1, fill='black')
        global triangle_points
        if len(triangle_points) == 2:
            tracer_triangle(canvas, *triangle_points, (event.x, event.y))
            triangle_points = []
        else:
            triangle_points.append((event.x, event.y))
    else:
        global x, y
        if x == -1:
            x, y = event.x, event.y
        else:
            tracer_forme((x, y), (event.x, event.y))
            x, y = -1, -1


def tracer_forme(p1: tuple[int, int], p2: tuple[int, int]):
    match value.get():
        case 1:
            draw_line(canvas, p1, p2)
        case 2:
            draw_rectangle(canvas, p1, p2)
        case 3:
            draw_circle(canvas, p1, p2)


def toggle_widget(widget: tkinter.Widget, **kwargs):
    if value.get() == 4:
        widget.pack(kwargs)
    else:
        widget.pack_forget()


def tracer_triangle(c: tkinter.Canvas, p1: tuple[int, int], p2: tuple[int, int], p3: tuple[int, int], width=2):
    c.create_line(*p1, *p2, width=2, fill='black')
    c.create_line(*p2, *p3, width=2, fill='black')
    c.create_line(*p1, *p3, width=2, fill='black')


def draw_line(c: tkinter.Canvas, p1: tuple[int, int], p2: tuple[int, int], width=2):
    for i in range(5):
        c.create_line(*p1, *p2, width=width,
                      fill=random.choice(['white', 'black', 'red', 'green', 'blue', 'cyan', 'yellow', 'magenta']))


def draw_rectangle(c: tkinter.Canvas, p1: tuple[int, int], p2: tuple[int, int], width=2):
    for i in range(5):
        c.create_rectangle(*p1, *p2, width=width,
                           fill=random.choice(
                               ['white', 'black', 'red', 'green', 'blue', 'cyan', 'yellow', 'magenta']))


def draw_circle(c: tkinter.Canvas, p1: tuple[int, int], p2: tuple[int, int], width=2):
    for i in range(5):
        c.create_oval(*p1, *p2, width=width,
                      fill=random.choice(['white', 'black', 'red', 'green', 'blue', 'cyan', 'yellow', 'magenta']))


def clear_canvas(c: tkinter.Canvas):
    c.delete(tkinter.ALL)


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
