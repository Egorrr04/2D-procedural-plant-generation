
from tkinter import ttk, filedialog
from PIL import ImageGrab
from PIL import Image, ImageTk
import io

import pymsgbox


def save_canvas_as_png(self):
    file_path = filedialog.asksaveasfilename(defaultextension=".png", filetypes=[("PNG files", "*.png")])
    if file_path:
        x = self.canvas.winfo_rootx()
        y = self.canvas.winfo_rooty()
        width = self.canvas.winfo_width()
        height = self.canvas.winfo_height()

        size = min(width, height)  # Выбор минимальной стороны для создания квадрата

        # Вычисление координат для центрирования квадрата
        x1 = x + ((width - size) / 2)
        y1 = y + ((height - size) / 2)
        x2 = x1 + size
        y2 = y1 + size

        img = ImageGrab.grab(bbox=(x1, y1, x2, y2))

        # Преобразование изображения в режим RGBA, если оно уже не в этом режиме
        img = img.convert("RGBA")

        # Создание нового изображения с прозрачным фоном
        new_img = Image.new("RGBA", (size, size), (255, 255, 255, 0))

        # Получение данных оригинального изображения
        datas = img.getdata()

        # Создание списка для хранения данных нового изображения
        newData = []

        # Определение цвета фона, который мы хотим сделать прозрачным
        transparent_color = (173, 216, 230)  # RGB значения для цвета "lightblue"

        # Проход по каждому пикселю в оригинальном изображении
        for item in datas:
            # Если пиксель соответствует цвету фона, делаем его прозрачным
            if item[:3] == transparent_color:
                newData.append((255, 255, 255, 0))
            else:
                newData.append(item)

        # Обновление нового изображения обработанными данными
        new_img.putdata(newData)

        # Сохранение нового изображения
        new_img.save(file_path)
        print("Изображение сохранено как", file_path)