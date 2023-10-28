import random
import tkinter

import Utils
import nsi
import math

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
                                command=lambda: tracer_forme(canvas, *triangle_points[-3:]))
    formButton.pack(side=tkinter.TOP, padx=5, pady=5)
    eraseButton = tkinter.Button(window, text='Effacer', command=lambda: clear_canvas(canvas))
    eraseButton.pack(side=tkinter.TOP, padx=5, pady=5)
    window.mainloop()


def click(event):
    if value.get() == 4:
        canvas.create_oval(event.x - 1, event.y - 1, event.x + 1, event.y + 1, fill='black')
        global triangle_points
        triangle_points.append((event.x, event.y))
        if len(triangle_points) % 3 == 0:
            tracer_triangle(canvas, *triangle_points[-3:])
    else:
        global x, y
        if x == -1:
            x, y = event.x, event.y
        else:
            tracer_forme(canvas, (x, y), (event.x, event.y))
            x, y = -1, -1


def tracer_forme(c: tkinter.Canvas, p1: tuple[int, int] = None, p2: tuple[int, int] = None, p3: tuple[int, int] = None):
    match value.get():
        case 1:
            draw_line(canvas, (
            (random.randint(0, length) if p1 is None else p1[0]), (random.randint(0, length) if p1 is None else p1[1])),
                      ((random.randint(0, length) if p2 is None else p2[0]),
                       (random.randint(0, length) if p2 is None else p2[1])))
        case 2:
            draw_rectangle(canvas, (
            (random.randint(0, length) if p1 is None else p1[0]), (random.randint(0, length) if p1 is None else p1[1])),
                           ((random.randint(0, length) if p2 is None else p2[0]),
                            (random.randint(0, length) if p2 is None else p2[1])))
        case 3:
            draw_circle(canvas, (
            (random.randint(0, length) if p1 is None else p1[0]), (random.randint(0, length) if p1 is None else p1[1])),
                        ((random.randint(0, length) if p2 is None else p2[0]),
                         (random.randint(0, length) if p2 is None else p2[1])))
        case 4:
            if p3 is not None:
                match triangleValue.get():
                    case 1:
                        for coord in Utils.divide_list(Utils.ajust_len_list(triangle_points, 3)[:-3], 3) + [[p1, p2, p3]]:
                            ax, bx, cx, ay, by, cy = coord[0][0], coord[1][0], coord[2][0], coord[0][1], coord[1][1], coord[2][1]
                            d = 2 * (ax * (by - cy) + bx * (cy - ay) + cx * (ay - by))
                            px = ((ax * ax + ay * ay) * (by - cy) + (bx * bx + by * by) * (cy - ay) + (
                                    cx * cx + cy * cy) * (ay - by)) / d
                            py = ((ax * ax + ay * ay) * (cx - bx) + (bx * bx + by * by) * (ax - cx) + (
                                    cx * cx + cy * cy) * (bx - ax)) / d
                            c.create_oval(px - 1, py - 1, px + 1, py + 1, width=2, fill='red', outline='red')
                            r = math.sqrt((px - ax) ** 2 + (py - ay) ** 2)
                            c.create_oval(px - r, py - r, px + r, py + r, width=2, outline='black')


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
    global triangle_points
    c.delete(tkinter.ALL)
    triangle_points = []


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
