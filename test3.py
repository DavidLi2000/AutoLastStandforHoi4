import keyboard
import time
import pyautogui
from pynput.mouse import Button, Controller

# For display 1920*1080
# ALL currently being used commanders MUST be field marshal
# It may malfunction during lag/autosave


delay1 = float(input('delay between moving mouse and pressing recommended 0.02: '))  # delay between moving mouse and pressing slightly dependent on lag
delay2 = float(input('delay for effect to take place recommended 0.1: '))   # delay for effect to take place highly dependent on lag
delay3 = float(input('delay for scroll recommended 0.13: '))   # delay for scroll
delay4 = float(input('delay before putting division back recommended 0.2: '))   # delay before putting back

numFreeGen = int(input('How many unused generals + field marshals: '))    # How many unused generals + field marshals
numGen = int(input('How many generals + field marshals your country has: '))       # How many generals + field marshals your country has
numArmyGroup = int(input('Number of army groups in the sector: '))    # Number of army groups in the sector
numArmy = int(input('Number of armies in the sector: '))        # Number of armies in the sector
startPosition = int(input('From No.which general to start: '))
usedGen = min(numFreeGen, numGen - 4)
spaceScroll = 416 / (numGen - 5)

mouse = Controller()


def startAutoLastStand():
    counter = -1 + startPosition
    while True:

        time.sleep(0.01)

        if keyboard.is_pressed('.'):      # set hotkey
            try:
                counter += 1
                pyautogui.moveTo(1079 + (numArmy - 1) * 40 + (numArmyGroup - 1) * 51, 1015)
                time.sleep(delay1)
                mouse.click(Button.left)  # create new army
                time.sleep(delay2)
                pyautogui.moveTo(1037 + (numArmy - 1) * 40 + (numArmyGroup - 1) * 51, 1015)
                time.sleep(delay1)
                mouse.click(Button.left)  # click for general
                time.sleep(delay2)
                pyautogui.moveTo(32, 143)
                time.sleep(delay1)
                mouse.click(Button.left)  # get general
                time.sleep(delay2)
                pyautogui.moveTo(1270, 342 + int((counter % usedGen) * spaceScroll))
                time.sleep(delay1)
                mouse.click(Button.left)  # scroll to general
                time.sleep(delay3)
                pyautogui.moveTo(835, 369)
                time.sleep(delay1)
                mouse.click(Button.left)  # assign general
                time.sleep(delay2)
                pyautogui.moveTo(932, 818)
                time.sleep(delay1)
                mouse.click(Button.left)  # last stand
                time.sleep(delay2)
                pyautogui.moveTo(952 - (numArmy + numArmyGroup - 2) * 40, 1018)
                time.sleep(delay4)
                mouse.click(Button.right)  # get laststanded army back to original army
                time.sleep(delay2)
                keyboard.press('enter')
                keyboard.press('enter')

                time.sleep(0.7)

            except:
                print('User movement interrupt')

if __name__ == '__main__':
    startAutoLastStand()
