import random
from lsystem import LSystem
import gui

print("4")


def setColor(color):
    color_code = next((key for key, value in gui.gui.color_names.items() if value == color), None)
    return color_code


def cmd_turtle_fd_f(t, length, *args, factor):
    #print("w", factor)
    color = setColor(gui.gui.comboColorsTrunk1.get())

    t.pencolor(darken_color(color, int(factor)))
    t.pensize(args[1] * float(gui.gui.comboPlantThickness.get()))
    t.fd(length * args[0])
    #print(darken_color(color, factor))


def cmd_turtle_fd_g(t, length, *args, factor):

    color = setColor(gui.gui.comboColorsTrunk2.get())

    t.pencolor(darken_color(color, int(factor)))
    t.pensize(args[1] * float(gui.gui.comboPlantThickness.get()))
    t.fd(length * args[0])



def cmd_turtle_fd_h(t, length, *args, factor):

    color = setColor(gui.gui.comboColorsTrunk3.get())

    t.pencolor(darken_color(color, int(factor)))
    t.pensize(args[1] * float(gui.gui.comboPlantThickness.get()))
    t.fd(length * args[0])






def darken_color(color, factor1):
    r = int(color[1:3], 16)
    g = int(color[3:5], 16)
    b = int(color[5:], 16)

    new_r = max(0, int(r - factor1))
    new_g = max(0, int(g - factor1))
    new_b = max(0, int(b - factor1))

    darkened_color = "#{:02x}{:02x}{:02x}".format(new_r, new_g, new_b)
    #print("darkened_color", darkened_color)

    return darkened_color


def cmd_turtle_fd_standart(t, length, *args, factor):
    t.pencolor(setColor(gui.gui.comboColorsTrunk.get()))
    t.pensize(args[1] * float(gui.gui.comboPlantThickness.get()))
    t.fd(length * args[0])


def cmd_turtle_fd_s(t, length, *args):
    t.penup()  # Поднять перо перед перемещением
    t.fd(length * args[0])  # Перемещение без рисования
    t.pendown()  # Опустить п


def cmd_turtle_fd_bereza(t, length, *args, factor):
    colors = ['#F0F8FF', 'black', '#F0F8FF', '#F0F8FF']  # Список цветов
    t.pensize(args[1] * float(gui.gui.comboPlantThickness.get()))
    for _ in range(30):  # Просто пример, как можно нарисовать 10 отрезков разными цветами
        color = random.choice(colors)  # Случайный выбор цвета из списка
        t.pencolor(color)
        t.fd(length * (args[0] / 30))


def cmd_turtle_left(t, angle, *args):
    t.left(args[0])


def cmd_turtle_right(t, angle, *args):
    t.right(args[0])




def cmd_turtle_segment(t, length, *args):
    # Получаем вероятность и размер листа один раз
    leaf_probability = float(gui.gui.comboPerLeaves3.get())
    leaf_size = float(gui.gui.comboSizeLeaves3.get())
    t.pencolor('#013220')
    # Проверяем, должен ли рисоваться лист
    if random.random() > leaf_probability:
        return
    t.begin_fill()

    # Устанавливаем размер пера для листа
    t.pensize(leaf_size)
    colorIntensity = random.randint(0, 60)
    # Устанавливаем цвет листа
    t.pencolor(darken_color(setColor(gui.gui.comboColorsLeaf3.get()),colorIntensity))




     # Рисуем лист
    t.fd(length // leaf_size)
    t.end_fill()
    # Возвращаем оригинальные цвет и размер пера


def cmd_turtle_list(t, length, *args):
    leaf_probability = float(gui.gui.comboPerLeaves1.get())
    if random.random() > leaf_probability:
        return

    colorIntensity = random.randint(0, 30)
    t.color(darken_color(setColor(gui.gui.comboColorsLeaf1.get()),colorIntensity))
    t.pencolor(darken_color(setColor(gui.gui.comboColorsLeaf1.get()),50))
    t.pensize(1)
    t.begin_fill()
    t.right(45)
    for i in range(2):
        t.circle(length * int(gui.gui.comboSizeLeaves1.get())/4, 90)
        t.circle(length * int(gui.gui.comboSizeLeaves1.get()) / 256, 90)

    t.end_fill()



def cmd_turtle_list_long(t, length, *args):
    leaf_probability = float(gui.gui.comboPerLeaves4.get())
    if random.random() > leaf_probability:
        return
    # Получаем вероятность и размер листа один раз
    colorIntensity = random.randint(0, 30)
    """ Рисуем лист с помощью черепашьей графики """
    t.color(darken_color(setColor(gui.gui.comboColorsLeaf4.get()),colorIntensity))
    t.pencolor(darken_color(setColor(gui.gui.comboColorsLeaf4.get()),50))
    t.pensize(1)
    t.begin_fill()
    t.right(15)
    for i in range(1):
        t.circle(length * int(gui.gui.comboSizeLeaves4.get())*4, 30)
        t.right(210)
        t.circle(length * int(gui.gui.comboSizeLeaves4.get())*4 , 30)
    t.end_fill()







def cmd_turtle_flower(t, length, *args):
    leaf_probability = float(gui.gui.comboPerLeaves2.get())
    if random.random() > leaf_probability:
        return
    # Получаем вероятность и размер листа один раз
    colorIntensity = random.randint(0, 30)
    t.color(darken_color(setColor(gui.gui.comboColorsLeaf2.get()), colorIntensity))
    t.pencolor(darken_color(setColor(gui.gui.comboColorsLeaf2.get()), 50))
    t.pensize(1)
    def petal(t, radius, angle):
        for _ in range(2):
            t.circle(radius, angle)
            t.left(180 - angle)

    # Функция для рисования цветка
    def draw_flower(t, petals, radius, angle, step):
        for _ in range(petals):

            petal(t, radius, angle)
            t.left(step)

    t.begin_fill()
    draw_flower(t, 16, length * int(gui.gui.comboSizeLeaves2.get()) /6, 60, 360 / 10)
    t.end_fill()




def introduced_rules(t):
    if gui.gui.comboObject.get() == "Дерево":
        axiom = gui.gui.entry.get()
        angle = int(gui.gui.comboAngle.get())
        f_len = int(gui.gui.comboSegmentLength.get())
        rule = gui.gui.text.get("1.0", gui.tk.END)

        rule = eval("(" + rule + ")")

        l_sys = LSystem(t, axiom, f_len, angle)

        l_sys.add_rules(*rule)

        rules_move_values = [("G", cmd_turtle_fd_g), ("H", cmd_turtle_fd_h), ("Z", cmd_turtle_flower),
                             ("F", cmd_turtle_fd_f), ("+", cmd_turtle_left),
                             ("-", cmd_turtle_right),
                             ("L", cmd_turtle_list), ("I", cmd_turtle_segment), ("U", cmd_turtle_list_long),
                             ("S", cmd_turtle_fd_s)]

        l_sys.add_rules_move(*rules_move_values)

        # print(l_sys.state)

        l_sys.process_iterations(int(gui.gui.comboDepth.get()))

        l_sys.draw_plant((65, -280), 90)

    if gui.gui.comboObject.get() == "Елка":
        axiom = gui.gui.entry.get()
        angle = int(gui.gui.comboAngle.get())
        f_len = int(gui.gui.comboSegmentLength.get())
        rule = gui.gui.text.get("1.0", gui.tk.END)

        rule = eval("(" + rule + ")")

        l_sys = LSystem(t, axiom, f_len, angle)

        l_sys.add_rules(*rule)

        rules_move_values = [("G", cmd_turtle_fd_g), ("H", cmd_turtle_fd_h), ("Z", cmd_turtle_flower), ("F", cmd_turtle_fd_f), ("+", cmd_turtle_left),
                             ("-", cmd_turtle_right),
                             ("L", cmd_turtle_list), ("I", cmd_turtle_segment), ("U", cmd_turtle_list_long), ("S", cmd_turtle_fd_s)]

        l_sys.add_rules_move(*rules_move_values)

        # print(l_sys.state)

        l_sys.process_iterations(int(gui.gui.comboDepth.get()))

        l_sys.draw_plant((0, -280), 90)



    if gui.gui.comboObject.get() == "Береза":
        axiom = gui.gui.entry.get()
        angle = int(gui.gui.comboAngle.get())
        f_len = int(gui.gui.comboSegmentLength.get())
        rule = gui.gui.text.get("1.0", gui.tk.END)

        rule = eval("(" + rule + ")")

        l_sys = LSystem(t, axiom, f_len, angle)

        l_sys.add_rules(*rule)
        rules_move_values = [("F", cmd_turtle_fd_bereza), ("+", cmd_turtle_left), ("-", cmd_turtle_right),
                             ("L", cmd_turtle_list)]

        l_sys.add_rules_move(*rules_move_values)

        # print(l_sys.state)

        l_sys.process_iterations(int(gui.gui.comboDepth.get()))

        l_sys.draw_plant((0, -280), 90)


    if gui.gui.comboObject.get() == "Олеандр":
        axiom = gui.gui.entry.get()
        angle = int(gui.gui.comboAngle.get())
        f_len = int(gui.gui.comboSegmentLength.get())
        rule = gui.gui.text.get("1.0", gui.tk.END)

        rule = eval("(" + rule + ")")

        l_sys = LSystem(t, axiom, f_len, angle)

        l_sys.add_rules(*rule)


        rules_move_values = [("G", cmd_turtle_fd_g), ("H", cmd_turtle_fd_h), ("Z", cmd_turtle_flower), ("F", cmd_turtle_fd_f), ("+", cmd_turtle_left),
                             ("-", cmd_turtle_right),
                             ("L", cmd_turtle_list), ("I", cmd_turtle_segment), ("U", cmd_turtle_list_long)]

        l_sys.add_rules_move(*rules_move_values)

        # print(l_sys.state)

        l_sys.process_iterations(int(gui.gui.comboDepth.get()))

        l_sys.draw_plant((0, -280), 90)


    if gui.gui.comboObject.get() == "Папоротник":
        axiom = gui.gui.entry.get()
        angle = int(gui.gui.comboAngle.get())
        f_len = int(gui.gui.comboSegmentLength.get())
        rule = gui.gui.text.get("1.0", gui.tk.END)

        rule = eval("(" + rule + ")")

        l_sys = LSystem(t, axiom, f_len, angle)

        l_sys.add_rules(*rule)


        rules_move_values = [("G", cmd_turtle_fd_g), ("H", cmd_turtle_fd_h), ("Z", cmd_turtle_flower), ("F", cmd_turtle_fd_f), ("+", cmd_turtle_left),
                             ("-", cmd_turtle_right),
                             ("L", cmd_turtle_list), ("I", cmd_turtle_segment), ("U", cmd_turtle_list_long)]

        l_sys.add_rules_move(*rules_move_values)

        # print(l_sys.state)

        l_sys.process_iterations(int(gui.gui.comboDepth.get()))

        l_sys.draw_plant((0, -280), 90)


    if gui.gui.comboObject.get() == "Говея":
        axiom = gui.gui.entry.get()
        angle = int(gui.gui.comboAngle.get())
        f_len = int(gui.gui.comboSegmentLength.get())
        rule = gui.gui.text.get("1.0", gui.tk.END)

        rule = eval("(" + rule + ")")

        l_sys = LSystem(t, axiom, f_len, angle)

        l_sys.add_rules(*rule)


        rules_move_values = [("G", cmd_turtle_fd_g), ("H", cmd_turtle_fd_h), ("Z", cmd_turtle_flower), ("F", cmd_turtle_fd_f), ("+", cmd_turtle_left),
                             ("-", cmd_turtle_right),
                             ("L", cmd_turtle_list), ("I", cmd_turtle_segment), ("U", cmd_turtle_list_long)]

        l_sys.add_rules_move(*rules_move_values)

        # print(l_sys.state)

        l_sys.process_iterations(int(gui.gui.comboDepth.get()))

        l_sys.draw_plant((0, -280), 90)

    if gui.gui.comboObject.get() == "Можжевельник":
        axiom = gui.gui.entry.get()
        angle = int(gui.gui.comboAngle.get())
        f_len = int(gui.gui.comboSegmentLength.get())
        rule = gui.gui.text.get("1.0", gui.tk.END)

        rule = eval("(" + rule + ")")

        l_sys = LSystem(t, axiom, f_len, angle)

        l_sys.add_rules(*rule)


        rules_move_values = [("G", cmd_turtle_fd_g), ("H", cmd_turtle_fd_h), ("Z", cmd_turtle_flower), ("F", cmd_turtle_fd_f), ("+", cmd_turtle_left),
                             ("-", cmd_turtle_right),
                             ("L", cmd_turtle_list), ("I", cmd_turtle_segment), ("U", cmd_turtle_list_long)]

        l_sys.add_rules_move(*rules_move_values)

        # print(l_sys.state)

        l_sys.process_iterations(int(gui.gui.comboDepth.get()))

        l_sys.draw_plant((0, -280), 90)

    if gui.gui.comboObject.get() == "Лапчатка":
        axiom = gui.gui.entry.get()
        angle = int(gui.gui.comboAngle.get())
        f_len = int(gui.gui.comboSegmentLength.get())
        rule = gui.gui.text.get("1.0", gui.tk.END)

        rule = eval("(" + rule + ")")

        l_sys = LSystem(t, axiom, f_len, angle)

        l_sys.add_rules(*rule)


        rules_move_values = [("G", cmd_turtle_fd_g), ("H", cmd_turtle_fd_h), ("Z", cmd_turtle_flower), ("F", cmd_turtle_fd_f), ("+", cmd_turtle_left),
                             ("-", cmd_turtle_right),
                             ("L", cmd_turtle_list), ("I", cmd_turtle_segment), ("U", cmd_turtle_list_long)]

        l_sys.add_rules_move(*rules_move_values)

        # print(l_sys.state)

        l_sys.process_iterations(int(gui.gui.comboDepth.get()))

        l_sys.draw_plant((0, -280), 90)


    if gui.gui.comboObject.get() == "Пальма":
        axiom = gui.gui.entry.get()
        angle = int(gui.gui.comboAngle.get())
        f_len = int(gui.gui.comboSegmentLength.get())
        rule = gui.gui.text.get("1.0", gui.tk.END)

        rule = eval("(" + rule + ")")

        l_sys = LSystem(t, axiom, f_len, angle)

        l_sys.add_rules(*rule)


        rules_move_values = [("G", cmd_turtle_fd_g), ("H", cmd_turtle_fd_h), ("Z", cmd_turtle_flower), ("F", cmd_turtle_fd_f), ("+", cmd_turtle_left),
                             ("-", cmd_turtle_right),
                             ("L", cmd_turtle_list), ("I", cmd_turtle_segment), ("U", cmd_turtle_list_long)]

        l_sys.add_rules_move(*rules_move_values)

        # print(l_sys.state)

        l_sys.process_iterations(int(gui.gui.comboDepth.get()))

        l_sys.draw_plant((0, -280), 90)





    if gui.gui.comboObject.get() == "Лаванда":
        axiom = gui.gui.entry.get()
        angle = int(gui.gui.comboAngle.get())
        f_len = int(gui.gui.comboSegmentLength.get())
        rule = gui.gui.text.get("1.0", gui.tk.END)

        rule = eval("(" + rule + ")")

        l_sys = LSystem(t, axiom, f_len, angle)

        l_sys.add_rules(*rule)


        rules_move_values = [("G", cmd_turtle_fd_g), ("H", cmd_turtle_fd_h), ("Z", cmd_turtle_flower), ("F", cmd_turtle_fd_f), ("+", cmd_turtle_left),
                             ("-", cmd_turtle_right),
                             ("L", cmd_turtle_list), ("I", cmd_turtle_segment), ("U", cmd_turtle_list_long), ("S", cmd_turtle_fd_s)]

        l_sys.add_rules_move(*rules_move_values)

        # print(l_sys.state)

        l_sys.process_iterations(int(gui.gui.comboDepth.get()))

        l_sys.draw_plant((0, -280), 90)

    if gui.gui.comboObject.get() == "Сосна":
        axiom = gui.gui.entry.get()
        angle = int(gui.gui.comboAngle.get())
        f_len = int(gui.gui.comboSegmentLength.get())
        rule = gui.gui.text.get("1.0", gui.tk.END)

        rule = eval("(" + rule + ")")

        l_sys = LSystem(t, axiom, f_len, angle)

        l_sys.add_rules(*rule)


        rules_move_values = [("G", cmd_turtle_fd_g), ("H", cmd_turtle_fd_h), ("Z", cmd_turtle_flower), ("F", cmd_turtle_fd_f), ("+", cmd_turtle_left),
                             ("-", cmd_turtle_right),
                             ("L", cmd_turtle_list), ("I", cmd_turtle_segment), ("U", cmd_turtle_list_long), ("S", cmd_turtle_fd_s)]

        l_sys.add_rules_move(*rules_move_values)

        # print(l_sys.state)

        l_sys.process_iterations(int(gui.gui.comboDepth.get()))

        l_sys.draw_plant((0, -280), 90)



    # Example usage:

