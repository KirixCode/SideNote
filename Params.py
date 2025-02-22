# начальные параметры
panel_width: int = 500
slide_speed: int = 10
right: bool = True

# объекты
tray: 'Tray'
window: 'Window'

# динамические параметры
is_panel_open: bool = False

def init():
    from PanelWindow import Window
    from Tray import Tray