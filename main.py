from PanelWindow import Window
from Tray import Tray
import Params

Params.init()
Params.tray = Tray()
Params.window = Window()

Params.window.mainloop()