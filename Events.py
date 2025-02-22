from tkinter import END, SEL_LAST, SEL_FIRST, INSERT
import Params

def save():
    file = open("text", "w")
    file.write(Params.window.text_fild.get("1.0", END))
    file.close()

def copy_text(event):
    """Обработчик для сохранения текста"""
    text = Params.window.text_fild.get(SEL_FIRST, SEL_LAST)
    Params.window.clipboard_clear()
    Params.window.clipboard_append(text)
    print("Текст скопирован:", text)
    save()
    return "break"

def cut_text(event):
    """Обработчик для вырезания текста"""
    try:
        text = Params.window.text_fild.get(SEL_FIRST, SEL_LAST)
        Params.window.text_fild.delete(SEL_FIRST, SEL_LAST)
        Params.window.clipboard_clear()
        Params.window.clipboard_append(text)
        print("Текст вырезан и скопирован в буфер обмена.")
    except Params.window.TclError:
        print("Нет выделенного текста.")
        return
    save()
    return "break"

def undo_action(event):
    """Обработчик для отмены действия"""
    try:
        Params.window.text_fild.edit_undo()
        print("Действие отменено.")
    except Params.window.TclError:
        print("Нечего отменять.")
        return
    save()
    return "break"

def paste_text(event):
    """Обработчик для вставки текста"""
    try:
        text = Params.window.clipboard_get()
        Params.window.text_fild.insert(INSERT, text)
        print("Текст вставлен из буфера обмена.")
    except Params.window.TclError:
        print("Буфер обмена пуст.")
        return
    save()
    return "break"

def handle_key_combination(event):
    """Общий обработчик для комбинаций клавиш"""
    key = event.keycode
    if event.keysym in ["c", "C", "V", "v", "X", "x"]:
        return
    print(key)
    if event.keycode == 67:  # Код клавиши 'S'/'С'
        copy_text(event)
    if event.keycode == 88:  # Код клавиши 'X'/'Ч'
        cut_text(event)
    # elif event.keycode == 90:  # Код клавиши 'Z'/'Я'
    #     Params.window.undo_action(event)
    elif event.keycode == 86:  # Код клавиши 'V'/'М'
        paste_text(event)
    save()

def on_mouse_enter(event=None):
    if not Params.is_panel_open:
        Params.window.attributes('-alpha', 1.0)
        Params.window.slide_panel_in()


def on_mouse_leave(event=None):
    if Params.is_panel_open:
        Params.window.slide_panel_out()

