# Date: 11th November 2018
# Author: Scott Johnson
# Title: Morse Code Traslator & Thermometer for Micro:bit

# I guess the title speaks for itself.  I have written this code to remain within a loop
# meaning it should always work...  I have also written it such that no 'line errors' should
# be possible from any user actions... If you can generate one let me know  :-)

from microbit import *
import speech

def morse():

# Dictionary containing Morse Code letter & number translations

    translation = {
        "DoDa": "A",
        "DaDoDoDo": "B",
        "DaDoDaDo": "C",
        "DaDoDo": "D",
        "Do": "E",
        "DoDoDaDo": "F",
        "DaDaDo": "G",
        "DoDoDoDo": "H",
        "DoDo": "I",
        "DoDaDaDa": "J",
        "DaDoDa": "K",
        "DoDaDoDo": "L",
        "DaDa": "M",
        "DaDo": "N",
        "DaDaDa": "O",
        "DoDaDaDo": "P",
        "DaDaDoDa": "Q",
        "DoDaDo": "R",
        "DoDoDo": "S",
        "Da": "T",
        "DoDoDa": "U",
        "DoDoDoDa": "V",
        "DoDaDa": "W",
        "DaDoDoDa": "X",
        "DaDoDaDa": "Y",
        "DaDaDoDo": "Z",
        "DoDaDaDaDa": "1",
        "DoDoDaDaDa": "2",
        "DoDoDoDaDa": "3",
        "DoDoDoDoDa": "4",
        "DoDoDoDoDo": "5",
        "DaDoDoDoDo": "6",
        "DaDaDoDoDo": "7",
        "DaDaDaDoDo": "8",
        "DaDaDaDaDo": "9",
        "DaDaDaDaDa": "0",
        }

    # Button Values & Totals

    buttonA = 'Do'
    dot = Image('00000:00000:00900:00000:00000')
    buttonB = 'Da'
    dash = Image('00000:00000:09990:00000:00000')
    runningTotal = ''
    content = ''

    # Core Code

    # This code opens a file for storing the translated digits

    with open('morse_translations.txt', 'w') as file:
    
        while True:

    # This code will recognise that you have pressed the A button on
    # the micro:bit, which indicates that you want to add 'Do' to the 
    # runningTotal, which it will do as long as there is no live session
    # 'content'
    # CHANGE 20Nov18: When the button is pressed an image representing a dot will be displayed

            if button_a.is_pressed():
                if content == '':
                    runningTotal = runningTotal + buttonA
                    display.show(dot)
                    sleep(200)
                else:
                    display.show(Image.SAD)
                    sleep(1000)

    # This code will recognise that you have pressed the B button on the micro:bit, 
    # which indicates that you want to add 'Da' to the runningTotal, which it will 
    # do as long as there is no live session 'content'
    # CHANGE 20Nov18: When the button is pressed an image representing a dash will be displayed

            elif button_b.is_pressed():
                if content == '':
                    runningTotal = runningTotal + buttonB
                    display.show(dash)
                    sleep(200)
                else:
                    display.show(Image.SAD)
                    sleep(1000)

    # This code will recognise that you have shaken the micro:bit, which indicates
    # that you want to translate (via the translation Dictionary) the DOs and DAs 
    # collected in this session and display the ascocaited digit on the Micro:bit 
    # screen. If an invalid combination of DOs and DAs is entered it will display a
    # sad face on the Micro:bit screen. In both cases it will reset the
    # 'runningTotal'
    # CHANGE 18Nov18: The translated digit will now also be written to a file

            elif accelerometer.was_gesture('shake'):
                if runningTotal in translation:
                    file.write(translation.get(runningTotal))
                    display.show(translation.get(runningTotal))
                    sleep(1000)
                    runningTotal = ''
                else:
                    display.show(Image.SAD)
                    sleep(1000)
                    runningTotal = ''

    # This code will recognise that you have touched pin0 & pinGND on the micro:bit, 
    # which indiactes that you want to display the transalted morse code characters that have 
    # been saved to file in this session, to the screen of the micro:bit. It will only do this
    # if there is content, otherwise it will just display a sad face and reopen the file
    # CHANGE 28Nov18: The translated characters will now be spoken through an attached speaker
    # as well as being displayed on screen

            elif pin2.is_touched():
                file.close()
                with open('morse_translations.txt') as file:
                    content = file.read()
                if content != '':
                    display.show(content)
                    speech.say(content, speed=120, pitch=100, throat=100, mouth=200)
                    sleep(1000)
                else:
                    file = open('morse_translations.txt', 'w')
                    display.show(Image.SAD)
                    sleep(1000)

    # This code will recognise that you have turned the micro:bit face down, which will quit back to the 
    # menu and overwrite the current session file, allowing the user to start over with a fresh session file

            elif accelerometer.was_gesture('face down'):
                file.close()
                file = open('morse_translations.txt', 'w')
                content = ''
                display.show(Image.YES)
                sleep(1000)
                break

    # If none of the above are happening... This code will ensure the 
    # display remains blank

            else:
                display.clear()


def temp():
    # A basic function that tells you the ambient temperature in Centigrade & Fahrenheit
    degree = Image('00999:00909:00999:00000:00000')
    while True:
        # Button A for Centigrade
        if button_a.is_pressed():
            display.scroll(temperature())
            display.show(degree)
            sleep(500)
            display.show('C')
            sleep(500)
        
        # Button B for Fahrenheit
        elif button_b.is_pressed():
            temp = temperature() * 1.8 + 32
            display.scroll(temp)
            display.show(degree)
            sleep(500)
            display.show('F')
            sleep(500)

        # Upside down to quit
        elif accelerometer.was_gesture('face down'):
            break

        else:
            display.clear()


#WIP
#def torch():
#    tlight = Image('09990:99999:99999:99999:09990')
#    aswitch = 'off'
#    bswitch = 'off'
#    while True:
#        if button_a.was_pressed() and aswitch == 'off':
#            aswitch = 'on'
#            while aswitch == 'on':
#                display.show(tlight)
#                if button_a.was_pressed() and aswitch == 'on':
#                    aswitch = 'off'
#                    break
#
#        elif button_b.was_pressed() and bswitch == 'off':
#            bswitch = 'on'
#            while bswitch == 'on':
#                display.show(tlight)
#                sleep(300)
#                display.clear()
#                sleep(300)
#                if button_b.was_pressed() and bswitch == 'on':
#                    bswitch = 'off'
#                    break
#
#        elif accelerometer.was_gesture('face down'):
#            break
#
#        else:
#            display.clear()


def menu():
    # A menu to allow the user to pick which utility they would like to use
    qmark = Image('09990:90009:00990:00000:00900')
    display.show(qmark)
    while True:
        if button_a.is_pressed():
            sleep(500)
            return morse()
        elif button_b.is_pressed():
            sleep(500)
            return temp()
#        elif ?
#            sleep(500)
#            return torch()
        else:
            display.show(qmark)


while True:
    menu()
