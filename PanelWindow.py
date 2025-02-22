from tkinter import WORD, BOTH, LEFT, END
from tkinter import Tk, Text, Frame

import Params
import Events

class Window(Tk):
    def __init__(self):
        super().__init__()
        self.setup_window()
        self.create_panel()

    def setup_window(self):
        # Размерность
        screen_width = self.winfo_screenwidth()
        screen_height = self.winfo_screenheight()

        # Настройка окна
        self.overrideredirect(True)
        self.attributes("-topmost", True)  # Размещения поверх всего

        # начальная x позиция
        # initial_x_position = screen_width - self.panel_width
        initial_x_position = screen_width - 5
        self.attributes('-alpha', 0.2)

        # Буквально "геометрия окна и его расположение" - Ширина*высоту+x+y
        self.geometry(f"{Params.panel_width}x{screen_height}+{initial_x_position}+0")

        # регистрация событий мыши
        self.bind("<Shift-Enter>", Events.on_mouse_enter) # мышь в зоне
        self.bind("<Leave>", Events.on_mouse_leave) # мышь вне зоны

    def create_panel(self):
        # Создаем панель
        self.panel_frame = Frame(self, width=Params.panel_width, height=self.winfo_screenheight(), bg="darkgray")
        self.panel_frame.pack(fill="both", expand=True)
        self.text_fild = Text(self.panel_frame,
                            bg='gray11',
                            fg='gray90',
                            padx=20,
                            pady=20,
                            wrap=WORD,
                            insertbackground='gray',
                            selectbackground='#8D917A',
                            spacing3=10,
                            width=30,
                            font='Arial 14 bold')

        self.text_fild.pack(padx=5, pady=5, expand=1, fill=BOTH, side=LEFT)
        try:
            text = open("text", "r")
        except:
            text = ""
        self.text_fild.insert(1.0, text.read())

        key_mapping = {
            's': 83,  # Английская "s"
            # 'S': 83,  # Английская "S" (заглавная)
            'ы': 107  # Русская "с"
        }

        self.text_fild.bind("<KeyPress>", lambda event: self.after(10, Events.save))
        self.text_fild.bind('<Control-KeyPress>', Events.handle_key_combination)


    def slide_panel_in(self):
        if Params.right:
            screen_width = self.winfo_screenwidth()
            x = self.winfo_x()

            if x-Params.slide_speed <= screen_width - Params.panel_width:
                x = screen_width - Params.panel_width+6
                self.geometry(f"{Params.panel_width}x{self.winfo_screenheight()}+{x}+0")
                Params.is_panel_open = True
                return

            if x > screen_width - Params.panel_width:
                x -= Params.slide_speed
                self.geometry(f"{Params.panel_width}x{self.winfo_screenheight()}+{x}+0")
                self.after(10, self.slide_panel_in)
            else:
                Params.is_panel_open = True

    def slide_panel_out(self):
        if Params.right:
            screen_width = self.winfo_screenwidth()
            x = self.winfo_x()

            if x+Params.slide_speed > screen_width:
                x = screen_width-5
                self.geometry(f"{Params.panel_width}x{self.winfo_screenheight()}+{x}+0")
                Params.is_panel_open = False
                self.attributes('-alpha', 0.2)
                return

            if x < screen_width-5:
                x += Params.slide_speed
                self.geometry(f"{Params.panel_width}x{self.winfo_screenheight()}+{x}+0")
                self.after(10, self.slide_panel_out)
                return
            else:
                Params.is_panel_open = False
                self.attributes('-alpha', 0.2)
                return