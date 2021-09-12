import pyautogui, time
time.sleep(1)

f = open('Mensagem', 'r')
for word in f:
    pyautogui.typewrite(word*1)
    pyautogui.press('enter')