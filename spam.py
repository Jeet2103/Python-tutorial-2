import pyautogui as pt
import time
limit = int(input("Enter limit:"))
message = input("Enter message:")
time.sleep(5)
for i in range(limit):
    pt.typewrite(message)
    pt.press("enter")

