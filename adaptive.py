import keyboard
import time
import pyautogui
from pynput.mouse import Button, Controller

# For display 1920*1080
# ALL currently being used commanders MUST be field marshal
# It may malfunction during lag/autosave

def adapt():
    print('Move mouse to Create new army position and press .')
    global loca1
    while True:
        time.sleep(0.01)
        if keyboard.is_pressed('.'):
            time.sleep(0.01)
            loca1 = (pyautogui.position())
            print(loca1)
            break
    input('Press enter to continue...')


    print('Move mouse to New army position and press .')
    global loca2
    while True:
        time.sleep(0.01)
        if keyboard.is_pressed('.'):
            time.sleep(0.01)
            loca2 = (pyautogui.position())
            print(loca2)
            break
    input('Press enter to continue...')

    print('Move mouse to Assign new army general position and press .')
    global loca3
    while True:
        time.sleep(0.01)
        if keyboard.is_pressed('.'):
            time.sleep(0.01)
            loca3 = (pyautogui.position())
            print(loca3)
            break
    input('Press enter to continue...')

    print('Move mouse to bottom of the scroll and press .')
    global loca5
    while True:
        time.sleep(0.01)
        if keyboard.is_pressed('.'):
            time.sleep(0.01)
            loca5 = (pyautogui.position())
            print(loca5)
            break
    input('Press enter to continue...')

    print('Move mouse to top of the scroll and press .')
    global loca4
    while True:
        time.sleep(0.01)
        if keyboard.is_pressed('.'):
            time.sleep(0.01)
            loca4 = (pyautogui.position())
            print(loca4)
            break
    input('Press enter to continue...')

    print('Move mouse to face of the first general and press .')
    global loca6
    while True:
        time.sleep(0.01)
        if keyboard.is_pressed('.'):
            time.sleep(0.01)
            loca6 = (pyautogui.position())
            print(loca6)
            break
    input('Press enter to continue...')

    print('Move mouse to last stand and press .')
    global loca7
    while True:
        time.sleep(0.01)
        if keyboard.is_pressed('.'):
            time.sleep(0.01)
            loca7 = (pyautogui.position())
            print(loca7)
            break
    input('Press enter to continue...')

    print('Move mouse to original army position and press .')
    global loca8
    while True:
        time.sleep(0.01)
        if keyboard.is_pressed('.'):
            time.sleep(0.01)
            loca8 = (pyautogui.position())
            print(loca8)
            break
    input('Press enter to continue...')


def getSetting():
    global delay1
    delay1 = float(input(
        'delay between moving mouse and pressing recommended 0.05: '))  # delay between moving mouse and pressing
    # slightly dependent on lag
    global delay2
    delay2= float(
        input('delay for effect to take place recommended 0.1: '))  # delay for effect to take place highly dependent on lag
    global delay3
    delay3 = float(input('delay for scroll recommended 0.15: '))  # delay for scroll
    global delay4
    delay4 = float(input('delay before putting division back recommended 0.22: '))  # delay before putting back

    numFreeGen = int(input('How many unused generals + field marshals: '))  # How many unused generals + field marshals
    numGen = int(input(
        'How many generals + field marshals your country has: '))  # How many generals + field marshals your country has
    global numArmyGroup
    numArmyGroup = int(input('Number of army groups in the sector: '))  # Number of army groups in the sector
    global numArmy
    numArmy = int(input('Number of armies in the sector: '))  # Number of armies in the sector
    global startPosition
    startPosition = int(input('From No.which general to start: '))
    global usedGen
    usedGen = min(numFreeGen, numGen - 4)
    global spaceScroll
    spaceScroll = (loca5[1]-loca4[1]) / (numGen - 5)



def startAutoLastStand():
    counter = -1 + startPosition
    mouse = Controller()
    while True:

        time.sleep(0.01)

        if keyboard.is_pressed('.'):  # set hotkey
            try:
                counter += 1
                pyautogui.moveTo(loca1)
                time.sleep(delay1)
                mouse.click(Button.left)  # create new army
                time.sleep(delay2)
                pyautogui.moveTo(loca2)
                time.sleep(delay1)
                mouse.click(Button.left)  # click for general
                time.sleep(delay2)
                pyautogui.moveTo(loca3)
                time.sleep(delay1)
                mouse.click(Button.left)  # get general
                time.sleep(delay2)
                pyautogui.moveTo(loca4[0], loca4[1] + int((counter % usedGen) * spaceScroll))
                time.sleep(delay1)
                mouse.click(Button.left)  # scroll to general
                time.sleep(delay3)
                pyautogui.moveTo(loca6)
                time.sleep(delay1)
                mouse.click(Button.left)  # assign general
                time.sleep(delay2)
                pyautogui.moveTo(loca7)
                time.sleep(delay1)
                mouse.click(Button.left)  # last stand
                time.sleep(delay2)
                pyautogui.moveTo(loca8)
                time.sleep(delay4)
                mouse.click(Button.right)  # get laststanded army back to original army
                time.sleep(delay2)
                keyboard.press('enter')
                keyboard.press('enter')

                time.sleep(0.7)

            except:
                print('User movement interrupt')


if __name__ == '__main__':
    adapt()
    getSetting()
    startAutoLastStand()
