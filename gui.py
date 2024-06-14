import os
from tkinter import *
import tkinter as tk
from tkinter import ttk, filedialog
from functools import partial
from tkinter import Canvas
import turtle
import random
from PIL import ImageGrab
from PIL import Image, ImageTk
import io

import pymsgbox
print("1")
from rules import introduced_rules
from saveFile import save_parameters_to_file
from savePNG import save_canvas_as_png
print("2")


# from rules import creating_fractal
class Gui:
    def __init__(self):

        self.create_root()
        self.create_notebook()
        self.create_combobox_tab1()


    def create_root(self):

        self.root = tk.Tk()

        self.root.title('Procedural generation plant')
        #self.root.geometry('1450x965')
        self.root.tk.call('tk', 'scaling', 1.0)
        self.root.columnconfigure(0, weight=1)
        self.root.rowconfigure(0, weight=1)
        self.root.resizable(False, False)
        self.screen_width = self.root.winfo_screenwidth()
        self.screen_height = self.root.winfo_screenheight()
        self.root.minsize(1500, 1000)

        self.width_scale = self.screen_width / 1500  # коэффициент масштабирования по ширине
        self.height_scale = self.screen_height / 1000  # коэффициент масштабирования по высоте

        new_width = int((1500 * self.width_scale)/1.2)
        new_height = int((1000 * self.height_scale)/1.2)
        self.root.geometry(f'{new_width}x{new_height}')  # установка новых размеров окна

        # Пример для масштабирования canvas:





        self.canvas = Canvas(master=self.root, width=new_width, height=new_height)
        self.canvas.config(bg='grey')
        self.canvas.grid(row=0, column=0, columnspan=50, rowspan=20, sticky='news')
        #self.canvas.scale("all", 110, 110, 111, 1111)
        self.screen = turtle.TurtleScreen(self.canvas)
        self.screen.bgcolor("lightblue")

        self.t = turtle.RawTurtle(self.screen)

        self.t.hideturtle()
        self.t.penup()
        self.t.left(90)
        self.t.pendown()
        # self.t.screen.tracer(0, 0)

        self.canvas.config( relief="solid", highlightbackground="lightblue")


    def create_notebook(self):

        self.notebook = ttk.Notebook(self.root)
        self.notebook.grid(row=20, column=0, columnspan=50, sticky='we', padx=4, pady=4)

        self.tab1 = tk.Frame(self.notebook, width=1500, height=200)
        self.tab2 = tk.Frame(self.notebook, width=1500, height=200)
        #self.tab3 = tk.Frame(self.notebook, width=1600, height=200)
        self.tab1.grid_rowconfigure(0, weight=1)  # Растягивание строки 0
        self.tab1.grid_columnconfigure(0, weight=1)  # Растягивание столбца 0
        self.tab2.grid_rowconfigure(0, weight=1)  # Растягивание строки 0
        self.tab2.grid_columnconfigure(0, weight=1)  # Растягивание столбца 0
        self.notebook.add(self.tab1, text="Построение растений")
        self.notebook.add(self.tab2, text="Инструкция")



    def create_combobox_tab1(self):

        label = ttk.Label(self.tab1, text="Вид растения:")
        label.grid(row=22, column=20, sticky='ws', padx=4, pady=4)
        self.object_f = ('Береза',  'Олеандр','Сосна' ,'Елка', 'Дерево', 'Папоротник','Пальма','Можжевельник','Говея','Лапчатка','Лаванда')
        self.comboObject = ttk.Combobox(self.tab1, values=self.object_f)
        self.comboObject.grid(row=23, column=20, sticky='n', padx=4, pady=4)

        label = ttk.Label(self.tab1, text="Поколение фрактала:")
        label.grid(row=21, column=1, sticky='ws', padx=4, pady=4)
        depth = ('1', '2', '3', '4', '5', '6', '7', '8', '9', '10','11','12','13','14','15','16')
        self.comboDepth = ttk.Combobox(self.tab1, values=depth)
        self.comboDepth.grid(row=21, column=2, sticky='n', padx=4, pady=4)

        label = ttk.Label(self.tab1, text="Длина сегмента прямой:")
        label.grid(row=22, column=1, sticky='ws', padx=4, pady=4)
        segmentLength = (
            '0', '1', '2','3', '4','5', '10', '15', '20', '25', '30', '35', '40', '45', '50', '55', '60', '65', '70', '75', '80')
        self.comboSegmentLength = ttk.Combobox(self.tab1, values=segmentLength)
        self.comboSegmentLength.grid(row=22, column=2, sticky='n', padx=4, pady=4)

        label = ttk.Label(self.tab1, text="Угол наклона:")
        label.grid(row=23, column=1, sticky='ws', padx=4, pady=4)
        tiltAngle = ('0', '5', '10', '15', '20', '25', '30', '35', '40', '45', '50', '55', '60', '65', '70', '75', '80', '85', '90', '95', '100', '110', '120', '180',)
        self.comboAngle = ttk.Combobox(self.tab1, values=tiltAngle)
        self.comboAngle.grid(row=23, column=2, sticky='n', padx=4, pady=4)

        label = ttk.Label(self.tab1, text="Толщина растения:")
        label.grid(row=24, column=1, sticky='ws', padx=4, pady=4)
        self.depthPlantThickness = (
            '1.0', '1.15', '1.25', '1.50', '1.75', '1.85', '2', '2.15', '2.25', '2.50', '2.75', '2.85', '3')
        self.comboPlantThickness = ttk.Combobox(self.tab1, values=self.depthPlantThickness)
        self.comboPlantThickness.grid(row=24, column=2, sticky='n', padx=4, pady=4)



        self.color_names = {
            '#00AF64': 'Зеленый',
            '#218359': 'Темно-зеленый',
            '#007241': 'Светло-зеленый',
            '#EBC763': 'Желтый',
            '#D7AB31': 'Темно-желтый',
            '#8F4D00': 'Коричневый',
            '#673700': 'Темно-коричневый',
            '#FF0D00': 'Красный',
            '#B00000': 'Темно-красный',
            '#D936C0': 'Розовый',
            '#872277': 'Темно-розовый',
            '#e178ff': 'Светло-розовый',
            '#57316B': 'Фиолетовый',
            '#009D92': 'Голубой',
            '#00665F': 'Темно-голубой',
            '#33CEC3': 'Светло-голубой',
            '#284A7E': 'Синий',
            'black': 'Черный',
            'white': 'Белый',
            '#F8F4FF': 'Белый (Магнолия)',
            '#C0C0C0': 'Серый',
            '#696969': 'Темно-серый',
            '#708090': 'Шиферно-серый',
        }

        label = ttk.Label(self.tab1, text="Цвет сигмента F:")

        label.grid(row=25, column=1, sticky=' ws', padx=4, pady=4)
        self.russian_color_names = list(self.color_names.values())
        self.comboColorsTrunk1 = ttk.Combobox(self.tab1, values=self.russian_color_names)
        self.comboColorsTrunk1.grid(row=25, column=2, sticky='n', padx=4, pady=4)

        label = ttk.Label(self.tab1, text="Цвет сигмента G:")

        label.grid(row=26, column=1, sticky=' ws', padx=4, pady=4)
        self.russian_color_names = list(self.color_names.values())
        self.comboColorsTrunk2 = ttk.Combobox(self.tab1, values=self.russian_color_names)
        self.comboColorsTrunk2.grid(row=26, column=2, sticky='n', padx=4, pady=4)

        label = ttk.Label(self.tab1, text="Цвет сигмента H:")

        label.grid(row=27, column=1, sticky=' ws', padx=4, pady=4)
        self.russian_color_names = list(self.color_names.values())
        self.comboColorsTrunk3 = ttk.Combobox(self.tab1, values=self.russian_color_names)
        self.comboColorsTrunk3.grid(row=27, column=2, sticky='n', padx=4, pady=4)







        label = ttk.Label(self.tab1, text="Название")
        label.grid(row=21, column=3, sticky=' ws', padx=4, pady=4)

        label = ttk.Label(self.tab1, text="Цвет")
        label.grid(row=21, column=4, sticky=' ws', padx=4, pady=4)

        label = ttk.Label(self.tab1, text="Размер")
        label.grid(row=21, column=5, sticky=' ws', padx=4, pady=4)

        label = ttk.Label(self.tab1, text="Вероятность")
        label.grid(row=21, column=6, sticky=' ws', padx=4, pady=4)

        label = ttk.Label(self.tab1, text="Лист")
        label.grid(row=22, column=3, sticky=' ws', padx=4, pady=4)

        self.russian_color_names = list(self.color_names.values())
        self.comboColorsLeaf1 = ttk.Combobox(self.tab1, values=self.russian_color_names)
        self.comboColorsLeaf1.grid(row=22, column=4, sticky='n', padx=4, pady=4)

        label = ttk.Label(self.tab1, text="Цветок")
        label.grid(row=23, column=3, sticky=' ws', padx=4, pady=4)
        self.russian_color_names = list(self.color_names.values())
        self.comboColorsLeaf2 = ttk.Combobox(self.tab1, values=self.russian_color_names)
        self.comboColorsLeaf2.grid(row=23, column=4, sticky='n', padx=4, pady=4)

        label = ttk.Label(self.tab1, text="Хвоя")
        label.grid(row=24, column=3, sticky=' ws', padx=4, pady=4)
        self.russian_color_names = list(self.color_names.values())
        self.comboColorsLeaf3 = ttk.Combobox(self.tab1, values=self.russian_color_names)
        self.comboColorsLeaf3.grid(row=24, column=4, sticky='n', padx=4, pady=4)

        label = ttk.Label(self.tab1, text="Большой лист")
        label.grid(row=25, column=3, sticky=' ws', padx=4, pady=4)
        self.russian_color_names = list(self.color_names.values())
        self.comboColorsLeaf4 = ttk.Combobox(self.tab1, values=self.russian_color_names)
        self.comboColorsLeaf4.grid(row=25, column=4, sticky='n', padx=4, pady=4)

        # label = ttk.Label(self.tab1, text="Размер листа 1:")
        # label.grid(row=25, column=3, sticky='ws', padx=4, pady=4)
        self.depthSizeLeaves = (
            '1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14', '15', '20')

        self.comboSizeLeaves1 = ttk.Combobox(self.tab1, values=self.depthSizeLeaves)
        self.comboSizeLeaves1.grid(row=22, column=5, sticky='n', padx=4, pady=4)

        # label = ttk.Label(self.tab1, text="Размер листа 2 :")
        # label.grid(row=26, column=3, sticky='ws', padx=4, pady=4)

        self.comboSizeLeaves2 = ttk.Combobox(self.tab1, values=self.depthSizeLeaves)
        self.comboSizeLeaves2.grid(row=23, column=5, sticky='n', padx=4, pady=4)

        # label = ttk.Label(self.tab1, text="Размер листа 3:")
        # label.grid(row=27, column=3, sticky='ws', padx=4, pady=4)

        self.comboSizeLeaves3 = ttk.Combobox(self.tab1, values=self.depthSizeLeaves)
        self.comboSizeLeaves3.grid(row=24, column=5, sticky='n', padx=4, pady=4)

        self.comboSizeLeaves4 = ttk.Combobox(self.tab1, values=self.depthSizeLeaves)
        self.comboSizeLeaves4.grid(row=25, column=5, sticky='n', padx=4, pady=4)

        # label = ttk.Label(self.tab1, text="Количество листвы:")
        # label.grid(row=21, column=6, sticky='ws', padx=4, pady=4)
        depthPerLeaves = ('0.0', '0.15', '0.25', '0.50', '0.75', '0.85', '1')
        self.comboPerLeaves1 = ttk.Combobox(self.tab1, values=depthPerLeaves)
        self.comboPerLeaves1.grid(row=22, column=6, sticky='n', padx=4, pady=4)

        self.comboPerLeaves2 = ttk.Combobox(self.tab1, values=depthPerLeaves)
        self.comboPerLeaves2.grid(row=23, column=6, sticky='n', padx=4, pady=4)

        self.comboPerLeaves3 = ttk.Combobox(self.tab1, values=depthPerLeaves)
        self.comboPerLeaves3.grid(row=24, column=6, sticky='n', padx=4, pady=4)

        self.comboPerLeaves4 = ttk.Combobox(self.tab1, values=depthPerLeaves)

        self.comboPerLeaves4.grid(row=25, column=6, sticky='n', padx=4, pady=4)



        sampleAxiom = 'A'
        sampleRule = ('("A", f"F(1, 1)[+({angle})A][-({angle})A]A", 0.5),\n'
                      '("A", f"F(1, 1)[++({angle})A][+({angle})A][-({angle})A][--({angle})A]", 0.4),\n'
                      '("A", f"F(1, 1)[-({angle})A]", 0.05),\n'
                      '("A", f"F(1, 1)[+({angle})A]", 0.05),\n'
                      '("F(x, y)", lambda x, y: f"F({(1.2+random.triangular(-0.1, 0.1, random.gauss(0, 0.1)))*x}, {1.5*y})"),\n'
                      '("+(x)", lambda x: f"+({x + random.triangular(-10, 10, random.gauss(0, 2))})"),\n'
                      '("-(x)", lambda x: f"-({x + random.triangular(-10, 10, random.gauss(0, 2))})"),\n')

        self.label = ttk.Label(self.tab1, text="Введите аксиому:")
        self.label.grid(row=21, column=0, sticky='ws', padx=4, pady=4)
        self.entry = Entry(self.tab1, width=80, font=("Arial", 12))  # Установка ширины виджета
        self.entry.insert(tk.END, sampleAxiom)
        self.entry.grid(row=22, column=0, sticky='we', padx=4, pady=4)

        # def on_undo(event):
        #   print("s")
        #  text.edit_undo()
        #   text.event_generate("<<Undo>>")

        label = ttk.Label(self.tab1, text="Введите правило:")
        label.grid(row=23, column=0, sticky='ws', padx=4, pady=4)
        self.text = Text(self.tab1, height=7, width=80, font=("Arial", 12), undo=True)

        self.text.insert(tk.END, sampleRule)
        self.text.grid(row=24, column=0, rowspan=20, sticky='we', padx=4, pady=4)
        # text.bind("<Control-z>", on_undo)

        self.btn_change = Button(master=self.tab1, text='Построить растение',
                                 command=lambda: introduced_rules(self.t))







        self.btn_change.configure(bg='#5EC4CD')
        self.btn_change.config(state='disabled')
        self.btn_change.grid(row=21, column=20, sticky='swen', padx=4, pady=4)




        print(self.comboColorsTrunk2.get())
        print(self.comboColorsTrunk2.get())



        self.btn_change1 = Button(master=self.tab1, text='Сохранить правило в файл',
                                 command=lambda: save_parameters_to_file('plant_parameters.txt'))



        self.btn_change1.configure(bg='#5EC4CD')
        self.btn_change1.config(state='disabled')
        self.btn_change1.grid(row=24, column=20, sticky='swen', padx=4, pady=4)

        self.btn_save_image = tk.Button(self.tab1, text="Сохранить как PNG", command=lambda: save_canvas_as_png(self))
        self.btn_save_image.grid(row=25, column=20, sticky='swen', padx=4, pady=4)
        self.btn_save_image.configure(bg='#5EC4CD')




        self.comboDepth.config(state='disabled')
        self.comboSegmentLength.config(state='disabled')
        self.comboAngle.config(state='disabled')
        self.comboPlantThickness.config(state='disabled')
        self.comboColorsTrunk1.config(state='disabled')
        self.comboColorsTrunk2.config(state='disabled')
        self.comboColorsTrunk3.config(state='disabled')
        self.comboColorsLeaf1.config(state='disabled')
        self.comboColorsLeaf2.config(state='disabled')
        self.comboColorsLeaf3.config(state='disabled')
        self.comboColorsLeaf4.config(state='disabled')
        self.comboSizeLeaves1.config(state='disabled')
        self.comboSizeLeaves2.config(state='disabled')
        self.comboSizeLeaves3.config(state='disabled')
        self.comboSizeLeaves4.config(state='disabled')
        self.comboPerLeaves1.config(state='disabled')
        self.comboPerLeaves2.config(state='disabled')
        self.comboPerLeaves3.config(state='disabled')
        self.comboPerLeaves4.config(state='disabled')

        self.comboObject.bind("<<ComboboxSelected>>", self.on_template_selected)




    # self.check_var_animation = BooleanVar()
    # self.check_button = tk.Checkbutton(self.root, text="Анимация рисования", variable=self.check_var_animation)
    # self.check_button.grid(row=22, column=20, sticky='w', padx=4, pady=4)

    def run(self):
        self.root.mainloop()


    def on_template_selected(self, event):
        self.btn_change1.config(state='normal')

        self.comboColorsTrunk1.config(state='readonly')
        self.comboColorsTrunk2.config(state='readonly')
        self.comboColorsTrunk3.config(state='readonly')
        self.comboDepth.config(state='readonly')
        self.comboSegmentLength.config(state='readonly')
        self.comboAngle.config(state='readonly')
        self.comboPlantThickness.config(state='readonly')
        self.comboColorsTrunk1.config(state='readonly')
        self.comboColorsTrunk2.config(state='readonly')
        self.comboColorsTrunk3.config(state='readonly')
        self.comboColorsLeaf1.config(state='readonly')
        self.comboColorsLeaf2.config(state='readonly')
        self.comboColorsLeaf3.config(state='readonly')
        self.comboColorsLeaf4.config(state='readonly')
        self.comboSizeLeaves1.config(state='readonly')
        self.comboSizeLeaves2.config(state='readonly')
        self.comboSizeLeaves3.config(state='readonly')
        self.comboSizeLeaves4.config(state='readonly')
        self.comboPerLeaves1.config(state='readonly')
        self.comboPerLeaves2.config(state='readonly')
        self.comboPerLeaves3.config(state='readonly')
        self.comboPerLeaves4.config(state='readonly')
        self.btn_change.config(state='normal')
        selected_template = gui.comboObject.get()
        # кол-во листвы
        if selected_template == 'Береза':
            self.entry.delete(0, tk.END)
            self.text.delete("1.0", tk.END)

            sampleAxiom = 'L'
            sampleRule = ('("L", f"F(1, 1)[+({angle})L][-({angle})L]", 0.5),\n'
                          '("L", f"F(1, 1)[++({angle})L][+({angle})L][-({angle})L][--({angle})L]", 0.4),\n'
                          '("L", f"F(1, 1)[-({angle})L]", 0.05),\n'
                          '("L", f"F(1, 1)[+({angle})L]", 0.05),\n'
                          '("F(x, y)", lambda x, y: f"F({(1.2+random.triangular(-0.1, 0.1, random.gauss(0, 0.1)))*x}, {1.5*y})"),\n'
                          '("+(x)", lambda x: f"+({x + random.triangular(-5, 5, random.gauss(0, 2))})"),\n'
                          '("-(x)", lambda x: f"-({x + random.triangular(-5, 5, random.gauss(0, 2))})"),\n')

            self.entry.insert(tk.END, sampleAxiom)
            self.text.insert(tk.END, sampleRule)

            self.comboColorsTrunk1.config(state='disabled')
            self.comboColorsTrunk2.config(state='disabled')
            self.comboColorsTrunk3.config(state='disabled')

            self.comboSegmentLength.set('35')  # устанавливаем длину сегмента
            self.comboAngle.set('25')  # устанавливаем угол наклона
            self.comboDepth.set('7')  # устанавливаем поколение фрактала
            self.comboSizeLeaves1.set('2')  # размер листа
            self.comboSizeLeaves2.set('')  # размер листа
            self.comboSizeLeaves3.set('')  # размер листа
            self.comboSizeLeaves3.set('')  # размер листа
            self.comboPlantThickness.set('1')
            self.comboColorsLeaf1.set('Зеленый')
            self.comboColorsLeaf2.set('')
            self.comboColorsLeaf3.set('')
            self.comboColorsLeaf4.set('')
            self.comboPerLeaves1.set('1')
            self.comboPerLeaves2.set('')
            self.comboPerLeaves3.set('')
            self.comboPerLeaves4.set('')
            # Другие параметры тоже можно установить здесь
        # Добавьте аналогичные проверки для других вариантов фракталов

        if selected_template == 'Елка':
            self.entry.delete(0, tk.END)
            self.text.delete("1.0", tk.END)

            sampleAxiom = 'A'
            sampleRule = (
                '("A", f" [G(0.2, 0.5)[G(0.2, 0.5)]G(0.4, 0.5)A][S(0.2, 0.5)[+({angle})G(0.2, 0.5)[I]B ][-({angle})G(0.2, 0.5)[I]D ][-({angle})+({angle})[I]Q]S(0.2, 0.5)]"),\n'
                '("Q", f"[G(0.1, 0.5)[G(0.2, 0.5)Q]G(0.3, 0.5)Q][S(0.1, 0.5)[+({angle})G(0.1, 0.5)[I]R ][-({angle})G(0.1, 0.5)[I]R ][-({angle})+({angle}) ]S(0.1, 0.5)] "),\n'
                '("D",  f"+({30})[+({angle - 70})[I]A ] [-({angle - 70})A[I]]F(0.2, 0.5)[I]A "),\n'
                '("B", f"-({30})[+({angle - 70})[I]A ] [-({angle - 70})A[I]]F(0.2, 0.5)[I]A "),\n'
                '("R", f"[+({angle - 70})[I]Q ] [-({angle - 70})A]F(0.2, 0.5)[I]Q "),\n'
                '("F(x, y)", lambda x, y: f"F({x * 1.9}, {y + 1.9})"),\n'
                '("G(x, y)", lambda x, y: f"G({x * 1.9}, {y + 1.9})"),\n'
                '("S(x, y)", lambda x, y: f"S({x * 1.9}, {y + 1.9})"),\n'
                
                '("+(x)", lambda x: f"+({x + random.triangular(-5, 5, random.gauss(0, 2))})"),\n'
                '("-(x)", lambda x: f"-({x + random.triangular(-5, 5, random.gauss(0, 2))})"),\n')

            self.entry.insert(tk.END, sampleAxiom)
            self.text.insert(tk.END, sampleRule)

            self.comboSegmentLength.set('20')  # устанавливаем длину сегмента
            self.comboAngle.set('45')  # устанавливаем угол наклона
            self.comboDepth.set('6')  # устанавливаем поколение фрактала
            self.comboSizeLeaves1.set('')  # размер листа
            self.comboSizeLeaves2.set('')  # размер листа
            self.comboSizeLeaves3.set('2')  # размер листа
            self.comboSizeLeaves4.set('')  # размер листа
            self.comboPlantThickness.set('1')
            self.comboColorsLeaf1.set('')
            self.comboColorsLeaf2.set('')
            self.comboColorsLeaf3.set('Светло-зеленый')
            self.comboColorsLeaf4.set('')
            self.comboColorsTrunk1.set('Темно-коричневый')
            self.comboColorsTrunk2.set('Темно-коричневый')
            self.comboColorsTrunk3.set('Темно-коричневый')
            self.comboPerLeaves1.set('')
            self.comboPerLeaves2.set('')
            self.comboPerLeaves3.set('1')
            self.comboPerLeaves4.set('')

        if selected_template == 'Олеандр':
            self.entry.delete(0, tk.END)
            self.text.delete("1.0", tk.END)
            sampleAxiom = 'H'
            sampleRule = (
                '("H", f"G(0.5, 2)[+({angle-8})F(1, 1)][-({angle-8})F(1, 1)][ F(1, 1)]"),\n'
                '("F", f"-({1})F(1, 1)+({angle})-({angle})[+({angle})F(1, 1)LLLLLLLLZ]F(0.5, 1)[-({angle})F(1, 1)U]",0.5),\n'
                '("F", f"-({1})F(1, 1)+({angle})-({angle})[+({angle})F(1, 1)U]F(0.5, 1)[-({angle})F(1, 1)LLLLLLLLZ]F(0.6, 1)",0.5),\n'
                '("H(x, y)", lambda x, y: f"H({1 * x}, {1.7 * y}) "),\n'
                '("F(x, y)", lambda x, y: f"F({1 * x}, {1.7 * y}) "),\n'
                '("G(x, y)", lambda x, y: f"G({1 * x}, {1 * y}) "),\n'
                '("+(x)", lambda x: f"+({x + random.triangular(0, 2, random.gauss(0, 1))})"),\n'
                '("-(x)", lambda x: f"-({x + random.triangular(0, 2, random.gauss(0, 1))})"),\n')

            self.entry.insert(tk.END, sampleAxiom)
            self.text.insert(tk.END, sampleRule)

            self.comboSegmentLength.set('30')  # устанавливаем длину сегмента
            self.comboAngle.set('20')  # устанавливаем угол наклона
            self.comboDepth.set('4')  # устанавливаем поколение фрактала
            self.comboSizeLeaves1.set('1')  # размер листа
            self.comboSizeLeaves2.set('1')  # размер листа
            self.comboSizeLeaves3.set('2')  # размер листа
            self.comboSizeLeaves4.set('1')  # размер листа
            self.comboPlantThickness.set('3')
            self.comboColorsLeaf1.set('Светло-розовый')
            self.comboColorsLeaf2.set('Розовый')
            self.comboColorsLeaf3.set('')
            self.comboColorsLeaf4.set('Светло-зеленый')
            self.comboColorsTrunk1.set('Светло-зеленый')
            self.comboColorsTrunk2.set('Светло-зеленый')
            self.comboColorsTrunk3.set('Светло-зеленый')
            self.comboPerLeaves1.set('1')
            self.comboPerLeaves2.set('1')
            self.comboPerLeaves3.set('1')
            self.comboPerLeaves4.set('1')

        if selected_template == 'Папоротник':
            self.entry.delete(0, tk.END)
            self.text.delete("1.0", tk.END)
            sampleAxiom = 'T'
            sampleRule = (
                '("T", f" F(1, 1)[+({angle+20})F(1, 1)V][ F(5, 1)Q][-({angle+40})F(1, 1)Q] "),\n'
                '("Q", f"-({6})F(1, 1)[+({angle+30})XL][-({angle+30})YL]F(1, 1)[+({angle+30})XL][-({angle+30})YL]Q"),\n'
                '("V", f"+({6})F(1, 1)[+({angle+30})XL][-({angle+30})YL]F(1, 1)[+({angle+30})XL][-({angle+30})YL]V"),\n'
                '("X", f"+({1})H(0.1, 1)[+({angle+30})EL][-({angle+30})EL]H(0.1, 1)X"),\n'
                '("Y", f"-({1})H(0.1, 1)[+({angle+30})EL][-({angle+30})EL]H(0.1, 1)Y"),\n'
                '("E", f"G(0.2, 1)[+({angle+30})L][-({angle+30})L]G(0.2, 1)E"),\n'
                '("H(x, y)", lambda x, y: f"H({1}, {1 * y}) "),\n'
                '("F(x, y)", lambda x, y: f"F({ x + 0.6}, {1.1 * y}) "),\n'
                '("G(x, y)", lambda x, y: f"G({1 * x}, {1 * y}) "),\n'
                '("+(x)", lambda x: f"+({x + random.triangular(0, 2, random.gauss(0, 1))})"),\n'
                '("-(x)", lambda x: f"-({x + random.triangular(0, 2, random.gauss(0, 1))})"),\n')

            self.entry.insert(tk.END, sampleAxiom)
            self.text.insert(tk.END, sampleRule)

            self.comboSegmentLength.set('10')  # устанавливаем длину сегмента
            self.comboAngle.set('5')  # устанавливаем угол наклона
            self.comboDepth.set('10')  # устанавливаем поколение фрактала
            self.comboSizeLeaves1.set('4')  # размер листа
            self.comboSizeLeaves2.set('')  # размер листа
            self.comboSizeLeaves3.set('')  # размер листа
            self.comboSizeLeaves4.set('')  # размер листа
            self.comboPlantThickness.set('3')
            self.comboColorsLeaf1.set('Темно-зеленый')
            self.comboColorsLeaf2.set('')
            self.comboColorsLeaf3.set('')
            self.comboColorsLeaf4.set('')
            self.comboColorsTrunk1.set('Темно-розовый')
            self.comboColorsTrunk2.set('Темно-розовый')
            self.comboColorsTrunk3.set('Темно-розовый')
            self.comboPerLeaves1.set('1')
            self.comboPerLeaves2.set('')
            self.comboPerLeaves3.set('')
            self.comboPerLeaves4.set('')

        if selected_template == 'Говея':
            self.entry.delete(0, tk.END)
            self.text.delete("1.0", tk.END)
            sampleAxiom = 'W'
            sampleRule = (
                '("W", f"F(0.1, 2)[+({angle-20})Q][-({angle-20})Q][-({angle})YU] "),\n'
                '("Q", f"G(0.5, 1)-({4})[+({angle-8})XU]G(0.5, 1)[-({angle-8})YU][+({angle-20})XU]G(0.5, 1)[-({angle-8})YU] "),\n'
                '("X", f"F(0.4, 1)[+({angle })F(0.1, 1)U][-({angle })F(0.1, 1)U]+({1})X "),\n'
                '("Y", f"F(0.4, 1)[+({angle })F(0.1, 1)U][-({angle })F(0.1, 1)U]-({1})Y "),\n'
                '("F(x, y)", lambda x, y: f"F({1.6 * x}, {1.2 * y}) "),\n'
                '("G(x, y)", lambda x, y: f"G({1.6 * x}, {1.2 * y}) "),\n'
                '("H(x, y)", lambda x, y: f"H({1.2 * x}, {1.7 * y}) "),\n'
                '("+(x)", lambda x: f"+({x + random.triangular(0, 5, random.gauss(0, 1))})"),\n'
                '("-(x)", lambda x: f"-({x + random.triangular(0, 5, random.gauss(0, 1))})"),\n')
            self.entry.insert(tk.END, sampleAxiom)
            self.text.insert(tk.END, sampleRule)

            self.comboSegmentLength.set('20')  # устанавливаем длину сегмента
            self.comboAngle.set('25')  # устанавливаем угол наклона
            self.comboDepth.set('7')  # устанавливаем поколение фрактала
            self.comboSizeLeaves1.set('')  # размер листа
            self.comboSizeLeaves2.set('')  # размер листа
            self.comboSizeLeaves3.set('')  # размер листа
            self.comboSizeLeaves4.set('2')  # размер листа
            self.comboPlantThickness.set('1.15')
            self.comboColorsLeaf1.set('')
            self.comboColorsLeaf2.set('')
            self.comboColorsLeaf3.set('')
            self.comboColorsLeaf4.set('Зеленый')
            self.comboColorsTrunk1.set('Светло-зеленый')
            self.comboColorsTrunk2.set('Светло-зеленый')
            self.comboColorsTrunk3.set('Светло-зеленый')
            self.comboPerLeaves1.set('')
            self.comboPerLeaves2.set('')
            self.comboPerLeaves3.set('')
            self.comboPerLeaves4.set('1')


        if selected_template == 'Можжевельник':
            self.entry.delete(0, tk.END)
            self.text.delete("1.0", tk.END)
            sampleAxiom = 'HGGFF'
            sampleRule = (
                '("H", f"H(3, 4)[+({angle+15})G][-({angle+15})G]"),\n'
                '("F", f"F(1, 1)[-({angle})F(1, 1)[ F(1, 1)+({angle})+({angle})F(1, 1)F(0.5, 1)]][+({angle})F(1, 1)F(0.5, 1)[-({angle})F(1, 1)]]F(1, 1)"),\n'
                '("G", f"G(1, 1)[-({angle+6})G(1, 1)[ G(1, 1)+({angle+10})+({angle+6})G(1, 1)G(0.5, 1)]][+({angle+6})G(1, 1)G(0.5, 1)[-({angle+6})G(1, 1)]]G(1, 1)"),\n'
                '("F(x, y)", lambda x, y: f"F({1 * x}, {1.7 * y}) "),\n'
                '("G(x, y)", lambda x, y: f"G({1 * x}, {1.7 * y}) "),\n'
                '("H(x, y)", lambda x, y: f"H({1 * x}, {1.7 * y}) "),\n'
                '("+(x)", lambda x: f"+({x + random.triangular(0, 1, random.gauss(0, 1))})"),\n'
                '("-(x)", lambda x: f"-({x + random.triangular(0, 1, random.gauss(0, 1))})"),\n')
            self.entry.insert(tk.END, sampleAxiom)
            self.text.insert(tk.END, sampleRule)

            self.comboSegmentLength.set('6')  # устанавливаем длину сегмента
            self.comboAngle.set('15')  # устанавливаем угол наклона
            self.comboDepth.set('4')  # устанавливаем поколение фрактала
            self.comboSizeLeaves1.set('')  # размер листа
            self.comboSizeLeaves2.set('')  # размер листа
            self.comboSizeLeaves3.set('')  # размер листа
            self.comboSizeLeaves4.set('')  # размер листа
            self.comboPlantThickness.set('2.5')
            self.comboColorsLeaf1.set('')
            self.comboColorsLeaf2.set('')
            self.comboColorsLeaf3.set('')
            self.comboColorsLeaf4.set('')
            self.comboColorsTrunk1.set('Темно-голубой')
            self.comboColorsTrunk2.set('Темно-голубой')
            self.comboColorsTrunk3.set('Темно-коричневый')
            self.comboPerLeaves1.set('')
            self.comboPerLeaves2.set('')
            self.comboPerLeaves3.set('')
            self.comboPerLeaves4.set('')


        if selected_template == 'Лапчатка':
            self.entry.delete(0, tk.END)
            self.text.delete("1.0", tk.END)
            sampleAxiom = 'A'
            sampleRule = (
                '("A", f"F(1, 0.4)[++({angle})B][+({angle})B][-({angle})B][--({angle})B]"),\n'
                '("B", f"F(1, 0.4)[+({angle})G][-({angle})G]"),\n'
                '("G", f"G(1, 1)G(1, 1)[+({angle})G(1, 1)LLL][-({angle})-({angle})G(1, 1)F(1, 1)Z][-({angle})G(1, 1)+({angle})G(1, 1)LL]"),\n'
                '("F(x, y)", lambda x, y: f"F({1 * x}, {1.7 * y}) "),\n'
                '("G(x, y)", lambda x, y: f"G({1 * x}, {1.7 * y}) "),\n'
                '("H(x, y)", lambda x, y: f"H({1 * x}, {1.7 * y}) "),\n'
                '("+(x)", lambda x: f"+({x + random.triangular(0, 1, random.gauss(0, 1))})"),\n'
                '("-(x)", lambda x: f"-({x + random.triangular(0, 1, random.gauss(0, 1))})"),\n')
            self.entry.insert(tk.END, sampleAxiom)
            self.text.insert(tk.END, sampleRule)

            self.comboSegmentLength.set('15')  # устанавливаем длину сегмента
            self.comboAngle.set('18')  # устанавливаем угол наклона
            self.comboDepth.set('5')  # устанавливаем поколение фрактала
            self.comboSizeLeaves1.set('4')  # размер листа
            self.comboSizeLeaves2.set('3')  # размер листа
            self.comboSizeLeaves3.set('')  # размер листа
            self.comboSizeLeaves4.set('')  # размер листа
            self.comboPlantThickness.set('1.5')
            self.comboColorsLeaf1.set('Светло-зеленый')
            self.comboColorsLeaf2.set('Желтый')
            self.comboColorsLeaf3.set('')
            self.comboColorsLeaf4.set('')
            self.comboColorsTrunk1.set('Темно-голубой')
            self.comboColorsTrunk2.set('Темно-голубой')
            self.comboColorsTrunk3.set('Темно-голубой')
            self.comboPerLeaves1.set('1')
            self.comboPerLeaves2.set('1')
            self.comboPerLeaves3.set('')
            self.comboPerLeaves4.set('')


        if selected_template == 'Пальма':
            self.entry.delete(0, tk.END)
            self.text.delete("1.0", tk.END)
            sampleAxiom = 'WEQ'
            sampleRule = (
                '("W", f"H(1, 10) +({random.uniform(0, 6) })-({random.uniform(0, 6) })W  "),\n'
                '("X", f"F(0.2, 1)[+({angle })F(0.1, 1)U][-({angle })F(0.1, 1)U]F(0.2, 1)[+({angle })F(0.1, 1)U][-({angle })F(0.1, 1)U]+({random.uniform(5, 20)})X "),\n'
                '("Y", f"F(0.2, 1)[+({angle })F(0.1, 1)U][-({angle })F(0.1, 1)U]F(0.2, 1)[+({angle })F(0.1, 1)U][-({angle })F(0.1, 1)U]-({random.uniform(5, 20) })Y "),\n'
                '("C", f"F(0.2, 1)[+({angle })F(0.1, 1)U][-({angle })F(0.1, 1)U]F(0.2, 1)[+({angle })F(0.1, 1)U][-({angle })F(0.1, 1)U]-({random.uniform(1, 3) })C "),\n'
                '("Q", f"G(1, 1)[+++++++++SSIS+++++++SIS+++++++SSIS+++++++SISS+++++++SI++++++SI][+({angle-30 })XF(0.1, 1)U ][-({angle-30 })YF(0.1, 1)U ][-({angle+120 })CF(0.1, 1)U ] "),\n'
                '("E", f"G(1, 1)[+({angle })XF(1, 1)U][-({angle+20})YF(1, 1)U][+({angle+30 })XF(1, 1)U][-({angle+60})YF(1, 1)U] "),\n'
                '("F(x, y)", lambda x, y: f"F({1}, {1.2 * y}) "),\n'
                '("G(x, y)", lambda x, y: f"G({1 * x}, {7}) "),\n'
                '("H(x, y)", lambda x, y: f"H({1.5 * x}, {5 + y}) "),\n'
                '("+(x)", lambda x: f"+({x + random.triangular(0, 5, random.gauss(0, 1))})"),\n'
                '("-(x)", lambda x: f"-({x + random.triangular(0, 5, random.gauss(0, 1))})"),\n')
            self.entry.insert(tk.END, sampleAxiom)
            self.text.insert(tk.END, sampleRule)

            self.comboSegmentLength.set('13')  # устанавливаем длину сегмента
            self.comboAngle.set('18')  # устанавливаем угол наклона
            self.comboDepth.set('7')  # устанавливаем поколение фрактала
            self.comboSizeLeaves1.set('')  # размер листа
            self.comboSizeLeaves2.set('')  # размер листа
            self.comboSizeLeaves3.set('18')  # размер листа
            self.comboSizeLeaves4.set('2')  # размер листа
            self.comboPlantThickness.set('1.25')
            self.comboColorsLeaf1.set('')
            self.comboColorsLeaf2.set('')
            self.comboColorsLeaf3.set('Желтый')
            self.comboColorsLeaf4.set('Зеленый')
            self.comboColorsTrunk1.set('Светло-зеленый')
            self.comboColorsTrunk2.set('Светло-зеленый')
            self.comboColorsTrunk3.set('Темно-коричневый')
            self.comboPerLeaves1.set('')
            self.comboPerLeaves2.set('')
            self.comboPerLeaves3.set('1')
            self.comboPerLeaves4.set('1')






        if selected_template == 'Лаванда':
            self.entry.delete(0, tk.END)
            self.text.delete("1.0", tk.END)
            sampleAxiom = 'F(0.5, 0.5)RK'
            sampleRule = (
                '("R", f"[ -({angle})[QF(3, 0.5)X[++++LL]][R]]"),\n'
                '("K", f"[ +({angle})[EF(3, 0.5)Y[++++LL]][K]]"),\n'
                '("Q", f"+({5})H(0.5, 0.5)H(1, 0.5)[+({angle+30})U][-({angle+30})U]H(0.5, 0.5)Q "),\n'
                '("E", f"-({5})H(0.5, 0.5)H(1, 0.5)[-({angle+30})U][+({angle+30})U]H(0.5, 0.5)E"),\n'
                '("X", f"+({5}) [G(0.6, 0.5)[+({angle})G(0.2, 0.5)LL][G(0.2, 0.5)LL][-({angle})G(0.2, 0.5)LL]G(0.4, 0.5)X][S(0.6, 0.5)[+({angle})G(0.2, 0.5)LL][-({angle})+({angle})G(0.2, 0.5)LL][-({angle})G(0.2, 0.5)LL]S(0.4, 0.5)]"),\n'
                '("Y", f"-({5}) [G(0.6, 0.5)[+({angle})G(0.2, 0.5)LL][G(0.2, 0.5)LL][-({angle})G(0.2, 0.5)LL]G(0.4, 0.5)Y][S(0.6, 0.5)[+({angle})G(0.2, 0.5)LL][-({angle})+({angle})G(0.2, 0.5)LL][-({angle})G(0.2, 0.5)LL]S(0.4, 0.5)]"),\n'
                '("F(x, y)", lambda x, y: f"F({x}, { y})"),\n'
                '("G(x, y)", lambda x, y: f"G({x}, { y})"),\n'
                '("H(x, y)", lambda x, y: f"H({ x*1.2 }, { y})"),\n'
                '("S(x, y)", lambda x, y: f"S({x*1.1}, {y })"),\n'
                '("+(x)", lambda x: f"+({x + random.triangular(-3, 3, random.gauss(0, 2))})"),\n'
                '("-(x)", lambda x: f"-({x + random.triangular(-3, 3, random.gauss(0, 2))})"),\n')
            self.entry.insert(tk.END, sampleAxiom)
            self.text.insert(tk.END, sampleRule)

            self.comboSegmentLength.set('23')  # устанавливаем длину сегмента
            self.comboAngle.set('5')  # устанавливаем угол наклона
            self.comboDepth.set('7')  # устанавливаем поколение фрактала
            self.comboSizeLeaves1.set('2')  # размер листа
            self.comboSizeLeaves2.set('')  # размер листа
            self.comboSizeLeaves3.set('')  # размер листа
            self.comboSizeLeaves4.set('1')  # размер листа
            self.comboPlantThickness.set('4')
            self.comboColorsLeaf1.set('Фиолетовый')
            self.comboColorsLeaf2.set('')
            self.comboColorsLeaf3.set('')
            self.comboColorsLeaf4.set('Зеленый')
            self.comboColorsTrunk1.set('Светло-зеленый')
            self.comboColorsTrunk2.set('Светло-зеленый')
            self.comboColorsTrunk3.set('Светло-зеленый')
            self.comboPerLeaves1.set('1')
            self.comboPerLeaves2.set('')
            self.comboPerLeaves3.set('')
            self.comboPerLeaves4.set('1')

        if selected_template == 'Сосна':
            self.entry.delete(0, tk.END)
            self.text.delete("1.0", tk.END)
            sampleAxiom = 'X'
            sampleRule = (
                '("X", f" [G(0.4, 0.5)[G(0.2, 0.5)]G(0.4, 0.5)X][S(0.4, 0.5)[+({angle})G(0.2, 0.5)DI][-({angle})G(0.2, 0.5)DI][-({angle})+({angle}) Q]S(0.4, 0.5)[I]]"),\n'
                '("D", f"[ +({angle+20})XI]H(0.1, 0.5)[ -({angle+20})XI]H(0.1, 0.5)X", 0.5),\n'
                '("D", f"[ -({angle+20})XI]H(0.1, 0.5)[ +({angle+20})XI]H(0.1, 0.5)X", 0.5),\n'
                '("Q", f"[ -({angle+20})[I]X][ +({angle+20})[I]X]X"),\n'
                
                '("F(x, y)", lambda x, y: f"F({x * 1.5}, {y + 0.7})"),\n'
                '("H(x, y)", lambda x, y: f"H({x * 1.5}, {y + 0.7})"),\n'
                '("G(x, y)", lambda x, y: f"G({x * 1.5}, {y + 0.7})"),\n'
                '("S(x, y)", lambda x, y: f"S({x * 1.5}, {y + 0.7})"),\n'
                '("+(x)", lambda x: f"+({x + random.triangular(-1, 1, random.gauss(0, 1))})"),\n'
                '("-(x)", lambda x: f"-({x + random.triangular(-1, 1, random.gauss(0, 1))})"),\n'
           )
            self.entry.insert(tk.END, sampleAxiom)
            self.text.insert(tk.END, sampleRule)

            self.comboSegmentLength.set('40')  # устанавливаем длину сегмента
            self.comboAngle.set('20')  # устанавливаем угол наклона
            self.comboDepth.set('6')  # устанавливаем поколение фрактала
            self.comboSizeLeaves1.set('')  # размер листа
            self.comboSizeLeaves2.set('')  # размер листа
            self.comboSizeLeaves3.set('3')  # размер листа
            self.comboSizeLeaves4.set('')  # размер листа
            self.comboPlantThickness.set('2.5')
            self.comboColorsLeaf1.set('')
            self.comboColorsLeaf2.set('')
            self.comboColorsLeaf3.set('Зеленый')
            self.comboColorsLeaf4.set('')
            self.comboColorsTrunk1.set('Темно-коричневый')
            self.comboColorsTrunk2.set('Темно-коричневый')
            self.comboColorsTrunk3.set('Темно-коричневый')
            self.comboPerLeaves1.set('')
            self.comboPerLeaves2.set('')
            self.comboPerLeaves3.set('1')
            self.comboPerLeaves4.set('')

        if selected_template == 'Дерево':
            self.entry.delete(0, tk.END)
            self.text.delete("1.0", tk.END)
            sampleAxiom = 'L'
            sampleRule = (
                '("L", f"[G(0.6, 0.5)G(0.4, 0.5)L][S(0.6, 0.5)[+({angle-10})G(0.2, 0.5)L][-({angle-10})G(0.2, 0.5)L][-({angle+10})+({angle}) L]S(0.4, 0.5)]"),\n'
                 
               

                '("F(x, y)", lambda x, y: f"F({x * 1.72}, {y + 1.6})"),\n'
                '("H(x, y)", lambda x, y: f"H({x * 1.72}, {y + 1.6})"),\n'
                '("G(x, y)", lambda x, y: f"G({x * 1.72}, {y + 1.6})"),\n'
                '("S(x, y)", lambda x, y: f"S({x * 1.72}, {y + 1.6})"),\n'
                '("+(x)", lambda x: f"+({x + random.triangular(-2, 2, random.gauss(0, 2))})"),\n'
                '("-(x)", lambda x: f"-({x + random.triangular(-2, 2, random.gauss(0, 2))})"),\n'
            )
            self.entry.insert(tk.END, sampleAxiom)
            self.text.insert(tk.END, sampleRule)

            self.comboSegmentLength.set('18')  # устанавливаем длину сегмента
            self.comboAngle.set('40')  # устанавливаем угол наклона
            self.comboDepth.set('6')  # устанавливаем поколение фрактала
            self.comboSizeLeaves1.set('3')  # размер листа
            self.comboSizeLeaves2.set('')  # размер листа
            self.comboSizeLeaves3.set('2')  # размер листа
            self.comboSizeLeaves4.set('')  # размер листа
            self.comboPlantThickness.set('3')
            self.comboColorsLeaf1.set('Темно-голубой')
            self.comboColorsLeaf2.set('')
            self.comboColorsLeaf3.set('Темно-голубой')
            self.comboColorsLeaf4.set('')
            self.comboColorsTrunk1.set('Темно-коричневый')
            self.comboColorsTrunk2.set('Темно-коричневый')
            self.comboColorsTrunk3.set('Темно-коричневый')
            self.comboPerLeaves1.set('1')
            self.comboPerLeaves2.set('')
            self.comboPerLeaves3.set('1')
            self.comboPerLeaves4.set('')






gui = Gui()



