from threading import Thread
from tkinter import Menu
from pystray import Icon, MenuItem, Menu
from PIL import Image, ImageDraw
import Params

class Tray(Thread):
    def __init__(self):
        menu = Menu(MenuItem('Выход', self.close))
        icon = Icon("Panel", self.create_image(), "Программа в трее", menu)

        super().__init__(target=icon.run, daemon=True)
        self.start()

    def close(self, icon):
        icon.stop()
        Params.window.quit()
        Params.window.update()

    def create_image(self):
        width = 64
        height = 64
        fill_color = (0, 128, 255)

        image = Image.new('RGBA', (width, height), (0, 0, 0, 0))

        dc = ImageDraw.Draw(image)
        dc.ellipse((8, 8, width - 8, height - 8), fill=fill_color)
        return image