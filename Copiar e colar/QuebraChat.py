# esse vai enviar a mensagem que você copiar

import pyautogui, time
time.sleep(1)
for i in range(15):
    pyautogui.hotkey('ctrl','v')
    pyautogui.press('enter')