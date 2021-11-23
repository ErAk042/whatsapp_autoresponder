# Whatsapp auto responder v1.2 by ErAk_v2
# Im bored send help pls



import time
import keyboard
import pyautogui

#---------How to use----------#
#
# 1-Put this script into a folder
# 2-Take a screenshot of the target persons name in whatsapp(Just the part where it shows who posted. Do not include anything else)
# 3-Name the image "img_1.png" and put it into the same folder with this script
# 4-Take a screenshot of the phrase that you want to respond at
# 5-Put it in the same folder and name it "img_2.png"
# 6-Type in what you want the bot to respond as and you are ready to go!
# Note- This was designed for whatsapp at 1080p resolution. You may need to change the region and coordinate values.



time.sleep(5)  # To avoid any possible malfunctions



while not keyboard.is_pressed('q'):  # Press q to exit the program
    start = pyautogui.locateCenterOnScreen('img_1.png', region=(0, 0, 1920, 1080), grayscale=True, confidence=0.70)  # Checks if the author of the message is the target person
    if start is not None:  # If it finds something
        msg = pyautogui.locateCenterOnScreen('img_2.png', region=(0, 0, 1920, 1080), grayscale=True, confidence=0.70)  # Checks if the message contains an certain word
        if msg is not None:
            pyautogui.moveTo(828, 990)  # Moves the mouse to the message box
            pyautogui.click()
            pyautogui.typewrite("xxxxxxxxxxxxxxxxxx.")  # Enter any text you want