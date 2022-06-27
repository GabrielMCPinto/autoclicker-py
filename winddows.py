import time
import win32gui

def iter_windows(callback):
    ctx = {'count': 0}
    def winEnumHandler( hwnd, ctx):
        name = win32gui.GetWindowText( hwnd )
        if win32gui.IsWindowVisible( hwnd ) and len(name) > 2:
            ctx['count'] += 1
            callback(hwnd, name, ctx['count'])

    win32gui.EnumWindows( winEnumHandler, ctx )

def select_window():
    windows = []
    def callback(hwnd, name, i):
        nonlocal windows
        print("{}. '{}'".format(len(windows), name))
        windows.append(hwnd)
    iter_windows(callback)
    i = input("Número da janela: ")
    try:
        i = int(i)
    except ValueError:
        return None  
    if i >= len(windows) or i < 0:
        return None

    return windows[i]
def init():
    global WINDOW
    WINDOW = select_window()
    return WINDOW 

def is_selected_window():
    window = win32gui.GetForegroundWindow()
    return WINDOW == win32gui.GetForegroundWindow()
