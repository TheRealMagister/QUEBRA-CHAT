import pyautogui, time
time.sleep(1)

f = open('Mensagem', 'r')
for word in f:
    pyautogui.typewrite(word*10)
    pyautogui.pess('enter')