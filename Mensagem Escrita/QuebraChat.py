import pyautogui, time
time.sleep(1)

f = open('Mensagem', 'r')
for word in f:
    pyautogui.typewrite(word*50)
    pyautogui.press('enter')