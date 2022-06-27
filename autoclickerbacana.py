# Um click a cada 1.5 segundos.
# Ativar no play do canto superior direito
# Desativar ctrl c no terminal

import winddows
import pyautogui
import time
 
def key():
    if winddows.is_selected_window(): 
        time.sleep(1.5)     
        pyautogui.leftClick()  
 
def main():
    if winddows.init() is None:
        print ('Ok')
        time.sleep(3)
        return         
    print('Rodando')
    print('Desativar: CTRL+C')
    while True:
        key()
 
main()
